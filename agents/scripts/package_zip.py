"""Package a finished run as one ZIP per topic: Topic/ -> Post 1..N/ -> files.
Usage: python3 package_zip.py runs/2026-11-15_topic --topic "Topic name" [--out exports]
- Each post-NN_series folder becomes "Post N (Series)".
- Run-level files (run-summary, source note, extract, plan, calendar rows, log) go in the topic folder.
- Verbatim licensed source text (source.txt) is never included.
Writes <out>/<topic-slug>_<run-date>.zip and prints its path.
"""
import argparse, os, re, sys, zipfile

ap = argparse.ArgumentParser()
ap.add_argument("run")
ap.add_argument("--topic", required=True)
ap.add_argument("--out", default="exports")
a = ap.parse_args()

run = a.run.rstrip("/")
date = os.path.basename(run).split("_")[0]
topic_dir = f"{a.topic} ({date})"
slug = re.sub(r"[^A-Za-z0-9]+", "-", a.topic).strip("-")
os.makedirs(a.out, exist_ok=True)
zpath = os.path.join(a.out, f"{slug}_{date}.zip")

EXCLUDE = {"source.txt"}
posts = sorted(d for d in os.listdir(run) if re.match(r"post-\d+_", d) and os.path.isdir(os.path.join(run, d)))
if not posts:
    sys.exit(f"No post-NN_series folders in {run}")

SERIES = {"approach": "Approach", "quick-ref": "Quick Ref", "friday-case": "Friday Case",
          "side-by-side": "Side by Side"}

def post_name(d):
    n, series = re.match(r"post-(\d+)_(.+)", d).groups()
    return f"Post {int(n)} ({SERIES.get(series, series.replace('-', ' ').title())})"

count = 0
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(run):
        dirs.sort()
        for f in sorted(files):
            if f in EXCLUDE or f.endswith(".pyc"):
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, run).split(os.sep)
            if rel[0] in posts:
                rel[0] = post_name(rel[0])
            z.write(full, "/".join([topic_dir] + rel))
            count += 1
print(f"{zpath} ({count} files, {len(posts)} posts)")
