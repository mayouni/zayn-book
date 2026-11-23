#!/usr/bin/env python3
"""Write each page of the built reader as the text a reader sees, for the fresh readers.

A fresh reader judges the page, not the source: the reports under each plate come from the run and are not in the Markdown.
This tool takes each article of en/index.html and writes its text, in reading order, to .cache/as-read/<slug>.txt (ignored by
git). It changes nothing in the book.

    python tools/as_read.py            # every page
    python tools/as_read.py ch8        # the pages whose slug starts with ch8
"""
import html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / ".cache" / "as-read"


def text_of(article):
    a = article
    a = re.sub(r'<span class="cl[^"]*">(.*?)</span>(?=<span class="cl|</code>)', lambda m: m.group(1) + "\n", a, flags=re.S)
    a = re.sub(r"<(script|style)\b.*?</\1>", "", a, flags=re.S)
    a = re.sub(r'<span class="exit">(.*?)</span>', r"[\1] ", a)
    a = re.sub(r'<span class="sk-rule">(.*?)</span>', r" (\1)", a)
    a = re.sub(r'<span class="(?:sk-ctl sk-missing)">', "[missing control: ", a)
    a = re.sub(r'<span class="(?:sk-ctl sk-restored)">', "[restored control: ", a)
    a = re.sub(r'<span class="sk-ctl">', "[control: ", a)
    a = re.sub(r"<(h1|h3|h4)\b[^>]*>", "\n\n## ", a)
    a = re.sub(r"</(p|div|h1|h3|h4|li|pre|figcaption|dt|dd|section|aside|figure|ul|dl|tr)>", "\n", a)
    a = re.sub(r"</t[dh]>", " | ", a)
    a = re.sub(r"<[^>]+>", "", a)
    t = html.unescape(a).replace("​", "")
    t = re.sub(r"[ \t]+\n", "\n", t)
    return re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"


def main():
    want = sys.argv[1] if len(sys.argv) > 1 else ""
    page = (ROOT / "en" / "index.html").read_text(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    for m in re.finditer(r'<article class="chapter-page" id="page-([^"]+)".*?</article>', page, re.S):
        slug = m.group(1)
        if want and not slug.startswith(want):
            continue
        text = text_of(m.group(0))
        (OUT / f"{slug}.txt").write_text(text, encoding="utf-8", newline="\n")
        print(f"{slug}: {len(text.split())} words -> .cache/as-read/{slug}.txt")


if __name__ == "__main__":
    main()
