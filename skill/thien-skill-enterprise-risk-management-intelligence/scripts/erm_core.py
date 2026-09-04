#!/usr/bin/env python3
"""Portable ERM arithmetic. Standard library only; no network or installation."""
import argparse
import hashlib
import json
import inspect
import math
import random
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path


class InputError(ValueError):
    pass


def number(value, name="value", minimum=None, maximum=None):
    if value is None or isinstance(value, bool):
        raise InputError(f"{name}: missing or boolean is not a number")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise InputError(f"{name}: invalid number") from None
    if not result.is_finite() or abs(result) > Decimal('1e30'):
        raise InputError(f"{name}: finite magnitude <= 1e30 required")
    if minimum is not None and result < Decimal(str(minimum)):
        raise InputError(f"{name}: below {minimum}")
    if maximum is not None and result > Decimal(str(maximum)):
        raise InputError(f"{name}: above {maximum}")
    return result


def nonnegative(value):
    return number(value, minimum=0)


def rate(value):
    return number(value, minimum=0, maximum=1)


def arithmetic(left, operator, right):
    """Small business calculations without eval or an artificial engagement."""
    left, right = number(left), number(right)
    if operator not in ('+', '-', '*', '/'):
        raise InputError('arithmetic operator must be +, -, * or /')
    if operator == '/' and right == 0:
        raise InputError('arithmetic division by zero')
    result = {'+': lambda: left+right, '-': lambda: left-right,
              '*': lambda: left*right, '/': lambda: left/right}[operator]()
    return dict(left=left, operator=operator, right=right, result=result)


def margin(price, volume, unit_cost, fixed_cost):
    price, volume, unit_cost, fixed_cost = map(nonnegative, (price, volume, unit_cost, fixed_cost))
    revenue = price * volume
    contribution = (price - unit_cost) * volume
    profit = contribution - fixed_cost
    return dict(revenue=revenue, contribution=contribution, profit=profit,
                margin=profit / revenue if revenue else None)


def pass_through(price, volume, unit_cost, fixed_cost, cost_change, pass_through_rate, volume_change):
    new_price = nonnegative(price) + number(cost_change) * rate(pass_through_rate)
    new_cost = nonnegative(unit_cost) + number(cost_change)
    new_volume = nonnegative(volume) * (1 + number(volume_change, minimum=-1))
    baseline = margin(price, volume, unit_cost, fixed_cost)
    scenario = margin(new_price, new_volume, new_cost, fixed_cost)
    # Price/cost effects use scenario volume; volume effect uses baseline margin.
    # This allocates interaction once and keeps displayed factors reproducible.
    terms = [
        ('price', new_price - nonnegative(price), new_volume, 'price_change × scenario_volume'),
        ('cost', nonnegative(unit_cost) - new_cost, new_volume, '-cost_change × scenario_volume'),
        ('volume', new_volume - nonnegative(volume), nonnegative(price) - nonnegative(unit_cost),
         'volume_change_units × baseline_unit_contribution'),
    ]
    components = [dict(driver=driver, factors=[a, b], formula=formula, amount=a*b)
                  for driver, a, b, formula in terms]
    delta = scenario['profit'] - baseline['profit']
    total = sum((term['amount'] for term in components), Decimal(0))
    return dict(baseline=baseline, scenario=scenario, profit_change=delta,
                profit_bridge=dict(components=components, total=total,
                                   reconciliation_difference=total-delta))


def working_capital(sales, cogs, dso, dio, dpo, days):
    sales, cogs, dso, dio, dpo = map(nonnegative, (sales, cogs, dso, dio, dpo))
    days = number(days, minimum=1)
    ar, inventory, ap = sales * dso / days, cogs * dio / days, cogs * dpo / days
    return dict(ar=ar, inventory=inventory, ap=ap, nwc=ar + inventory - ap)


