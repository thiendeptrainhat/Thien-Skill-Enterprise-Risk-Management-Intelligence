#!/usr/bin/env python3
"""Validate this bundled schema subset, references and ERM snapshot semantics.

This is deliberately not a general JSON Schema implementation. Unsupported
keywords fail closed. Standard library only; never resolves remote references.
"""
import argparse
from datetime import date
from pathlib import Path
from erm_core import InputError, load_json, number, validate_rules, write_json

SCHEMA = Path(__file__).resolve().parents[1] / 'schemas/engagement.schema.json'
KEYWORDS = {'$schema', '$id', '$defs', '$ref', 'title', 'type', 'enum', 'properties',
            'required', 'additionalProperties', 'items', 'minLength', 'minimum',
            'maximum', 'format'}


def check_schema(node):
    unknown = set(node) - KEYWORDS
    if unknown:
        raise InputError(f'unsupported schema keywords: {sorted(unknown)}')
    for key in ('$defs', 'properties'):
        for child in node.get(key, {}).values():
            check_schema(child)
    if 'items' in node:
        check_schema(node['items'])


def matches(value, kind):
    return {'object': lambda: isinstance(value, dict),
            'array': lambda: isinstance(value, list),
            'string': lambda: isinstance(value, str),
            'integer': lambda: isinstance(value, int) and not isinstance(value, bool),
            'number': lambda: isinstance(value, (int, float)) and not isinstance(value, bool),
            'boolean': lambda: isinstance(value, bool),
            'null': lambda: value is None}[kind]()


def walk(value, spec, root, path='$'):
    if '$ref' in spec:
        if not spec['$ref'].startswith('#/$defs/'):
            raise InputError('only bundled definition references allowed')
        return walk(value, root['$defs'][spec['$ref'].split('/')[-1]], root, path)
    kinds = spec.get('type')
    if kinds and not any(matches(value, k) for k in (kinds if isinstance(kinds, list) else [kinds])):
        raise InputError(f'{path}: wrong type')
    if 'enum' in spec and value not in spec['enum']:
        raise InputError(f'{path}: not in enum')
    if isinstance(value, dict):
        missing = set(spec.get('required', [])) - set(value)
        unknown = set(value) - set(spec.get('properties', {}))
        if missing or (unknown and spec.get('additionalProperties') is False):
            raise InputError(f'{path}: missing={sorted(missing)}, unknown={sorted(unknown)}')
        for key, val in value.items():
            if key in spec.get('properties', {}):
                walk(val, spec['properties'][key], root, f'{path}.{key}')
    elif isinstance(value, list):
        for i, val in enumerate(value):
            walk(val, spec['items'], root, f'{path}[{i}]')
    elif isinstance(value, str):
        if len(value.strip()) < spec.get('minLength', 0):
            raise InputError(f'{path}: empty string')
        if spec.get('format') == 'date':
            try:
                if date.fromisoformat(value).isoformat() != value:
                    raise ValueError('noncanonical date')
            except ValueError:
                raise InputError(f'{path}: ISO YYYY-MM-DD date required') from None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        number(value, path, spec.get('minimum'), spec.get('maximum'))


