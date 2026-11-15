"""Shared parser for slides.md (canonical format written by the Planner-Writer).

## Slide N: Title
**Headline:** text
**Body:** text
**Visual:** layout and icon idea (no text in icons)
**Source:** pages / guideline
"""
import re

FIELD = r"\*\*{}:\*\*\s*(.*?)\s*(?:\(\d+ words\))?\s*$"

US_SPELLINGS = {
    "edema": "oedema", "hemorrhage": "haemorrhage", "hemorrhagic": "haemorrhagic",
    "anemia": "anaemia", "esophagus": "oesophagus", "esophageal": "oesophageal",
    "hypoxemic": "hypoxaemic", "hospitalized": "hospitalised", "color": "colour",
    "center": "centre", "behavior": "behaviour", "pediatric": "paediatric",
    "tumor": "tumour", "gastroesophageal": "gastro-oesophageal", "percent": "per cent",
    "fiber": "fibre", "liter": "litre", "anesthesia": "anaesthesia", "leukemia": "leukaemia",
    "orthopedic": "orthopaedic", "melena": "melaena", "diarrhea": "diarrhoea",
}
AUS_WATCH = ["oedema", "haemorrhage", "haemodynamic", "anaemia", "oesophag", "hypoxaemi",
             "hospitalised", "tumour", "melaena", "diarrhoea", "per cent", "paediatric",
             "haematemesis", "gastro-oesophageal", "colour", "centre", "litre", "anaesthe"]


def parse(path):
    text = open(path, encoding="utf-8").read()
    slides = []
    for block in re.split(r"(?m)^## Slide ", text)[1:]:
        m = re.match(r"(\d+)\s*:?\s*(.*)", block)
        n, title = int(m.group(1)), m.group(2).strip()
        def get(name):
            mm = re.search(FIELD.format(name), block, re.M)
            return mm.group(1).strip() if mm else ""
        slides.append({"n": n, "title": title, "headline": get("Headline"),
                       "body": get("Body"), "visual": get("Visual"), "source": get("Source")})
    return slides


def words(s):
    return len(s.split())
