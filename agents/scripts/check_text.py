"""Mechanical checks on slides.md: word limits, dashes, US spellings.
Usage: python3 check_text.py path/to/slides.md [--max-head 8] [--max-body 35]
Exit code 1 if any check fails.
"""
import re, sys, argparse
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from slideslib import parse, words, US_SPELLINGS

ap = argparse.ArgumentParser()
ap.add_argument("slides")
ap.add_argument("--max-head", type=int, default=8)
ap.add_argument("--max-body", type=int, default=35)
a = ap.parse_args()

raw = open(a.slides, encoding="utf-8").read()
fails = []
for s in parse(a.slides):
    if not s["headline"] or not s["body"]:
        fails.append(f"S{s['n']}: missing headline or body")
    if words(s["headline"]) > a.max_head:
        fails.append(f"S{s['n']}: headline {words(s['headline'])} words (max {a.max_head})")
    if words(s["body"]) > a.max_body:
        fails.append(f"S{s['n']}: body {words(s['body'])} words (max {a.max_body})")
    for field in ("headline", "body"):
        for us, aus in US_SPELLINGS.items():
            if re.search(rf"\b{us}\b", s[field], re.I):
                fails.append(f"S{s['n']} {field}: '{us}' should be '{aus}'")
for ch, name in (("—", "em dash"), ("–", "en dash")):
    if ch in raw:
        fails.append(f"file contains an {name} ({raw.count(ch)}x)")

print("TEXT CHECK:", "PASS" if not fails else "FAIL")
for f in fails:
    print(" -", f)
sys.exit(1 if fails else 0)