def cash_waterfall(opening, inflows, outflows, burn_per_period):
    opening = nonnegative(opening)
    incoming = sum(map(nonnegative, inflows), Decimal(0))
    outgoing = sum(map(nonnegative, outflows), Decimal(0))
    closing = opening + incoming - outgoing
    burn = number(burn_per_period)
    return dict(closing_cash=closing, runway_periods=max(closing, Decimal(0)) / burn if burn > 0 else None,
                runway_basis='closing_cash/net_burn', liquidity_shortfall=max(-closing, Decimal(0)))


def credit(gross, eligible_collateral, pd, lgd):
    net = max(nonnegative(gross) - nonnegative(eligible_collateral), Decimal(0))
    return dict(net_exposure=net, expected_loss=net * rate(pd) * rate(lgd))


def concentration(exposures):
    if not exposures:
        raise InputError('exposures required')
    vals = list(map(nonnegative, exposures))
    total = sum(vals)
    if not total:
        return dict(total=total, shares=None, hhi=None, largest_share=None)
    shares = [x / total for x in vals]
    return dict(total=total, shares=shares, hhi=sum(x * x for x in shares), largest_share=max(shares))


def disruption(demand, available_capacity, unit_contribution, recovery_cost, penalty):
    units = max(nonnegative(demand) - nonnegative(available_capacity), Decimal(0))
    contribution = nonnegative(unit_contribution)
    loss = units * contribution + nonnegative(recovery_cost) + nonnegative(penalty)
    return dict(lost_units=units, incremental_loss=loss)


def quality(units, rework_rate, unit_rework_cost, recall_units, unit_recall_cost, incident_cost):
    rework = nonnegative(units) * rate(rework_rate) * nonnegative(unit_rework_cost)
    recall = nonnegative(recall_units) * nonnegative(unit_recall_cost)
    return dict(rework_cost=rework, recall_cost=recall,
                incremental_loss=rework + recall + nonnegative(incident_cost))


def inventory(stock, demand, unit_contribution, obsolete_units, carrying_cost, markdown_units, unit_discount):
    stock, demand, obsolete_units, markdown_units = map(nonnegative, (stock, demand, obsolete_units, markdown_units))
    if obsolete_units + markdown_units > stock:
        raise InputError('obsolete and markdown buckets must be disjoint and within stock')
    shortfall = max(demand - (stock - obsolete_units), Decimal(0))
    loss = shortfall * nonnegative(unit_contribution) + obsolete_units * nonnegative(carrying_cost)
    loss += markdown_units * nonnegative(unit_discount)
    return dict(shortfall_units=shortfall, incremental_loss=loss)


def project_eac(budget, actual_cost, etc, baseline_finish_day, forecast_finish_day):
    eac = nonnegative(actual_cost) + nonnegative(etc)
    return dict(eac=eac, cost_variance=nonnegative(budget) - eac,
                delay_days=max(number(forecast_finish_day) - number(baseline_finish_day), Decimal(0)))


def headroom(value, limit, direction):
    value, limit = number(value), number(limit)
    if direction not in ('higher', 'lower'):
        raise InputError('headroom direction must be higher (ceiling) or lower (floor)')
    return dict(headroom=limit - value if direction == 'higher' else value - limit,
                utilization=value / limit if direction == 'higher' and limit > 0 and value >= 0 else None)


def treatment(initial_cost, net_benefits, discount_rate, budget, required_resources, available_resources):
    initial_cost = nonnegative(initial_cost)
    discount = number(discount_rate, minimum=0)
    flows = list(map(number, net_benefits))
    if len(flows) > 1000:
        raise InputError('maximum 1000 periods')
    npv = -initial_cost + sum((v / ((1 + discount) ** (i + 1)) for i, v in enumerate(flows)), Decimal(0))
    return dict(npv=npv, budget_feasible=initial_cost <= nonnegative(budget),
                resources_feasible=nonnegative(required_resources) <= nonnegative(available_resources),
                approval='recommendation_only')


SEVERITIES = {'within': 0, 'warning': 1, 'breach': 2, 'capacity_breach': 3}
OPS = {'>': lambda a, b: a > b, '>=': lambda a, b: a >= b,
       '<': lambda a, b: a < b, '<=': lambda a, b: a <= b}


