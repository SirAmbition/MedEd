# Common rules (every agent reads this, nothing else from the README)

- Audience: final-year medical students, interns, residents, BPT trainees (Australia). Never basic: every slide must teach a PGY1 something new.
- Australian spelling and units. Never use em dashes or en dashes (use colons, commas, "to").
- Source rule: paraphrase only. Never copy wording, list order or images from the source. Subscription sources (UpToDate, eTG, AMH) are background only.
- No patient stories, no individual medical advice. Fictional cases are labelled "Fictional case".
- Reporting: you talk only to your own manager. Exception: on single-post runs B1 reports to the Supervisor (no GM B).
- Logging (light): when you finish a task, append ONE entry of at most 4 lines to log/FLOW.md in the run folder:
  `HH:MM | FROM -> TO | what you did | decision or key flag`
  Put detail in your output files, not the log.
- Worker replies to the GM: at most 8 lines: files written, 2 to 3 key decisions, confidence, flags.
- Scripts (in /home/claude/agents/scripts/): check_text.py (word limits, dashes, US spellings), build_package.py (prompts, alt-text scaffold, caption skeleton, checklist from frozen slides.md), check_sync.py (final consistency check). Use them; don't redo their work by hand.
- slides.md uses the canonical format in a1-planner-writer.md so the scripts can read it.
