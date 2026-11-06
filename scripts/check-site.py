#!/usr/bin/env python3
"""Dependency-free structural, local-link and accessibility smoke checks."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['index.html', 'privacy.html', 'terms.html']
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())

class Page(HTMLParser):
    def __init__(self, name):
        super().__init__(convert_charrefs=True)
        self.name, self.ids, self.refs, self.stack, self.tags = name, [], [], [], Counter()
        self.external = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags[tag] += 1
        if tag == 'html': assert attrs.get('lang') == 'en', self.name
        if tag == 'img': assert attrs.get('alt'), f'{self.name}: missing image alt'
        if tag == 'video':
            assert 'controls' in attrs and 'autoplay' not in attrs, self.name
            assert attrs.get('aria-label'), self.name
        if tag == 'nav': assert attrs.get('aria-label'), f'{self.name}: unnamed nav'
        if tag == 'a': assert attrs.get('href'), f'{self.name}: empty href'
        if 'id' in attrs: self.ids.append(attrs['id'])
        for key in ['aria-labelledby', 'aria-describedby']:
            self.refs.extend('#' + i for i in attrs.get(key, '').split())
        for key in ['href', 'src', 'poster']:
            if key in attrs:
                link = attrs[key]
                scheme = urlsplit(link).scheme
                if scheme in ['https', 'http']: self.external.add(link)
                elif scheme != 'mailto':
                    assert not link.startswith('/'), f'{self.name}: root-relative URL {link}'
                    self.refs.append(link)
        if tag not in VOID: self.stack.append(tag)
    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f'{self.name}: unbalanced </{tag}>, {self.stack}'
        self.stack.pop()

pages = {}
for name in PAGES:
    page = Page(name)
    page.feed((ROOT / name).read_text())
    assert not page.stack, f'{name}: unclosed tags {page.stack}'
    assert len(set(page.ids)) == len(page.ids), f'{name}: duplicate IDs'
    assert page.tags['h1'] == page.tags['main'] == 1, f'{name}: h1/main count'
    assert 'main' in page.ids, f'{name}: skip target'
    pages[name] = page

count = 0
for name, page in pages.items():
    for ref in page.refs:
        link = urlsplit(ref)
        target = (ROOT / unquote(link.path or name)).resolve()
        if target.is_dir(): target /= 'index.html'
        assert target.is_relative_to(ROOT) and target.exists(), f'{name}: missing {ref}'
        if link.fragment:
            assert target.name in pages and unquote(link.fragment) in pages[target.name].ids, f'{name}: missing anchor {ref}'
        count += 1
    print(f'{name}: balanced HTML; unique IDs; named navigation; one h1/main; image/video checks passed')
print(f'{count} local references and accessibility targets passed; no root-relative paths')
print('External documentation links:')
for url in sorted(set.union(*(p.external for p in pages.values()))): print(url)