def validate_rules(metric):
    direction = metric['bad_direction']
    if direction not in ('higher', 'lower', 'two_sided'):
        raise InputError('bad_direction invalid')
    rules = metric['rules']
    for rule in rules:
        if rule['op'] not in OPS or rule['severity'] not in ('warning', 'breach', 'capacity_breach'):
            raise InputError('invalid predicate/severity')
        if direction == 'higher' and rule['op'] not in ('>', '>='):
            raise InputError('higher-bad direction has a lower predicate')
        if direction == 'lower' and rule['op'] not in ('<', '<='):
            raise InputError('lower-bad direction has an upper predicate')
        number(rule['threshold'])
    for prefix in ('>', '<'):
        side = [r for r in rules if r['op'].startswith(prefix)]
        levels = [r['severity'] for r in side]
        if len(set(levels)) != len(levels):
            raise InputError('duplicate severity on the same side')
        side.sort(key=lambda r: SEVERITIES[r['severity']])
        for previous, current in zip(side, side[1:]):
            a, b = number(previous['threshold']), number(current['threshold'])
            if (prefix == '>' and a > b) or (prefix == '<' and a < b):
                raise InputError('capacity/limit/warning order is inverted')
    if direction == 'two_sided':
        lower = [number(r['threshold']) for r in rules if r['op'].startswith('<')]
        upper = [number(r['threshold']) for r in rules if r['op'].startswith('>')]
        if lower and upper and max(lower) >= min(upper):
            raise InputError('two-sided warning interval must be nonempty')


def evaluate_metric(value, metric, quality='valid'):
    validate_rules(metric)
    if metric['approval'] != 'approved':
        return dict(status='DRAFT', reason='method_not_approved', matched=[])
    if value is None or quality != 'valid' or not metric['rules']:
        return dict(status='UNKNOWN', reason='missing_stale_or_unconfigured', matched=[])
    value = number(value)
    matched = [r['severity'] for r in metric['rules'] if OPS[r['op']](value, number(r['threshold']))]
    status = max(matched, key=SEVERITIES.get) if matched else 'within'
    return dict(status=status, reason='evaluated', matched=matched)


def portfolio_status(results):
    known = [r['status'] for r in results if r['status'] in SEVERITIES]
    unknown = sum(r['status'] not in SEVERITIES for r in results)
    return dict(known_status=max(known, key=SEVERITIES.get) if known else 'UNKNOWN',
                incomplete=bool(unknown) or not results, unresolved_metrics=unknown,
                confirmed_breaches=sum(r['status'] in ('breach', 'capacity_breach') for r in results))


def aggregate_losses(records, currency, horizon, scope):
    seen, total, eliminated = {}, Decimal(0), Decimal(0)
    for item in records:
        if not item.get('id'):
            raise InputError('economic loss id required')
        if (item['currency'], item['horizon'], item['scope']) != (currency, horizon, scope):
            raise InputError('mixed currency/horizon/scope; reconcile before aggregation')
        if not isinstance(item.get('eliminated', False), bool):
            raise InputError('eliminated must be boolean')
        amount = nonnegative(item['amount'])
        signature = (amount, item.get('eliminated', False))
        if item['id'] in seen:
            if seen[item['id']] != signature:
                raise InputError('conflicting records for one economic loss id')
            continue
        seen[item['id']] = signature
        if signature[1]:
            eliminated += amount
        else:
            total += amount
    return dict(total=total, eliminated=eliminated, unique_loss_count=len(seen), currency=currency)


