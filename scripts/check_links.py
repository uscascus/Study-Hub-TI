"""Check local HTML resources, anchors and Markdown file targets; no network access."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for attr in ('href', 'src'):
            if attr in attrs:
                self.links.append(attrs[attr])

pages = {}
for path in SITE.rglob('*.html'):
    page = Page()
    page.feed(path.read_text(encoding='utf-8'))
    pages[path.resolve()] = page

errors = []
checked = 0
for source, page in pages.items():
    for link in page.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        target = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
        if target.is_dir():
            target /= 'index.html'
        checked += 1
        if not target.exists():
            errors.append(f'{source.relative_to(ROOT)}: missing {link}')
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f'{source.relative_to(ROOT)}: missing anchor {link}')

for source in ROOT.rglob('*.md'):
    if '.git' in source.parts:
        continue
    for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)\s]+)\)', source.read_text(encoding='utf-8')):
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        checked += 1
        if not (source.parent / unquote(parsed.path)).exists():
            errors.append(f'{source.relative_to(ROOT)}: missing {link}')

print(f'Checked {len(pages)} HTML pages and {checked} local targets.')
for error in errors:
    print(error)
raise SystemExit(bool(errors))
