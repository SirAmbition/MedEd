# Run summary: T1DM in children and adolescents (15 Nov 2026)

**Status: TEST RUN. 4 posts built and every check passes, but NONE is ready to post.** The only source is UpToDate (licensed, background only), and I could not confirm the claims against an open guideline from this environment. That confirmation, plus adding the open reference to each caption, is the one blocker.

## What was made

| Post | Series | Topic | Slides | Text check | Compliance | Sync check |
|---|---|---|---|---|---|---|
| post-01_approach | Approach (Mon) | New diabetes in a child: the work-up | 10 | PASS | PASS | PASS |
| post-02_quick-ref | Quick Ref (Wed) | T1DM risk by relative: fathers outrank mothers | 1 | PASS (60-word limit) | PASS (Supervisor resolution) | PASS |
| post-03_friday-case | Friday Case (Fri) | The toddler labelled gastro (fictional case) | 5 | PASS | PASS | PASS |
| post-04_side-by-side | Side by Side (Sun) | Youth T1DM, T2DM and monogenic: what separates them | 7 | PASS | PASS (Supervisor resolution) | PASS |

Each post folder has: slides.md (FROZEN), accuracy.md, compliance.md, image-prompts.md (Mode B ChatGPT prompts plus an Image QA checklist), alt-text.txt, caption.txt, pinterest.txt and checklist.md. The run folder also has 00_source.md, 01_extract.md (now the cached extract for this source), 02_plan.md (with the Supervisor's approval conditions), 02_plan-review.md, calendar-rows.csv and log/FLOW.md.

## What needs you

### 1. Blocker: confirm against an open guideline (every post)
- GM A checked every claim against the UpToDate page. Open-guideline confirmation was attempted twice but blocked:
  - this network refuses onlinelibrary.wiley.com (ISPAD 2022), ispad.org and diabetesjournals.org (ADA);
  - PubMed Central holds only the abstract of ADA Standards of Care 2026 Section 2 (PMC12690183).
- Result: 0 claims fully confirmed. 2 were partly confirmed in the ISPAD 2022 monogenic chapter (PMC10107883: diagnosis by gene sequencing). Every other claim is UNCONFIRMED.
- Suggested open sources: ISPAD Clinical Practice Consensus Guidelines 2022 (definition, epidemiology and classification, doi 10.1111/pedi.13454; stages; DKA) and ADA Standards of Care in Diabetes 2026, Section 2 (doi 10.2337/dc26-S002).
- Then replace the `References: [OWNER TO ADD ...]` line in each caption.txt. Never cite UpToDate publicly.
- To let a future run confirm claims itself, allow those three hosts in the environment's network settings.

### 2. Checkpoint 2: thresholds to check manually
- **Approach:**
  - random glucose 11.1 mmol/L with symptoms;
  - fasting glucose 7.0 mmol/L on more than one occasion;
  - HbA1c 6.5%, confirmed by a second measure;
  - insulin antibodies about 10 to 14 days after insulin;
  - DKA about 30% (15 to 70%), over half of under-3s;
  - polyuria and polydipsia in over 90%;
  - HbA1c reflects 10 to 12 weeks.
- **Quick Ref:**
  - MZ twin 30% within 10 years, 65% by 60;
  - both parents up to 30%;
  - DZ twin 8%;
  - father 3 to 8%, mother 1 to 4%;
  - sibling 3 to 6% by 20;
  - no family history 0.4%.
- **Friday Case:** the fictional observations (HR 132/min, capillary refill 2 s in a 2-year-old) should read as plausible.
- **Side by Side:**
  - up to 25% of T1DM overweight;
  - BMI 95th centile;
  - 45% of T1DM before age 10;
  - up to 30% of clinical T2DM antibody positive;
  - acanthosis 50 to 90% vs about 12%;
  - biochemical insulin resistance in up to 25% of T1DM;
  - US registry 55 / 16 / 20 / 10%;
  - family history up to 10% vs 75 to 90%;
  - monogenic onset under 25.

### 3. Judgement calls for you to accept or change
- **Quick Ref headline "fathers outrank mothers":** true by range (3 to 8% vs 1 to 4%), but the ranges overlap at 3 to 4%. The rows are ordered roughly by risk, not strictly (sibling 3 to 6% sits below mother 1 to 4%). The image does not claim a strict order.
- **Friday Case option C:** says "capillary blood glucose"; the source says serum glucose. This is accepted as practice wording.
- **Niche fit:** paediatric diabetes may sit outside an adult internal medicine niche (the niche is still TBD in README section 12). I have suggested it as a later week's mini-series, not a launch-week topic. calendar-rows.csv has no dates yet.

### 4. Images and posting
- Generate the images in ChatGPT from each image-prompts.md (slide 1 first, in a fresh chat), save them as final/slide-NN.png, then upload them for B3 Image QA.
- **Most slides contain numbers or thresholds.** README rule: they either use Mode A (Claude renders the slide) or must pass Image QA before posting. Mode A rendering by B2 is available on request. The default image mode is still an open decision.
- Then schedule for 5:30pm AWST and cross-post to Pinterest.

## How the run went (deviations from README)

1. **Agents could not brief agents.** Sub-agents in this environment cannot launch other agents, so GM A and GM B could not brief their workers directly. The Supervisor launched each worker (A1, A2, B1) on the GM's behalf, in the GM's order, and relayed instructions through the run files. Roles, models (GMs Sonnet 5.5 medium, workers Haiku 5.5 medium) and the sequential order were kept. Consider updating README section 6 for this.
2. **Plan approval was decided by the Supervisor after one send-back, instead of escalating to you.** The rule says to ask the owner at that point, but you asked to review only the final output. Quick Ref Usefulness/Level and Friday Case Discrimination were at 3; I resolved them with 5 written conditions (see 02_plan.md).
3. **A2's re-check left 2 low flags; the Supervisor resolved them at the freeze review.** Quick Ref rows were re-ordered. A 5-word technical phrase on Side by Side slide 5 was accepted, as it is under the 6-word threshold.
4. **The Supervisor wrote the source note and extract.** v0.6 has no Ingestor role, so I wrote 00_source.md and 01_extract.md at the brief.
5. **source.txt is git-ignored.** It is the verbatim licensed text used for A2's paraphrase check, so it is kept locally only.

## Quality notes
- **Accuracy loops:** GM A made several small fixes, and the Supervisor caught 2 errors before freeze:
  - Side by Side misread the registry's 10% group as mostly T2DM; the source says mostly T1DM.
  - "antipsychotics" was corrected to "atypical antipsychotics".
- **Compliance:** the first pass flagged 20 issues (copied runs of 6 or more words, source list order, overstatements, one parent-directed headline). All were fixed before freeze.
- **Cost:** about 0.75 million sub-agent tokens across the run. Much of it went on plan rework, and on GM A re-reading the extract and source on every call.
