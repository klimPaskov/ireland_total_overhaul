# Ireland visual and historical-AI cleanup handoff

Date: 2026-08-03
Feature slug: `ireland_focus_tree`

## Implemented source changes

- The 216-focus tree's authored x-lanes are compacted to `-66..66`, with no duplicate coordinates and a minimum same-row gap of 2.
- The three decision-category scripted GUIs use ordinary `text` and `pdx_tooltip` fields for ordinary localisation. `context_aware_text` remains only for bracketed scripted-localisation calls.
- The malformed outer `scripted_gui` nesting is repaired so Conditions, Northern Settlement, and Concealed Evidence are all registered inside one valid container.
- The 420 action-cost localisation keys (140 base, 140 blocked, 140 tooltip) use compact row text and retain the detailed surcharge explanation in the hover tooltip.
- The 45 advisor `small` portrait slots now use native 65x67 generated cards. The original full-size `large` portrait slots remain unchanged.
- The historical-AI route guard is registered as `slopx_ireland_alternate_focus_ai_allowed`. All 18 alternate route-entry focuses use it in `available`; each also has an `ai_will_do` zero-weight modifier when `is_historical_focus_on = yes`.
- The initialization effect already assigns the De Valera base profile whenever the country is AI-controlled with Historical AI Focuses enabled. Non-historical AI-only random profile selection remains behind `NOT = { is_historical_focus_on = yes }`.

## Audit evidence

- Current focus source: 216 focus blocks, x range `-66..66`, no coordinate collisions.
- Current focus icon source audit: 216 focus references resolve to 216 definitions and backing files.
- Broad Ireland sprite audit: 303 references resolve to 303 definitions; no missing texture files.
- Advisor workflow: 45 DDS cards reopen as 65x67 with the expected one-level BGRA payload; 45 prefixed preview PNGs are available.
- Localisation file remains UTF-8 with BOM and all 420 action-cost keys match their intended compact values.

## MCP status

The target Ireland source was inspected against the local documentation and existing Ireland audit records. The live HOI4 MCP calls in this desktop session currently return `WORKSPACE_NOT_REGISTERED` for the Ireland workspace, so a fresh MCP render could not be generated from this session. No unsupported GFX or GUI fields were introduced while that registration is unavailable.
