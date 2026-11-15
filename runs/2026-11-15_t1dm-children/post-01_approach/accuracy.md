# Accuracy check: post-01_approach

Checked against source.txt page markers (UpToDate v40.0). Open-guideline access: only PubMed/PMC via tool; web fetch blocked (403). Nothing marked confirmed unless read.

| Claim | Slide | Source page | Verdict | Open-guideline confirmation |
|---|---|---|---|---|
| Classic symptoms + random venous glucose 11.1 mmol/L or more diagnostic; OGTT seldom needed; no repeat needed if unequivocal | 1 | p.8 | OK | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |
| Polyuria/polydipsia over 90%, found by asking; hypovolaemic without looking dry | 2 | p.5 | OK | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |
| DKA about 30% (15 to 70%); higher under 6 or socioeconomic disadvantage; over half under 3 | 3 | p.6 | OK | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |
| GAD65, IA-2, IAA, ZnT8 at presentation, before or soon after insulin; insulin antibodies 10 to 14 days | 4 | p.9 | OK | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |
| HbA1c 6.5% needs confirmation; fasting 7.0 on more than one occasion; variants/rapid turnover mislead; 10 to 12 weeks | 5 | p.8 | FIXED (headline said 12-week average; now 10 to 12 weeks) | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |
| Type 1A vs 1B | 6 | p.10 | OK | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |
| Insulin and C-peptide after recovery; low in T1DM, high in T2DM | 7 | p.10 | FIXED (added 'if T2DM is possible', source's condition) | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |
| Diabetes commonest cause in healthy child; critical illness, high-dose glucocorticoids, sympathomimetics; drug list | 8 | p.10, p.11, p.12 | FIXED ('antipsychotics' now 'atypical antipsychotics', p.12) | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |
| Renal glycosuria/Fanconi: glycosuria, normal plasma glucose | 9 | p.12 | OK | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |
| Summary sequence | 10 | p.8 to p.12 | OK | UNCONFIRMED (no web access; only PubMed tool reachable, ISPAD 2022 definition/classification chapter not in PMC) |

Doses/thresholds for owner's manual check: random glucose 11.1 mmol/L; fasting 7.0 mmol/L (more than one occasion); HbA1c 6.5% (NGSP assay); antibody timing 10 to 14 days; DKA 30% (15 to 70%), over half under 3; over 90% polyuria/polydipsia.

Text check (check_text.py): PASS (after fixing S5 headline length).
Send-backs: none. Confirmed in open guidelines: 0 of 10 rows; unconfirmed: 10.

## Update after Supervisor review
- S8 and key claim now say 'atypical antipsychotics'. Text check re-run: PASS.
- Second open-guideline attempt: ADA SoC 2026 S2 (PMC12690183) and 2025 S2 (PMC11635041) returned abstract only, so no ADA confirmation could be read. Counts: confirmed 0, different 0, unconfirmed 10.