def simulate_margin(price, unit_cost, volume, fixed_cost, seed, draws):
    if isinstance(draws, bool) or not isinstance(draws, int) or not 10 <= draws <= 100000:
        raise InputError('draws: integer in [10, 100000]')
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise InputError('explicit integer seed required')
    triples = []
    for name, triple in [('price', price), ('unit_cost', unit_cost), ('volume', volume)]:
        if not isinstance(triple, list) or len(triple) != 3:
            raise InputError(f'{name}: [low, mode, high] required')
        lo, mode, hi = map(nonnegative, triple)
        if not lo <= mode <= hi:
            raise InputError(f'{name}: require low <= mode <= high')
        triples.append(tuple(map(float, (lo, hi, mode))))
    rng = random.Random(seed)
    fixed = float(nonnegative(fixed_cost))
    samples = []
    for _ in range(draws):
        p, c, v = [rng.triangular(*triple) for triple in triples]
        samples.append((p - c) * v - fixed)
    samples.sort()
    def percentile(p):
        index = (draws - 1) * p
        lo, hi = math.floor(index), math.ceil(index)
        return samples[lo] + (samples[hi] - samples[lo]) * (index - lo)
    return dict(p05=percentile(.05), p50=percentile(.5), p95=percentile(.95),
                mean=sum(samples) / draws, seed=seed, draws=draws,
                limitation='Independent triangular assumptions; not calibrated or validated forecast')


OPERATIONS = {f.__name__: f for f in (margin, pass_through, working_capital, cash_waterfall,
              credit, concentration, disruption, quality, inventory, project_eac, headroom,
              treatment, aggregate_losses, simulate_margin, arithmetic)}


def json_default(value):
    if isinstance(value, Decimal):
        return format(value, 'f')
    raise TypeError(type(value).__name__)


def reject_pairs(pairs):
    obj = {}
    for key, val in pairs:
        if key in obj:
            raise InputError(f'duplicate JSON key: {key}')
        obj[key] = val
    return obj


def load_json(path):
    def reject_constant(value):
        raise InputError(f'nonfinite JSON: {value}')
    with Path(path).open(encoding='utf-8') as f:
        return json.load(f, object_pairs_hook=reject_pairs, parse_constant=reject_constant)


def write_json(value, path=None):
    text = json.dumps(value, ensure_ascii=False, indent=2, default=json_default, allow_nan=False) + '\n'
    if path:
        with Path(path).open('x', encoding='utf-8') as f:
            f.write(text)
    else:
        print(text, end='')


def calculate(request):
    operation = request['operation']
    if operation not in OPERATIONS:
        raise InputError(f'unsupported operation {operation}')
    context = request['context']
    if not isinstance(context, dict):
        raise InputError('context must be an object: unit, currency, horizon, source_refs')
    for field in ('unit', 'currency', 'horizon', 'source_refs'):
        if not context.get(field):
            raise InputError(f'context.{field} required; label synthetic or assumptions honestly')
    with localcontext() as ctx:
        ctx.prec = 34
        outputs = OPERATIONS[operation](**request['parameters'])
    return dict(operation=operation, formula_reference='references/scenarios-portfolio.md',
                parameters=request['parameters'], context=context, outputs=outputs)


def canonical_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'),
                      default=json_default, allow_nan=False)


_NO_COMPARISON = object()


