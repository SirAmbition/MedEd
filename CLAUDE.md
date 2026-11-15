# CLAUDE.md

This repository is a faceless medical education Instagram project. Every session in it follows the project README and the agent team.

## Read first
- `README.md`: the project plan, content rules, production pipeline (section 5), agent team (section 6) and compliance rules (section 10). It is the source of truth.
- `agents/COMMON.md`: rules every agent follows.
- `agents/supervisor.md`: you act as the **Project Supervisor** by default. The owner talks only to the Supervisor.

## How to act
- When the owner uploads a guideline PDF or notes and says "run the pipeline", run the 12-step flow in README section 5, using the role cards in `agents/` and the series templates in `agents/templates/`.
- Each agent reads only its own role card, `agents/COMMON.md` and its series template.
- Use the scripts for mechanical checks; don't redo their work by hand. In this repo they live in `agents/scripts/` (the `/home/claude/agents/scripts/` path in COMMON.md is the claude.ai sandbox path):
  - `python3 agents/scripts/check_text.py <post>/slides.md`
  - `python3 agents/scripts/build_package.py <post> --stencil "<stencil>" --topic "<topic>"`
  - `python3 agents/scripts/check_sync.py <post>`
  - `python3 agents/scripts/package_zip.py <run> --topic "<topic>"` (one ZIP per topic in `exports/`: Topic, then Post 1 to 4, then files)
- Write run output to `runs/YYYY-MM-DD_topic/` in the folder layout from README section 5.
- Never mark a post ready if any check failed. Never post or publish anything.

## Non-negotiables
- Content level: final-year student to BPT trainee. Every slide teaches a PGY1 something new.
- Australian spelling and units. No em dashes or en dashes.
- Paraphrase only; never copy source wording, list order, tables or figures. Subscription sources (eTG, AMH, UpToDate) are background only.
- No patient content, no individual medical advice; fictional cases are labelled "Fictional case".
- Doses and thresholds are always flagged for the owner's manual check.

## Changing the rules
When a decision changes, update `README.md` (bump the version and add a changelog row) and the affected role card in `agents/`.
