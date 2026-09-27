#!/usr/bin/env python3
"""Refill the shared parts of every page from partials/.

In a page, a block like

    <!-- include: header -->
    ...anything...
    <!-- end: header -->

is replaced in place with the contents of partials/header.html.
The nav link pointing to the current page gets aria-current="page".

Usage: python3 build.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
PARTIALS = ROOT / "partials"
BLOCK = re.compile(r"<!-- include: (\w+) -->.*?<!-- end: \1 -->", re.S)


def url_of(page):
    url = "/" + page.relative_to(ROOT).as_posix()
    return url.removesuffix("index.html")


def render(name, url):
    html = (PARTIALS / f"{name}.html").read_text().strip()
    return html.replace(f'<a href="{url}">', f'<a href="{url}" aria-current="page">')


def build(page):
    src = page.read_text()
    url = url_of(page)
    out = BLOCK.sub(
        lambda m: f"<!-- include: {m[1]} -->\n{render(m[1], url)}\n<!-- end: {m[1]} -->",
        src,
    )
    if out != src:
        page.write_text(out)
        print("updated", page.relative_to(ROOT))


for page in sorted(ROOT.rglob("*.html")):
    if not page.is_relative_to(PARTIALS) and ".git" not in page.parts:
        build(page)
