#!/usr/bin/env python3
"""D04 hygiene reviews, hard byte budgets, and reproducible three-target builds."""
import argparse
import hashlib
import json
import re
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'thien-skill-enterprise-risk-management-intelligence'
SOURCE = ROOT / 'skill' / SLUG
VERSION = (SOURCE / 'VERSION').read_text().strip()
DIST = ROOT / 'dist' / VERSION
TARGETS = ('claude', 'chatgpt', 'universal')
TEXT = {'.md', '.py', '.mjs', '.json', '.html', '.yaml', '.txt', ''}
ALLOWED = TEXT | {'.png'}
MIB = 1024 * 1024
ABS = re.compile(r'/Users/|/private/tmp|[A-Za-z]:\\\\')
LINK = re.compile(r'\[[^]]*\]\((?!https?://|mailto:|#)([^)#]+)(?:#[^)]+)?\)')


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def fail(message):
    raise ValueError('HYGIENE FAIL: ' + message)


def byte_gate(label, size, warning, maximum, reviews):
    if size > maximum:
        fail(f'{label}: {size} bytes exceeds {maximum}')
    if size > warning:
        reviews.append(f'{label}: byte budget review ({size} > {warning})')


def count_review(label, count, first, second, reviews):
    if count > first:
        reviews.append(f'{label}: {count} files; {"elevated " if count > second else ""}consumer/duplication review required, not a hard cap')


def inspect_hygiene(source=None, root=None):
    source, root = Path(source or SOURCE), Path(root or ROOT)
    files = sorted(p for p in source.rglob('*') if p.is_file())
    reviews = []
    if not (source / 'SKILL.md').is_file() or (source / '.agents').exists():
        fail('entrypoint/universal layout')
    count_review('canonical', len(files), 32, 40, reviews)
    total = sum(p.stat().st_size for p in files)
    byte_gate('canonical', total, 3*MIB, 5*MIB, reviews)
    for p in files:
        rel = p.relative_to(source)
        if p.suffix not in ALLOWED or p.is_symlink():
            fail(f'unsupported/symlink {rel}')
        if any(x in {'__pycache__', '.DS_Store', '.pytest_cache', 'node_modules'} or x.endswith('~') for x in rel.parts):
            fail(f'temp/cache {rel}')
        size = p.stat().st_size
        if p.suffix in TEXT:
            limit = (250*1024, 500*1024) if p.suffix == '.html' else (100*1024, 200*1024)
            byte_gate(str(rel), size, *limit, reviews)
            text = p.read_text(encoding='utf-8')
            if ABS.search(text):
                fail(f'machine path {rel}')
            if re.search(r'(?i)\b(TODO|FIXME|lorem ipsum|your .* here)\b', text):
                fail(f'scaffold placeholder {rel}')
            lines = len(text.splitlines())
            thresholds = (200, 300) if p.name == 'SKILL.md' else (500, 800) if p.suffix in {'.py', '.mjs', '.json', '.html'} else (300, 450) if rel.parts[0] in {'references', 'industry-packs', 'integration'} else (150, 250)
            if p.name == 'LICENSE':
                reviews.append(f'LICENSE: {lines} lines; retained unchanged legal template')
            elif lines > thresholds[0]:
                reviews.append(f'{rel}: {lines} lines; review thresholds {thresholds}, not a hard cap')
            for link in LINK.findall(text) if p.suffix == '.md' else []:
                target = (p.parent / link.replace('%20', ' ')).resolve()
                try:
                    target.relative_to(source.resolve())
                except ValueError:
                    fail(f'link escapes package {rel}: {link}')
                if not target.exists():
                    fail(f'broken link {rel}: {link}')
        else:
            byte_gate(str(rel), size, int(1.5*MIB), 2*MIB, reviews)
    for p in source.rglob('*'):
        if p.is_symlink():
            fail(f'symlink {p.relative_to(source)}')
        if p.is_dir() and not any(p.iterdir()):
            fail(f'empty directory {p.relative_to(source)}')
    qa = [p for p in (root/'qa').rglob('*') if p.is_file()]
    qa_bytes = sum(p.stat().st_size for p in qa)
    byte_gate('QA', qa_bytes, 15*MIB, 25*MIB, reviews)
    count_review('QA', len(qa), 15, 20, reviews)
    project_files = files + [p for folder in ('docs', 'tests', 'tools') for p in (root/folder).rglob('*') if p.is_file()]
    project_files += [p for p in root.glob('*') if p.is_file()]
    count_review('project source', len(project_files), 48, 60, reviews)
    for p in (root/'docs').glob('*.md'):
        lines = len(p.read_text().splitlines())
        if lines > 600:
            reviews.append(f'{p.name}: {lines} lines; governance review thresholds 600/800, not a hard cap')
    return files, dict(canonical_files=len(files), canonical_bytes=total, qa_files=len(qa), qa_bytes=qa_bytes,
                      project_source_files=len(project_files), reviews=reviews)


