# parity-tool-scan-flow

`parity-tool-scan-flow` explores cli tools with a small Python codebase and local fixtures. The technical goal is to package a Python local lab for scan analysis with node-edge fixtures, cycle and reachability reports, and documented operating limits.

## Use Case

I want this repository to be useful as a quick reading exercise: fixtures first, implementation second, verifier last.

## Parity Tool Scan Flow Review Notes

The first comparison I would make is `argument risk` against `file span` because it shows where the rule is most opinionated.

## Highlights

- `fixtures/domain_review.csv` adds cases for file span and terminal width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/parity-tool-scan-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `argument risk` and `file span`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Code Layout

The implementation keeps the scoring rule plain: reward signal and confidence, preserve slack, penalize drag, then classify the result into a review lane.

The Python implementation avoids hidden state so fixture changes are easy to reason about.

## Run The Check

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Regression Path

The check exercises the source code and the review fixture. `edge` is the high score at 204; `baseline` is the low score at 116.

## Future Work

The repository is intentionally scoped to local checks. I would expand it by adding adversarial fixtures before adding features.
