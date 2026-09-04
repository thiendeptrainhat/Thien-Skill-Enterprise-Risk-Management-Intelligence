"""Regression and adverse-input tests with independent numeric expectations."""
import copy
import hashlib
import json
import sys
import tempfile
import subprocess
from unittest.mock import patch
import unittest
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'skill/thien-skill-enterprise-risk-management-intelligence/scripts'))
from erm_core import *
from validate_engagement import validate
from report import prepare, render_html
from fixture import engagement


class Arithmetic(unittest.TestCase):
    def test_margin(self):
        self.assertEqual(margin(100,1000,60,10000),dict(revenue=D(100000),contribution=D(40000),profit=D(30000),margin=D('.3')))
        self.assertIsNone(margin(10,0,5,100)['margin'])

    def test_passthrough(self):
        result=pass_through(100,1000,60,10000,10,'.5','-.1')
        self.assertEqual(result['scenario']['profit'],D(21500))
        self.assertEqual(result['profit_change'],D(-8500))

    def test_profit_bridge_reconciles_components(self):
        cases = [
            ((100,1000,60,10000,10,'.5','-.1'), [4500,-9000,-4000]),
            (('75','80','30','1000','-4','.25','.2'), [-96,384,720]),
            ((10,0,12,3,2,1,0), [0,0,0]),
            ((10,50,12,3,2,0,-1), [0,0,100]),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                r=pass_through(*args); b=r['profit_bridge']
                self.assertEqual([t['amount'] for t in b['components']],list(map(D,expected)))
                for term in b['components']:
                    self.assertEqual(term['amount'],term['factors'][0]*term['factors'][1])
                self.assertEqual(b['total'],r['scenario']['profit']-r['baseline']['profit'])
                self.assertEqual(b['reconciliation_difference'],0)

    def test_calculation_context_must_be_object(self):
        with self.assertRaises(InputError):
            calculate(dict(operation='margin',parameters={},context='triệu VND'))

    def test_working_capital(self):
        result=working_capital(36500,18250,30,60,45,365)
        self.assertEqual(result,dict(ar=D(3000),inventory=D(3000),ap=D(2250),nwc=D(3750)))

    def test_cash_shortfall(self):
        r=cash_waterfall(20,[8],[30],5)
        self.assertEqual((r['closing_cash'],r['runway_periods'],r['liquidity_shortfall']),(D(-2),D(0),D(2)))
        self.assertIsNone(cash_waterfall(10,[],[],0)['runway_periods'])

    def test_credit(self):
        self.assertEqual(credit(100,20,'.1','.5')['expected_loss'],D(4))
        self.assertEqual(credit(100,200,1,1)['net_exposure'],0)

    def test_concentration(self):
        self.assertEqual(concentration([60,30,10])['hhi'],D('.46'))
        self.assertIsNone(concentration([0,0])['hhi'])

    def test_disruption(self):
        self.assertEqual(disruption(1000,800,40,2000,1000)['incremental_loss'],11000)

    def test_quality(self):
        self.assertEqual(quality(1000,'.1',5,100,50,2000)['incremental_loss'],7500)

    def test_inventory(self):
        # Usable80; demand100 gives20 lost margin +20 writeoff +10 markdown.
        r=inventory(100,100,5,20,3,10,1)
        self.assertEqual((r['shortfall_units'],r['incremental_loss']),(20,170))

    def test_project(self):
        self.assertEqual(project_eac(100,70,50,90,110),dict(eac=D(120),cost_variance=D(-20),delay_days=D(20)))

    def test_headroom(self):
        self.assertEqual(headroom(110,100,'higher')['headroom'],-10)
        self.assertEqual(headroom(-2,0,'lower')['headroom'],-2)
        self.assertIsNone(headroom(-2,0,'lower')['utilization'])

    def test_treatment(self):
        r=treatment(100,[40]*3,'.1',80,3,2)
        self.assertAlmostEqual(float(r['npv']),-.525920360631,places=10)
        self.assertFalse(r['budget_feasible']);self.assertFalse(r['resources_feasible'])

    def test_simulation(self):
        a=simulate_margin([100,100,100],[60,60,60],[1000,1000,1000],10000,7,100)
        self.assertEqual((a['p05'],a['p50'],a['p95']), (30000,30000,30000))
        args=([90,100,110],[50,60,70],[900,1000,1100],10000,123,1000)
        a,b=simulate_margin(*args),simulate_margin(*args)
        self.assertEqual(a,b);self.assertLess(a['p05'],a['p95'])

    def test_invalid_numbers(self):
        for value in [None,True,'NaN','Infinity',float('nan'),'1e31']:
            with self.subTest(value=value),self.assertRaises(InputError):number(value)
        for call in [lambda:credit(1,0,1.01,.5),lambda:concentration([-1]),lambda:inventory(10,10,1,8,1,3,1),
                     lambda:working_capital(1,1,1,1,1,0),lambda:simulate_margin([3,2,1],[1,2,3],[1,2,3],0,1,10)]:
            with self.assertRaises(InputError):call()

    def test_loss_id_dedup_and_currency(self):
        losses=[dict(id='L1',amount=10,currency='VND',horizon='Q4',scope='G'),dict(id='L1',amount=10,currency='VND',horizon='Q4',scope='G')]
        self.assertEqual(aggregate_losses(losses,'VND','Q4','G')['total'],10)
        losses[1]['amount']=12
        with self.assertRaises(InputError):aggregate_losses(losses,'VND','Q4','G')
        losses[1].update(id='L2',amount=10,currency='USD')
        with self.assertRaises(InputError):aggregate_losses(losses,'VND','Q4','G')


class CheckedResults(unittest.TestCase):
    def request(self, operator='-', left=80, right=20):
        return dict(operation='arithmetic', parameters=dict(left=left, operator=operator, right=right),
                    context=dict(unit='tỷ VND', currency='VND', horizon='Q4/2026', source_refs=['SYN1']))

    def test_arithmetic_business_cases_and_invalid_inputs(self):
        for operator,left,right,expected in [('-',80,20,60),('*',120,'.4',48),('+','-5','2.5','-2.5'),('/',20,80,'.25')]:
            with self.subTest(operator=operator):
                r=checked_calculation(self.request(operator,left,right))
                self.assertEqual(r['calculation']['outputs']['result'],D(str(expected)))
        for args in [('?',1,1),('/',1,0),('+',True,2),('*','NaN',2)]:
            with self.subTest(args=args),self.assertRaises(InputError):
                checked_calculation(self.request(*args))

    def test_matching_result_is_reexecuted_not_trusted(self):
        request=self.request();prior=calculate(request)
        with patch('erm_core.calculate',wraps=calculate) as run:
            result=checked_calculation(request,prior)
            run.assert_called_once()
        self.assertEqual(result['verification']['comparison'],'MATCH')
        self.assertEqual(result['verification']['status'],'EXECUTED')
        self.assertIn('(80) - (20) = 60',result['text'])
        self.assertEqual(result['verification']['input_sha256'],hashlib.sha256(canonical_json(request).encode()).hexdigest())
        self.assertEqual(result['verification']['calculation_sha256'],hashlib.sha256(canonical_json(prior).encode()).hexdigest())

    def test_missing_forged_or_mismatched_comparison_rejected(self):
        request=self.request();prior=calculate(request)
        invalid=[None,{},dict(status='PASS'),dict(calculation=prior,verification=dict(status='EXECUTED'))]
        for key,value in [('unit','VND'),('currency','USD'),('horizon','FY2025'),('source_refs',['SYN2'])]:
            bad=copy.deepcopy(prior);bad['context'][key]=value;invalid.append(bad)
        for key,value in [('left',81),('right',21)]:
            bad=copy.deepcopy(prior);bad['parameters'][key]=value;invalid.append(bad)
        bad=copy.deepcopy(prior);bad['outputs']['result']=D(61);invalid.append(bad)
        for record in invalid:
            with self.subTest(record=record),self.assertRaises(InputError):checked_calculation(request,record)
        with patch('erm_core.calculate',side_effect=InputError('runtime calculation failed')):
            with self.assertRaisesRegex(InputError,'runtime calculation failed'):checked_calculation(request,prior)

    def test_bridge_factors_and_total_checked_before_text(self):
        request=dict(operation='pass_through',parameters=dict(price=100,volume=1000,unit_cost=60,
            fixed_cost=10000,cost_change=10,pass_through_rate='.5',volume_change='-.1'),context=self.request()['context'])
        result=checked_calculation(request)
        bridge=result['calculation']['outputs']['profit_bridge']
        self.assertEqual([t['amount'] for t in bridge['components']],[D(4500),D(-9000),D(-4000)])
        self.assertEqual(bridge['total'],D(-8500))
        for field in ['factor','amount','total','delta']:
            bad=calculate(request)
            if field=='factor':bad['outputs']['profit_bridge']['components'][0]['factors'][0]=D(6)
            elif field=='amount':bad['outputs']['profit_bridge']['components'][0]['amount']=D(4501)
            elif field=='total':bad['outputs']['profit_bridge']['total']=D(-8499)
            else:bad['outputs']['scenario']['profit']=D(21501)
            with self.subTest(field=field),patch('erm_core.calculate',return_value=bad):
                with self.assertRaisesRegex(InputError,'bridge does not reconcile'):checked_calculation(request)

    def test_context_and_status_cannot_be_self_attested(self):
        for field,value in [('unit',None),('currency',1),('horizon',' '),('source_refs','SYN1'),('source_refs',[])]:
            request=self.request();request['context'][field]=value
            with self.subTest(field=field,value=value),self.assertRaises(InputError):checked_calculation(request)
        request=self.request();request['verification']={'status':'PASS'}
        with self.assertRaises(InputError):checked_calculation(request)
        original=self.request();result=checked_calculation(original)
        original['context']['horizon']='CHANGED';original['parameters']['left']=99
        self.assertEqual(result['calculation']['context']['horizon'],'Q4/2026')
        self.assertEqual(result['calculation']['parameters']['left'],80)

    def test_cli_checked_json_text_and_legacy_compatibility(self):
        engine=ROOT/'skill/thien-skill-enterprise-risk-management-intelligence/scripts/erm_core.py'
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);request=root/'input.json';request.write_text(json.dumps(self.request()))
            def run(*args):return subprocess.run([sys.executable,str(engine),'--input',str(request),*args],capture_output=True,text=True)
            legacy=run();self.assertEqual(legacy.returncode,0,legacy.stderr)
            self.assertEqual(set(json.loads(legacy.stdout)),{'operation','parameters','context','formula_reference','outputs'})
            comparison=root/'prior.json';comparison.write_text(legacy.stdout)
            checked=run('--checked','--compare',str(comparison));self.assertEqual(checked.returncode,0,checked.stderr)
            packet=json.loads(checked.stdout);self.assertEqual(packet['calculation']['outputs']['result'],'60')
            text=run('--checked','--compare',str(comparison),'--text')
            self.assertEqual(text.returncode,0,text.stderr);self.assertEqual(text.stdout,packet['text'])
            output=root/'answer.txt';output.write_text('preserve existing')
            duplicate=run('--checked','--text','--output',str(output))
            self.assertEqual(duplicate.returncode,2);self.assertEqual(output.read_text(),'preserve existing')

    def test_cli_failure_never_emits_checked_artifact(self):
        engine=ROOT/'skill/thien-skill-enterprise-risk-management-intelligence/scripts/erm_core.py'
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);request=root/'input.json';request.write_text(json.dumps(self.request()))
            comparison=root/'prior.json';output=root/'out.json'
            for content in ['null','{"status":"PASS"}', '{broken']:
                comparison.write_text(content)
                run=subprocess.run([sys.executable,str(engine),'--input',str(request),'--checked',
                    '--compare',str(comparison),'--output',str(output)],capture_output=True,text=True)
                self.assertEqual(run.returncode,2,run.stdout);self.assertEqual(run.stdout,'')
                self.assertIn('UNCHECKED:',run.stderr);self.assertFalse(output.exists())
            comparison.unlink()
            run=subprocess.run([sys.executable,str(engine),'--input',str(request),'--checked',
                '--compare',str(comparison)],capture_output=True,text=True)
            self.assertEqual(run.returncode,2);self.assertEqual(run.stdout,'')


