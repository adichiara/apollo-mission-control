# PC+2 live validation — 2026-09-13

## Result

A full nominal Apollo 13 PC+2 sequence was run through the deployed Render build using the facilitator test console.

- All scheduled scenario events occurred at their expected GET time points through the current terminal transition into PTC preparation.
- No timing discrepancy was observed during this nominal end-to-end pass.
- The compact facilitator control-board layout materially improved test usability on mobile.

## Presentation observation

Structured controller values that are themselves objects or arrays are still rendered as raw JSON in the facilitator console. This is especially visible in CAPCOM material such as the final PC+2 PAD. For validation, the underlying data are useful, but the representation should be flattened into concise human-readable labeled rows rather than JSON blobs.

This is a facilitator/test-console presentation issue only. It does not change historical claims or simulation behavior.