def validate(data):
    schema = load_json(SCHEMA)
    check_schema(schema)
    walk(data, schema, schema)
    indexes = {}
    warnings = []
    for collection, records in data.items():
        if collection == 'context':
            continue
        indexes[collection] = {}
        for record in records:
            key = record['id']
            if key in indexes[collection]:
                raise InputError(f'{collection}: duplicate id {key}')
            indexes[collection][key] = record

    def link(collection, key, path):
        if key not in indexes[collection]:
            raise InputError(f'{path}: unresolved {collection} id {key}')
        return indexes[collection][key]

    def evidence(ids, path):
        if not ids:
            warnings.append(f'{path}: no evidence; conclusion must disclose the gap')
        for key in ids:
            source = link('sources', key, path)
            if source['status'] != 'current':
                warnings.append(f'{path}: source {key} is {source["status"]}')

    ctx = data['context']
    as_of = date.fromisoformat(ctx['as_of'])
    if not ctx['jurisdictions'] or not ctx['objectives']:
        raise InputError('context: jurisdiction and objective required')
    for source in data['sources']:
        if source['replaced_by']:
            link('sources', source['replaced_by'], source['id'])
        visited, node = set(), source
        while node['replaced_by']:
            if node['id'] in visited:
                raise InputError('source replacement cycle')
            visited.add(node['id'])
            node = link('sources', node['replaced_by'], source['id'])
    for node in data['taxonomy']:
        if node['level'] == 0 and node['parent_id'] is not None:
            raise InputError('taxonomy root cannot have parent')
        if node['level'] > 0:
            parent = link('taxonomy', node['parent_id'], node['id'])
            if parent['level'] != node['level'] - 1:
                raise InputError('taxonomy must progress L0/L1/L2 without cycles')
    for risk in data['risks']:
        link('taxonomy', risk['taxonomy_id'], risk['id'])
        if risk['objective'] not in ctx['objectives']:
            raise InputError(f'{risk["id"]}: unknown objective')
    for collection, records in data.items():
        if collection == 'context':
            continue
        for record in records:
            for key in ('evidence_ids', 'design_evidence_ids', 'operating_evidence_ids', 'validation_evidence_ids'):
                if key in record:
                    evidence(record[key], record['id'])
            for key in record.get('risk_ids', []):
                link('risks', key, record['id'])
    assessment_keys = set()
    for method in data['methods']:
        if len(method['impact_levels']) != 5 or len(method['likelihood_levels']) != 5:
            raise InputError('method: exactly five meaningful level definitions required')
        if method['approval'] == 'approved' and not method['approved_by']:
            raise InputError('approved method requires authority')
    for assessment in data['assessments']:
        link('risks', assessment['risk_id'], assessment['id'])
        method = link('methods', assessment['method_id'], assessment['id'])
        if assessment['horizon'] != method['horizon']:
            raise InputError('assessment and method horizon mismatch')
        if assessment['as_of'] > ctx['as_of']:
            raise InputError('assessment from future of snapshot')
        key = (assessment['risk_id'], assessment['basis'], assessment['as_of'], assessment['method_id'])
        if key in assessment_keys:
            raise InputError('ambiguous assessment at same basis/date/method')
        assessment_keys.add(key)
        if None in (assessment['impact'], assessment['likelihood']) and assessment['rating'] is not None:
            raise InputError('missing impact/likelihood cannot carry a rating')
    for metric in data['metrics']:
        validate_rules(metric)
        if metric['approval'] == 'approved' and not metric['approved_by']:
            raise InputError('approved metric requires authority')
    observation_keys = set()
    for obs in data['observations']:
        metric = link('metrics', obs['metric_id'], obs['id'])
        for dimension in ('unit', 'currency', 'horizon', 'scope'):
            if obs[dimension] != metric[dimension]:
                raise InputError(f'{obs["id"]}: metric {dimension} mismatch')
        if obs['value'] is not None:
            number(obs['value'], obs['id'])
        if obs['quality'] == 'valid' and obs['value'] is None:
            raise InputError('null value cannot be labelled valid')
        observed = date.fromisoformat(obs['as_of'])
        if observed > as_of:
            raise InputError('observation from future of snapshot')
        key = (obs['metric_id'], obs['as_of'])
        if key in observation_keys:
            raise InputError('ambiguous observations at same metric/date')
        observation_keys.add(key)
        if (as_of - observed).days > metric['max_age_days']:
            warnings.append(f'{obs["id"]}: stale at snapshot; report must evaluate UNKNOWN')
    for dep in data['dependencies']:
        for key in ('from_risk_id', 'to_risk_id'):
            link('risks', dep[key], dep['id'])
        if dep['from_risk_id'] == dep['to_risk_id']:
            raise InputError('self dependency')
    for loss in data['losses']:
        number(loss['amount'], loss['id'], minimum=0)
    for treatment in data['treatments']:
        number(treatment['cost'], treatment['id'], minimum=0)
        if treatment['status'] != 'proposed' and not treatment['acceptance_authority']:
            raise InputError('treatment execution/acceptance needs authority')
        for field in ('no_action_case', 'target'):
            if not treatment.get(field):
                warnings.append(f'{treatment["id"]}: {field} not provided; disclose treatment comparison gap')
        for key in treatment.get('target_assessment_ids', []):
            assessment = link('assessments', key, treatment['id'])
            if assessment['basis'] != 'target' or assessment['risk_id'] not in treatment['risk_ids']:
                raise InputError('treatment target assessment must have target basis and linked risk')
    for handoff in data['handoffs']:
        if handoff['result_status'] == 'validated':
            if (handoff['capability_status'] != 'verified'
                    or not (handoff['method'] or '').strip()
                    or handoff['validation_status'] not in ('PASS', 'PASS_WITH_LIMITS')
                    or not handoff.get('validation_evidence_ids')):
                raise InputError('validated handoff requires verified capability, method, passing validation and evidence')
            for key in handoff['validation_evidence_ids']:
                if link('sources', key, handoff['id'])['status'] != 'current':
                    raise InputError('validated handoff evidence must reference current sources')
    return dict(status='VALID', warnings=warnings, counts={k: len(v) for k, v in indexes.items()},
                limitation='Structural and semantic checks; not assurance of source truth or method suitability')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot')
    args = parser.parse_args()
    try:
        write_json(validate(load_json(args.snapshot)))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(2, f'error: {exc}\n')


if __name__ == '__main__':
    main()
