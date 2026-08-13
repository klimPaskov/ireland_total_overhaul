# Expansion Localisation Final Audit

**Scope:** Current working-tree localisation audit for the 188-focus expansion, industrial concerns and contracts, five-family territorial decisions, postwar decisions, and Parliament live-checklist tooltips. Only small, player-facing localisation fixes were made. `thumbnail.png` and gameplay/GFX sources were not edited; no commit was created.

## Verdict

Focus, decision, category, industrial-concern, and scripted-localisation key coverage is complete. The Parliament live rows are present and match the canonical scripted triggers. Ten small wording corrections were applied to align visible rewards and territorial descriptions with their current effects. One non-localisation GFX reference and several unwrapped raw strength/state requirements remain for the owning implementation agents.

## Small localisation patch

Changed file: `localisation/english/ireland_l_english.yml`

| Key | Before | After / reason |
| --- | --- | --- |
| `ireland_aer_lingus_air_link_reward_tt` | Listed the concern and four Transport Planes only. | Also names the unlocked **Aer Lingus Transports** contract; the focus sets `ireland_industrial_contracts_open` and the company flag. |
| `ireland_turf_development_board_programme_reward_tt` | Referred to the unrelated State Materials contract. | Names the visible **Turf Fuel Reserve** contract and keeps the 500 Fuel reward. |
| `ireland_ford_cork_works_agreement_reward_tt` | Referred to the generic Transport Fleet contract. | Names the visible **Ford Motor Works** contract and keeps 50 Trucks. |
| `ireland_irish_shipping_registry_reward_tt` | Displayed `Irish Shipping`, not the idea title. | Uses the exact **Irish Shipping Registry** company title. |
| `ireland_steel_holdings_programme_reward_tt` | Referred to the unrelated State Materials contract. | Names the visible **Haulbowline Foundry** contract and the one Military Factory. |
| `ireland_harland_and_wolff_access_reward_tt` | Used a shortened company name and unrelated Merchant Tonnage contract. | Uses **Harland and Wolff Access**, **Belfast Refit Capacity**, one Northern Ireland Dockyard, and 10 Navy Experience. |
| `ireland_territorial_support_welsh_republic_desc` | Implied equipment is always sent and omitted War Support. | Explains the `WLS` conditional, records support when no Welsh government exists, states 250 Infantry Equipment where applicable, and adds 2% War Support/no claim/core. |
| `ireland_territorial_support_scottish_republic_desc` | Implied equipment is always sent and omitted War Support. | Explains the `SCO` conditional, records support when no Scottish government exists, states 250 Infantry Equipment where applicable, and adds 2% War Support/no claim/core. |
| `ireland_territorial_negotiate_atlantic_basing_desc` | Omitted the completion reward. | States that completion grants military access and 2% Stability, with no territorial transfer. |
| `ireland_territorial_review_highlands_integration_desc` | Stated the 60 Compliance/15 Resistance gate and no automatic core, but omitted the completion modifiers. | Adds the visible -10 Resistance and +10 Compliance result while retaining the no-automatic-core warning. |

The changed lines are currently around 5336, 5352-5367, and 5477-5481.

## Coverage findings

### Missing keys

None found in the audited surfaces:

- 188 actual focus IDs: every title, `_desc`, `_reward_tt`, and all 188 `custom_effect_tooltip` references resolve.
- 198 base decisions, 29 expansion decisions, and 4 marine-service decisions: every title/`_desc` resolves; all `custom_effect_tooltip`, `custom_trigger_tooltip`, `custom_cost_text`, and `tooltip` references resolve.
- 15 decision categories: every title and `_desc` resolves.
- 9 industrial concerns: every idea name and `_desc` resolves.
- Scripted localisation: 29 defined-text names with 90 unique `localization_key` outputs in `ireland_localisation.txt`, plus 7 outputs in `ireland_coastwatch.txt`; all outputs resolve. The 18 Parliament status projections are defined and referenced by the four GUI tooltips.

### Duplicate keys

None. `ireland_l_english.yml` has 5,484 unique parsed keys; `ireland_game_rules_l_english.yml` has 7 unique keys.

### Scripted localisation and Parliament

No broken scripted-localisation references were found. The four Parliament button tooltips already expose live rows for stage, Dublin ownership, settlement/constitutional/government gates, completion state, chamber majorities, and 25/35 Political Power thresholds. Their wording matches the current `ireland_parliament.txt` triggers (strict `> 24` and `> 34` checks are correctly displayed as "At least 25" and "At least 35"). Dynamic majority rows use the live vote/seat and threshold variables.

### Decision requirement text opportunity (not patched)

`common/decisions/ireland_expansion_decisions.txt` still exposes some requirements as raw script rather than custom player-facing rows:

- `ireland_territorial_deliver_ulster_ultimatum` (lines 215-229) and `ireland_territorial_enforce_border_demand` (280-287) directly show state 119 ownership/controller and strength-ratio checks without a `custom_trigger_tooltip` wrapper.
- The staged claims for states 120, 122, and 123 wrap readiness and foreign-controller conditions, but leave the direct `strength_ratio < @IRELAND_TERRITORIAL_STRENGTH_RATIO_LIMIT` rows unwrapped (lines 357-372, 388-407, and 423-442).

The existing readiness and foreign-controller tooltip keys are valid. Adding a ratio/target explanation needs a small decision-script change and should be owned by the decisions agent; no raw-trigger localisation was invented here.

## GFX-visible references

- All 188 focus icon references resolve to definitions in `interface/*.gfx`.
- Existing base-decision, marine-service, and category icon references resolve. Expansion decision icons resolve except `GFX_decision_ireland_open_a_customs_port`, used by `ireland_territorial_offer_belfast_compact` and `ireland_territorial_negotiate_atlantic_basing`; no definition exists in the current interface files. This is an asset/GFX follow-up, not a localisation patch.
- `interface/ireland_industrial_concerns.gfx` has all nine company sprites and all nine referenced texture files. Targeted `ireland_icons.gfx`, `ireland_focus_expansion_shine.gfx`, and `ireland_industrial_concerns.gfx` texture checks found no missing files.

## Encoding and validation

- Consulted the required offline Paradox wiki localisation, focus, decision, scope, interface, and scripted-GUI pages plus vanilla `effects_documentation.md` and `triggers_documentation.md` before auditing.
- Both English localisation files retain UTF-8 BOM encoding. The main file is CRLF and the game-rules file is LF; no encoding repair was needed.
- PowerShell key audits, focus/decision/category/company coverage checks, scripted-localisation output checks, duplicate-key checks, GFX definition checks, and targeted texture-file checks were rerun after the patch.
- No in-game runtime or GUI render was run in this read-only audit. Controller-change timing and raw-trigger display remain unproven at runtime.

## Handoff

- Parent should review the ten changed keys above; no gameplay meaning was changed.
- The missing customs-port GFX definition and the raw strength/state requirement wrappers remain open implementation issues.
- No unresolved localisation-key or encoding issue remains in the audited expansion/Parliament surfaces.
- No commit was made, and `thumbnail.png` was not touched.

## Parent closure — 2026-08-13

The two gameplay-adjacent opportunities above were closed after this
localisation pass. The stale customs-port sprite reference was replaced by the
registered Atlantic-route sprite, and the State 119 plus staged 120/122/123
controller/strength checks are wrapped in named player-facing requirement
tooltips. The postwar mission-capacity requirement and launch-refund tooltips
are also defined. No localisation or GFX blocker remains.