def checked_calculation(request, comparison=_NO_COMPARISON):
    """Execute now, optionally reconcile a raw result, then generate the text.

    No caller-supplied status can enable verification. Hashes identify content,
    not historical execution or authentic enterprise sources. This is not a
    verifier for arbitrary prose or a security boundary against modified code.
    """
    if not isinstance(request, dict) or set(request) != {'operation', 'parameters', 'context'}:
        raise InputError('checked request requires only operation, parameters and context')
    snapshot = json.loads(canonical_json(request))
    context = snapshot['context']
    if not isinstance(context, dict):
        raise InputError('context must be an object')
    for field in ('unit', 'currency', 'horizon'):
        if not isinstance(context.get(field), str) or not context[field].strip():
            raise InputError(f'context.{field} must be nonempty text')
    refs = context.get('source_refs')
    if not isinstance(refs, list) or not refs or any(not isinstance(x, str) or not x.strip() for x in refs):
        raise InputError('context.source_refs must be a nonempty list of source labels')
    if not isinstance(snapshot['parameters'], dict):
        raise InputError('parameters must be an object')
    result = calculate(snapshot)  # Always execute, even if comparison says PASS.
    bridge = result['outputs'].get('profit_bridge')
    if bridge is not None:
        with localcontext() as ctx:
            ctx.prec = 34
            terms = bridge['components']
            if (any(t['factors'][0]*t['factors'][1] != t['amount'] for t in terms)
                    or sum((t['amount'] for t in terms), Decimal(0)) != bridge['total']
                    or bridge['total'] != result['outputs']['profit_change']
                    or bridge['total'] != result['outputs']['scenario']['profit']-result['outputs']['baseline']['profit']
                    or bridge['reconciliation_difference'] != 0):
                raise InputError('profit bridge does not reconcile')
    comparing = comparison is not _NO_COMPARISON
    if comparing and canonical_json(comparison) != canonical_json(result):
        raise InputError('comparison differs from executed calculation (input/context/output); no checked result emitted')
    engine = Path(__file__)
    verification = dict(status='EXECUTED', comparison='MATCH' if comparing else 'NOT_REQUESTED',
        input_sha256=hashlib.sha256(canonical_json(snapshot).encode()).hexdigest(),
        calculation_sha256=hashlib.sha256(canonical_json(result).encode()).hexdigest(),
        engine_sha256=hashlib.sha256(engine.read_bytes()).hexdigest(),
        skill_version=(engine.parents[1]/'VERSION').read_text().strip())
    lines = ['Đã thực thi phép tính: ' + result['operation'] + '.',
             'Phạm vi kiểm chứng: phép tính dưới đây theo input được cung cấp.',
             'Không xác minh nguồn dữ liệu, giả định, mô hình hay phê duyệt kinh doanh.']
    if comparing:
        lines.append('Đã đối soát input/context/output với kết quả cung cấp bằng lần tính mới.')
    if result['operation'] == 'arithmetic':
        out = result['outputs']
        lines.append(f"({out['left']}) {out['operator']} ({out['right']}) = {out['result']}")
    if bridge is not None:
        for term in bridge['components']:
            a, b = term['factors']
            lines.append(f"{term['driver']}: ({a}) × ({b}) = {term['amount']}")
        lines.append(f"Tổng bridge = {bridge['total']}; thay đổi lợi nhuận = {result['outputs']['profit_change']}")
    lines += ['Input và kết quả (đơn vị/kỳ trong context; tỷ lệ margin/utilization là tỷ số):',
              '```json', json.dumps(result, ensure_ascii=False, indent=2, default=json_default, allow_nan=False),
              '```', 'Dấu vết nội dung, không phải chữ ký xác thực hay bằng chứng lịch sử:',
              canonical_json(verification)]
    return dict(calculation=result, verification=verification, text='\n'.join(lines)+'\n')


def main():
    parser = argparse.ArgumentParser(description='ERM calculator; operations: ' + ', '.join(OPERATIONS),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='JSON keys: operation, parameters (object), context (object with unit, currency, horizon, source_refs).\n'
               + 'Parameter names by operation:\n' + '\n'.join(name + str(inspect.signature(fn)) for name, fn in OPERATIONS.items()))
    parser.add_argument('--input', required=True, help='Path to a JSON file, not inline JSON text')
    parser.add_argument('--output', help='New JSON file (text with --text); never overwrites')
    parser.add_argument('--checked', action='store_true', help='Execute and generate calculation, provenance and fixed checked text')
    parser.add_argument('--compare', help='Raw calculator JSON to reconcile against this new execution; requires --checked')
    parser.add_argument('--text', action='store_true', help='Emit only generated checked text; requires --checked')
    args = parser.parse_args()
    if (args.compare is not None or args.text) and not args.checked:
        parser.error('--compare/--text require --checked')
    try:
        request = load_json(args.input)
        if args.checked:
            result = checked_calculation(request, load_json(args.compare) if args.compare is not None else _NO_COMPARISON)
            if args.text:
                if args.output:
                    with Path(args.output).open('x', encoding='utf-8') as f:
                        f.write(result['text'])
                else:
                    print(result['text'], end='')
            else:
                write_json(result, args.output)
        else:
            write_json(calculate(request), args.output)
    except (ValueError, KeyError, TypeError, OSError, ArithmeticError) as exc:
        parser.exit(2, f"{'UNCHECKED' if args.checked else 'error'}: {exc}\n")


if __name__ == '__main__':
    main()