class Semantics(unittest.TestCase):
    def test_boundary_and_precedence(self):
        m=engagement()['metrics'][0]
        self.assertEqual(evaluate_metric(200,m)['status'],'breach')
        self.assertEqual(evaluate_metric(300,m)['status'],'capacity_breach')
        self.assertEqual(evaluate_metric(None,m)['status'],'UNKNOWN')
        self.assertEqual(evaluate_metric(0,m,'stale')['status'],'UNKNOWN')
        m['approval']='draft';self.assertEqual(evaluate_metric(300,m)['status'],'DRAFT')
        r=portfolio_status([{'status':'capacity_breach'},{'status':'UNKNOWN'}])
        self.assertTrue(r['incomplete']);self.assertEqual(r['known_status'],'capacity_breach')

    def test_direction(self):
        m=engagement()['metrics'][1]
        self.assertEqual(evaluate_metric(-2000,m)['status'],'capacity_breach')
        self.assertEqual(evaluate_metric(6000,m)['status'],'within')
        m['rules'][0]['op']='>'
        with self.assertRaises(InputError):evaluate_metric(1,m)

    def test_capacity_order(self):
        m=engagement()['metrics'][0];m['rules'][1]['threshold']=400
        with self.assertRaises(InputError):validate_rules(m)

    def test_two_sided(self):
        m=dict(bad_direction='two_sided',approval='approved',rules=[dict(op='<',threshold=5,severity='breach'),dict(op='>=',threshold=10,severity='breach')])
        self.assertEqual(evaluate_metric(5,m)['status'],'within')
        self.assertEqual(evaluate_metric(10,m)['status'],'breach')

    def test_valid_snapshot(self):
        self.assertEqual(validate(engagement())['status'],'VALID')

    def test_bad_snapshots(self):
        mutations=[lambda d:d['risks'][0].update(taxonomy_id='missing'),
            lambda d:d['observations'][0].update(currency='USD'),lambda d:d['observations'][0].update(value=None),
            lambda d:d['methods'][0].update(approved_by=None),lambda d:d['assessments'][0].update(horizon='year'),
            lambda d:d['assessments'][2].update(rating='Low'),lambda d:d['sources'][0].update(replaced_by='SYN1'),
            lambda d:d['losses'].append(copy.deepcopy(d['losses'][0])),lambda d:d['metrics'][0].update(typo=1),
            lambda d:d['observations'][0].update(as_of='2027-01-01'),lambda d:d['handoffs'][0].update(result_status='validated')]
        for i,mutate in enumerate(mutations):
            with self.subTest(i=i):
                data=engagement();mutate(data)
                with self.assertRaises(InputError):validate(data)

    def test_source_replacement_warning(self):
        data=engagement();source=copy.deepcopy(data['sources'][0]);source['id']='SYN2'
        data['sources'][0].update(status='superseded',replaced_by='SYN2');data['sources'].append(source)
        self.assertTrue(any('superseded' in x for x in validate(data)['warnings']))

    def test_snapshot_report(self):
        r=prepare(engagement())
        self.assertEqual(r['summary']['confirmed_breaches'],2)
        self.assertEqual(r['summary']['unresolved_metrics'],1)
        self.assertEqual(r['loss_totals'][0]['total'],13000)
        self.assertEqual(r['summary']['known_status'],'capacity_breach')

    def test_stale_latest_is_not_green(self):
        data=engagement();data['metrics'][0]['max_age_days']=0
        data['observations']=[o for o in data['observations'] if o['id']!='O13']
        self.assertEqual(prepare(data)['metrics'][0]['status'],'UNKNOWN')

    def test_method_change_not_overwritten(self):
        data=engagement();m=copy.deepcopy(data['methods'][0]);m['id']='M2';data['methods'].append(m)
        a=copy.deepcopy(data['assessments'][0]);a.update(id='A4',method_id='M2',rating='Low');data['assessments'].append(a)
        self.assertEqual(len(prepare(data)['risks'][0]['assessments']),2)

    def test_injection_escaped(self):
        data=engagement();data['context']['decision']='</script><script>alert(1)</script>'
        html=render_html(prepare(data))
        self.assertNotIn(data['context']['decision'],html)
        self.assertIn('\\u003c/script\\u003e',html)

    def test_duplicate_json_key_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'test.json';p.write_text('{"x":1,"x":2}')
            with self.assertRaises(InputError):load_json(p)
            with self.assertRaises(FileExistsError):write_json({},p)


