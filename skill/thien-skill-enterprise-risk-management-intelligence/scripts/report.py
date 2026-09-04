#!/usr/bin/env python3
"""Validated ERM reporting snapshot and offline HTML. No network, no overwrites."""
import argparse
import hashlib
import json
from collections import defaultdict
from datetime import date
from pathlib import Path
from erm_core import aggregate_losses, concentration, evaluate_metric, headroom, json_default, load_json, portfolio_status, write_json
from validate_engagement import validate


def prepare(data):
    validation = validate(data)
    ctx = data['context']
    metrics = []
    for metric in data['metrics']:
        obs = sorted([o for o in data['observations'] if o['metric_id'] == metric['id']], key=lambda o: o['as_of'])
        latest = obs[-1] if obs else None
        quality = latest['quality'] if latest else 'missing'
        if latest and (date.fromisoformat(ctx['as_of']) - date.fromisoformat(latest['as_of'])).days > metric['max_age_days']:
            quality = 'stale'
        value = latest['value'] if latest else None
        result = evaluate_metric(value, metric, quality)
        room = []
        if result['status'] not in ('UNKNOWN', 'DRAFT'):
            for rule in metric['rules']:
                if rule['severity'] == 'breach':
                    room.append(dict(op=rule['op'],limit=rule['threshold'],**headroom(value, rule['threshold'],
                                     'higher' if rule['op'].startswith('>') else 'lower')))
        if metric['bad_direction'] != 'higher' or not metric.get('utilization_applicable', True):
            for entry in room:
                entry['utilization'] = None
        metrics.append(dict(**metric,value=value,observed_at=latest['as_of'] if latest else None,
                            quality=quality,**result,headroom=room,history=obs))
    methods = {m['id']: m for m in data['methods']}
    risks = []
    for risk in data['risks']:
        assessments = [a for a in data['assessments'] if a['risk_id'] == risk['id']]
        # Preserve one latest assessment per basis/method. Never choose between methods silently.
        latest = {}
        for a in sorted(assessments, key=lambda a: a['as_of']):
            latest[(a['basis'], a['method_id'])] = dict(**a,approval=methods[a['method_id']]['approval'])
        results = [m for m in metrics if risk['id'] in m['risk_ids']]
        risks.append(dict(**risk,assessments=list(latest.values()),appetite=portfolio_status(results)))
    groups = defaultdict(list)
    for loss in data['losses']:
        groups[(loss['currency'],loss['horizon'],loss['scope'])].append(loss)
    totals = []
    for (currency,horizon,scope),losses in groups.items():
        total = aggregate_losses(losses,currency,horizon,scope)
        weights = [x['amount'] for x in losses if not x['eliminated']]
        totals.append(dict(**total,horizon=horizon,scope=scope,unit=ctx['unit'],
                           loss_concentration=concentration(weights) if weights else None))
    canonical = json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)
    summary = portfolio_status(metrics)
    summary['risk_count'] = len(risks)
    summary['treatment_count'] = len(data['treatments'])
    summary['decision'] = ctx['decision']
    return dict(context=ctx,source_sha256=hashlib.sha256(canonical.encode()).hexdigest(),
                summary=summary,risks=risks,metrics=metrics,loss_totals=totals,validation=validation,snapshot=data)


def render_html(report):
    template = Path(__file__).resolve().parents[1] / 'assets/dashboard.html'
    payload = json.dumps(report,ensure_ascii=False,default=json_default,allow_nan=False)
    payload = payload.replace('&','\\u0026').replace('<','\\u003c').replace('>','\\u003e')
    return template.read_text(encoding='utf-8').replace('__ERM_PAYLOAD__',payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot')
    parser.add_argument('--out',required=True,help='New directory for report.json and dashboard.html')
    args = parser.parse_args()
    try:
        report = prepare(load_json(args.snapshot))
        out = Path(args.out)
        out.mkdir(parents=True,exist_ok=False)
        write_json(report,out/'report.json')
        (out/'dashboard.html').write_text(render_html(report),encoding='utf-8')
        print(f'Created {out}; Office export is a separate capability-dependent operation.')
    except (ValueError,KeyError,TypeError,OSError) as exc:
        parser.exit(2,f'error: {exc}\n')


if __name__ == '__main__':
    main()
