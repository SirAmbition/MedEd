"""Final consistency check: every slide's exact headline and body appear in image-prompts.md and alt-text.txt.
Usage: python3 check_sync.py post_folder
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slideslib import parse

post = sys.argv[1]
slides = parse(os.path.join(post, "slides.md"))
fails = []
for fname in ("image-prompts.md", "alt-text.txt"):
    path = os.path.join(post, fname)
    if not os.path.exists(path):
        fails.append(f"{fname} missing")
        continue
    txt = open(path, encoding="utf-8").read()
    for s in slides:
        for field in ("headline", "body"):
            if s[field] and s[field] not in txt:
                fails.append(f"{fname}: slide {s['n']} {field} not found word for word")
print("SYNC CHECK:", "PASS" if not fails else "FAIL")
for f in fails:
    print(" -", f)
sys.exit(1 if fails else 0)
