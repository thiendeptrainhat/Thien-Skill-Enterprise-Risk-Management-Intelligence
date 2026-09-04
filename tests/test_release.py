"""D04 gates and actual optional Office-runtime regression (no installation)."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'skill/thien-skill-enterprise-risk-management-intelligence'
sys.path.insert(0,str(SOURCE/'scripts'))
from fixture import engagement
from report import prepare
from erm_core import json_default
spec=importlib.util.spec_from_file_location('builder',ROOT/'tools/build_release.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)


class ReleaseGates(unittest.TestCase):
    def test_counts_and_lines_request_review_instead_of_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);src=root/'source';shutil.copytree(SOURCE,src)
            for i in range(10):(src/f'probe-{i}.md').write_text('Linked synthetic budget fixture.\n'*850)
            with (src/'SKILL.md').open('a') as f:
                for i in range(10):f.write(f'\n[Probe {i}](probe-{i}.md)\n')
            files,audit=builder.inspect_hygiene(src,root)
            self.assertEqual(len(files),41)
            self.assertTrue(any('41 files' in s for s in audit['reviews']))
            self.assertTrue(any('850 lines' in s for s in audit['reviews']))

    def test_html_specific_byte_budget(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);src=root/'source';shutil.copytree(SOURCE,src);p=src/'assets/dashboard.html'
            p.write_text('x'*(300*1024))
            self.assertTrue(any('dashboard.html: byte budget review' in s for s in builder.inspect_hygiene(src,root)[1]['reviews']))
            p.write_text('x'*(500*1024+1))
            with self.assertRaisesRegex(ValueError,'exceeds'):builder.inspect_hygiene(src,root)

    def test_qa_and_zip_hard_limits(self):
        for label,warning,hard in [('QA',15*builder.MIB,25*builder.MIB),('compressed ZIP',3*builder.MIB,5*builder.MIB)]:
            notes=[];builder.byte_gate(label,warning+1,warning,hard,notes);self.assertTrue(notes)
            with self.assertRaises(ValueError):builder.byte_gate(label,hard+1,warning,hard,[])
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'qa').mkdir()
            with (root/'qa/budget.bin').open('wb') as f:f.truncate(25*builder.MIB+1)
            with self.assertRaisesRegex(ValueError,'QA'):builder.inspect_hygiene(SOURCE,root)

    def test_release_state_reproducibility_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);src=root/'source';shutil.copytree(SOURCE,src);(src/'VERSION').write_text('1.0.0\n')
            a=builder.build('Release',src,root,root/'a');b=builder.build('Release',src,root,root/'b')
            self.assertEqual(a['state'],'Release')
            self.assertEqual(a['native_platform_tests'],'NOT_RUN_FOR_THIS_BUILD')
            self.assertEqual([x['sha256'] for x in a['targets'].values()],[x['sha256'] for x in b['targets'].values()])
            with self.assertRaisesRegex(ValueError,'preserve'):builder.build('Release',src,root,root/'a')
            (src/'VERSION').write_text('0.1.3\n')
            with self.assertRaisesRegex(ValueError,'0.x'):builder.build('Release',src,root,root/'c')


@unittest.skipUnless(os.environ.get('ERM_NODE') and os.environ.get('ERM_NODE_MODULES'), 'Approved Office runtime not supplied')
class OfficeRuntime(unittest.TestCase):
    def run_export_check(self,data):
        report=prepare(data)
        with tempfile.TemporaryDirectory(prefix='erm-office-test-') as tmp:
            root=Path(tmp);(root/'node_modules').symlink_to(os.environ['ERM_NODE_MODULES'],target_is_directory=True)
            shutil.copyfile(SOURCE/'scripts/export_office.mjs',root/'export.mjs')
            (root/'report.json').write_text(json.dumps(report,ensure_ascii=False,default=json_default))
            p=subprocess.run([os.environ['ERM_NODE'],str(root/'export.mjs'),str(root/'report.json'),str(root/'out'),
                str(SOURCE/'assets/logo.png'),str(root/'preview'),'--check'],capture_output=True,text=True,timeout=60)
            files=list((root/'out').glob('*'))
            self.assertEqual(files,[],'Check-only and rejected inputs must not write Office artifacts')
            return p

    def test_numeric_strings_match_engine(self):
        data=engagement()
        for obs in data['observations']:
            if obs['value'] is not None:obs['value']=str(obs['value'])
        for m in data['metrics']:
            for r in m['rules']:r['threshold']=str(r['threshold'])
        p=self.run_export_check(data);self.assertEqual(p.returncode,0,p.stderr)
        self.assertEqual(json.loads(p.stdout)['checks']['statuses'],[['breach'],['capacity_breach'],['UNKNOWN']])

    def test_decimal_exponents_and_negative_values(self):
        data=engagement();data['observations'][2]['value']='2.000e2';data['observations'][5]['value']='-2.5e3'
        data['metrics'][0]['rules'][1]['threshold']='200.000'
        p=self.run_export_check(data);self.assertEqual(p.returncode,0,p.stderr)

    def test_unsafe_string_and_number_precision_is_explicit(self):
        for value in ['0.1234567890123456',9007199254740992,'1e-400']:
            with self.subTest(value=value):
                data=engagement();data['observations'][2]['value']=value
                p=self.run_export_check(data);self.assertNotEqual(p.returncode,0)
                self.assertIn('Excel precision limit',p.stderr)

    def test_identifiers_remain_text(self):
        data=engagement();data['risks'][0]['owner']='00123'
        p=self.run_export_check(data);self.assertEqual(p.returncode,0,p.stderr)

    def test_word_preset_and_content_parity(self):
        import xml.etree.ElementTree as ET
        with tempfile.TemporaryDirectory(prefix='erm-word-test-') as tmp:
            root=Path(tmp)
            supplied=os.environ.get('ERM_DOCX_SAMPLE')
            if supplied:
                docx_path=Path(supplied)
            else:
                (root/'node_modules').symlink_to(os.environ['ERM_NODE_MODULES'],target_is_directory=True)
                shutil.copyfile(SOURCE/'scripts/export_office.mjs',root/'export.mjs')
                (root/'report.json').write_text(json.dumps(prepare(engagement()),ensure_ascii=False,default=json_default))
                run=subprocess.run([os.environ['ERM_NODE'],str(root/'export.mjs'),str(root/'report.json'),str(root/'out'),
                    str(SOURCE/'assets/logo.png'),str(root/'preview')],capture_output=True,text=True,timeout=180)
                self.assertEqual(run.returncode,0,run.stderr)
                docx_path=root/'out/report.docx'
            ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            W='{'+ns['w']+'}'
            with zipfile.ZipFile(docx_path) as z:
                styles=ET.fromstring(z.read('word/styles.xml'))
                doc=ET.fromstring(z.read('word/document.xml'))
            expected={'Normal':(0,120),'Heading1':(320,160),'Heading2':(240,120)}
            for name,(before,after) in expected.items():
                matches=styles.findall(f"w:style[@w:styleId='{name}']",ns)
                self.assertEqual(len(matches),1,'Duplicate or missing style ID: '+name)
                style=matches[0]
                self.assertIsNotNone(style,name)
                spacing=style.find('w:pPr/w:spacing',ns)
                self.assertEqual(spacing.get(W+'before'),str(before))
                self.assertEqual(spacing.get(W+'after'),str(after))
                for para in doc.findall('.//w:p',ns):
                    applied=para.find('w:pPr/w:pStyle',ns)
                    if applied is not None and applied.get(W+'val')==name:
                        self.assertIsNone(para.find('w:pPr/w:spacing',ns),'Direct spacing overrides preset')
            normal=styles.find("w:style[@w:styleId='Normal']",ns)
            self.assertIn(normal.get(W+'default'),('1','true'))
            self.assertEqual(normal.find('w:rPr/w:rFonts',ns).get(W+'ascii'),'Calibri')
            self.assertEqual(normal.find('w:rPr/w:sz',ns).get(W+'val'),'22')
            self.assertEqual(normal.find('w:pPr/w:spacing',ns).get(W+'line'),'264')
            text=' '.join(doc.itertext())
            fixture=engagement()
            for risk in fixture['risks']:
                self.assertIn(risk['id'],text)
            for treatment in fixture['treatments']:
                self.assertIn(treatment['no_action_case'],text)
                self.assertIn(treatment['target'],text)
            for warning in prepare(fixture)['validation']['warnings']:
                self.assertIn(warning,text)