def hygiene():
    return inspect_hygiene()[0]


def build(state='Testing', source=None, root=None, dist=None):
    source, root = Path(source or SOURCE), Path(root or ROOT)
    version = (source/'VERSION').read_text().strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+', version) or state not in ('Testing', 'Release'):
        fail('invalid version/state')
    if state == 'Release' and int(version.split('.')[0]) < 1:
        fail('0.x is Testing; Release requires an explicitly completed version')
    destination = Path(dist or DIST)
    if destination.exists():
        fail('release exists; preserve delivered artifacts')
    files, audit = inspect_hygiene(source, root)
    release = dict(version=version, slug=SLUG, state=state, targets={},
                   native_platform_tests='NOT_RUN_FOR_THIS_BUILD', hygiene=audit)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Validate every staged target before making a version directory visible.
    with tempfile.TemporaryDirectory(prefix='.erm-build-', dir=destination.parent) as tmp:
        staged = Path(tmp)/'payload'
        staged.mkdir()
        for target in TARGETS:
            manifest = dict(name=SLUG, display_name="Thiện's Skill — Enterprise Risk Management Intelligence",
                            version=version, state=state, target=target,
                            layout=f'{SLUG}/ at ZIP root; no .agents/skills layer',
                            files={str(p.relative_to(source)):dict(sha256=digest(p), bytes=p.stat().st_size) for p in files})
            payload = {str(PurePosixPath(SLUG)/p.relative_to(source)):p.read_bytes() for p in files}
            payload[f'{SLUG}/PACKAGE-MANIFEST.json'] = json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2).encode()+b'\n'
            count_review('ZIP entries', len(payload), 34, 42, audit['reviews'])
            byte_gate('unpacked payload', sum(map(len, payload.values())), 3*MIB, 5*MIB, audit['reviews'])
            zpath = staged/f'{SLUG}-{version}-{target}.zip'
            with zipfile.ZipFile(zpath, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
                for name, data in payload.items():
                    info = zipfile.ZipInfo(name, (2026, 9, 4, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    z.writestr(info, data, compresslevel=9)
            byte_gate('compressed ZIP', zpath.stat().st_size, 3*MIB, 5*MIB, audit['reviews'])
            with zipfile.ZipFile(zpath) as z:
                if z.testzip() or set(z.namelist()) != set(payload) or len(z.namelist()) != len(payload):
                    fail('ZIP integrity/paths')
                for name, data in payload.items():
                    if z.read(name) != data:
                        fail('source/package mismatch')
            release['targets'][target] = dict(file=zpath.name, sha256=digest(zpath), bytes=zpath.stat().st_size, entries=len(payload))
        (staged/'RELEASE-MANIFEST.json').write_text(json.dumps(release, ensure_ascii=False, indent=2)+'\n')
        (staged/'SHA256SUMS').write_text(''.join(f"{v['sha256']}  {v['file']}\n" for v in release['targets'].values()))
        if destination.exists():
            fail('destination created concurrently; will not replace it')
        staged.rename(destination)
    return release


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--build', action='store_true')
    parser.add_argument('--state', choices=['Testing', 'Release'], default='Testing', help='Explicit release lifecycle; never infers native test success')
    args = parser.parse_args()
    try:
        result = inspect_hygiene()[1] if args.check else build(args.state)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(2, str(exc)+'\n')
