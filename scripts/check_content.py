#!/usr/bin/env python3
"""Offline content checks: pairing, code parity, relative links, data hygiene.

Not a substitute for editorial review, runtime QA or a dedicated secret scanner.
"""
from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
ERRORS = []
LANGS = ('en', 'es')
LINK = re.compile(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')
FENCES = re.compile(r'^```([^\n]*)\n(.*?)^```', re.M | re.S)


def code_blocks(text):
    # Diagrams/text templates translate labels; executable samples stay identical.
    return [(lang, body) for lang, body in FENCES.findall(text) if lang not in ('mermaid', 'text')]


def check_document(path):
    text = path.read_text(encoding='utf-8')
    if len(FENCES.findall(text)) * 2 != len(re.findall(r'^```', text, re.M)):
        ERRORS.append(f'{path.relative_to(ROOT)}: unbalanced code fence')
    for target in LINK.findall(text):
        if target.startswith(('https:', 'http:', 'mailto:', '#')):
            continue
        target = target.split('#')[0]
        if target and not (path.parent / target).exists():
            ERRORS.append(f'{path.relative_to(ROOT)}: missing relative target {target}')


def main():
    files = {lang: {p.relative_to(DOCS / lang) for p in (DOCS / lang).rglob('*') if p.is_file()} for lang in LANGS}
    if files['en'] != files['es']:
        ERRORS.append(f'Language file mismatch: {files["en"] ^ files["es"]}')
    pages = sorted(p for p in files['en'] if p.suffix == '.md')
    if len(pages) != 10:
        ERRORS.append(f'Expected 10 chapters per language, found {len(pages)}')
    for page in pages:
        pair = [(DOCS / lang / page).read_text(encoding='utf-8') for lang in LANGS]
        if code_blocks(pair[0]) != code_blocks(pair[1]):
            ERRORS.append(f'{page}: executable example differs by language')
        if len(re.findall(r'^## ', pair[0], re.M)) != len(re.findall(r'^## ', pair[1], re.M)):
            ERRORS.append(f'{page}: section count differs by language')
        for lang in LANGS:
            check_document(DOCS / lang / page)
    check_document(ROOT / 'README.md')
    for svg in DOCS.rglob('*.svg'):
        element = ET.parse(svg).getroot()
        if element.get('role') != 'img' or not element.get('aria-labelledby'):
            ERRORS.append(f'{svg.relative_to(ROOT)}: missing accessible image metadata')
    # AMA policy (owner decision): no savings figures in the manual until a representative measurement exists.
    numeric_claim = re.compile(r'(?:[−-]\s?\d+(?:[.,]\d+)?\s?%|\b\d{1,3}(?:[.,]\d{3})+\s*(?:tokens|input)|\bUSD\s?0[.,]\d+|\$\s?0[.,]\d+)', re.I)
    for lang in LANGS:
        for page in ('ama.md', 'sources.md', 'index.md', 'architecture.md'):
            if numeric_claim.search((DOCS / lang / page).read_text(encoding='utf-8')):
                ERRORS.append(f'{lang}/{page}: savings figure found; AMA publishes no percentages yet')
    # Encode deployment-specific disallowed terms without publishing them verbatim.
    forbidden = [r'\b(?:\d{1,3}\.){3}\d{1,3}\b', r'/home/' + 'otixe', r'\botixe\.' + 'cl\b', r'\b\d{12}\b', r'\b' + '\x66\x6f\x6e\x61\x73\x61' + r'\b', r'\bSOUL\.md\b']
    privacy = re.compile('|'.join(forbidden), re.I)
    for path in ROOT.rglob('*'):
        if not path.is_file() or any(x in ('.venv', 'site', '.git', '__pycache__') for x in path.relative_to(ROOT).parts) or path == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        if privacy.search(text):
            ERRORS.append(f'{path.relative_to(ROOT)}: forbidden private-data pattern')
    if ERRORS:
        print('\n'.join(ERRORS), file=sys.stderr)
        return 1
    print(f'PASS: {len(pages)} paired chapters, matching executable examples, local Markdown targets and accessible SVGs.')
    print('PASS: no AMA savings figures; private-data pattern scan clean.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
