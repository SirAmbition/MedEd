# post-02_quick-ref: compliance review (A2)

Checked: verbatim word runs (5 and 6+ words) in every Headline and Body against source.txt, near-swaps, list order, overstatement, AHPRA, disclosure.

| Slide | Issue | Suggested rewrite |
|---|---|---|
| 1 (headline) | "Your child's T1DM risk" addresses a parent and reads as individual risk information. This is a clinician education post (AHPRA, medium). | Childhood T1DM risk by affected relative |
| 1 (body) | Verbatim 6-word run "of an affected father 3 to" (p.3, "Offspring of an affected father, 3 to 8 percent") (medium). | Affected father 3 to 8%, affected mother 1 to 4%. No family history 0.4%. Non-twin sibling 3 to 6% by age 20. Dizygotic twin 8%. Monozygotic twin 30% within 10 years of the first twin's diagnosis, 65% by age 60. Both parents affected: up to 30%. Lifetime risk; sibling and twin rows have set time frames. |

Note (low, no rewrite required): the sibling, dizygotic and monozygotic rows keep the p.4 order. The post's stated reason is ascending risk, which is acceptable. If the table is redesigned, put a different row first so the order is the post's own.

AHPRA: no patient information, no individual advice, no testimonials. Friday Case not used. Disclosure: no sponsor or affiliate content.

Flags: 2 (1 medium AHPRA framing, 1 medium verbatim run), plus 1 low note.


## Fixes applied (GM A, after compliance review)
Both flags accepted. Text check (--max-body 60) PASS.
- Title and headline now "Childhood T1DM risk by affected relative" (clinician-facing).
- Body: "of an affected father 3 to" run removed; now "Child's risk: father affected 3 to 8%, mother affected 1 to 4% (father higher)". Row order is the post's own (parents, none, sibling, DZ, MZ, both parents). Figures unchanged (p.3, p.4).

## Re-check (A2, after GM A fixes)

Scope: current slides.md against source.txt. Verbatim scan (5 and 6+ word runs) clean; the 6-word run is removed. Headline and body wording are fine.

| Slide | Remaining issue | Suggested rewrite |
|---|---|---|
| 1 (headline) | none | none |
| 1 (body) | Low: the sibling, dizygotic and monozygotic rows still run in the source's order (p.4: non-twin sibling, dizygotic twin, monozygotic twin). The GM fix changed the order of the other rows only. | Child's risk: father affected 3 to 8%, mother affected 1 to 4% (father higher). No family history 0.4%. Monozygotic twin 30% within 10 years of first twin's diagnosis, 65% by age 60. Dizygotic twin 8%. Non-twin sibling 3 to 6% by age 20. Both parents affected: reported up to 30%. Lifetime risk; sibling and twin rows have set time frames. |

Flags remaining: 1 (low).

VERDICT: FIX NEEDED

Supervisor resolution: rows re-ordered by descending risk at freeze review. VERDICT: PASS
