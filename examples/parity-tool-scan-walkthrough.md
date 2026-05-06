# Parity Tool Scan Flow Walkthrough

This note is the quickest way to read the extra review model in `parity-tool-scan-flow`.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | file span | 116 | watch |
| stress | terminal width | 163 | ship |
| edge | argument risk | 204 | ship |
| recovery | report density | 174 | ship |
| stale | file span | 136 | watch |

Start with `edge` and `baseline`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

`edge` is the optimistic case; use it to make sure the scoring path still rewards strong signal.