class Remediation(unittest.TestCase):
    def test_handoff_rejects_failed_or_missing_evidence(self):
        for status, evidence in [('FAIL',['SYN1']),('NOT_RUN',['SYN1']),('PASS',[]),(None,['SYN1'])]:
            with self.subTest(status=status,evidence=evidence):
                data=engagement();data['handoffs'][0].update(capability_status='verified',method='synthetic-test',
                    result_status='validated',validation_status=status,validation_evidence_ids=evidence)
                with self.assertRaises(InputError):validate(data)

    def test_handoff_acceptance_roundtrip(self):
        for status in ['PASS','PASS_WITH_LIMITS']:
            data=engagement();data['handoffs'][0].update(capability_status='verified',method='synthetic-test',
                result_status='validated',validation_status=status,validation_evidence_ids=['SYN1'])
            result=prepare(data)
            self.assertEqual(result['snapshot']['handoffs'][0]['validation_status'],status)
            self.assertEqual(result['snapshot']['handoffs'][0]['validation_evidence_ids'],['SYN1'])
            data['sources'][0]['status']='unverified'
            with self.assertRaises(InputError):validate(data)

    def test_handoff_failure_can_be_recorded_without_acceptance(self):
        data=engagement();data['handoffs'][0].update(result_status='rejected',validation_status='FAIL')
        self.assertEqual(validate(data)['status'],'VALID')

    def test_treatment_target_roundtrip_and_reference(self):
        data=engagement();a=copy.deepcopy(data['assessments'][0]);a.update(id='AT1',basis='target')
        data['assessments'].append(a);data['treatments'][0]['target_assessment_ids']=['AT1']
        report=prepare(data)
        self.assertEqual(report['snapshot']['treatments'][0],data['treatments'][0])
        self.assertIn('no_action_case',report['snapshot']['treatments'][0])
        data['treatments'][0]['target_assessment_ids']=['A1']
        with self.assertRaises(InputError):validate(data)
        data['treatments'][0]['target_assessment_ids']=['missing']
        with self.assertRaises(InputError):validate(data)

    def test_treatment_missing_comparison_is_not_silent(self):
        data=engagement();data['treatments'][0].pop('target');data['treatments'][0].pop('no_action_case')
        warnings=prepare(data)['validation']['warnings']
        self.assertTrue(any('target not provided' in w for w in warnings))
        self.assertTrue(any('no_action_case not provided' in w for w in warnings))

    def test_utilization_upper_floor_signed_and_opt_out(self):
        data=engagement();report=prepare(data)
        self.assertEqual(report['metrics'][0]['headroom'][0]['utilization'],1)
        self.assertIsNone(report['metrics'][1]['headroom'][0]['utilization'])
        data['metrics'][0]['utilization_applicable']=False
        self.assertIsNone(prepare(data)['metrics'][0]['headroom'][0]['utilization'])
        data['metrics'][0]['utilization_applicable']=True
        data['observations'][2]['value']=-10
        self.assertIsNone(prepare(data)['metrics'][0]['headroom'][0]['utilization'])
        self.assertIsNone(headroom(10,0,'higher')['utilization'])

    def test_utilization_two_sided(self):
        data=engagement();data['metrics'][0].update(bad_direction='two_sided',rules=[
            dict(op='<',threshold=50,severity='breach'),dict(op='>',threshold=150,severity='breach')])
        report=prepare(data)
        self.assertEqual(len(report['metrics'][0]['headroom']),2)
        self.assertTrue(all(x['utilization'] is None for x in report['metrics'][0]['headroom']))


if __name__=='__main__':unittest.main(verbosity=2)
