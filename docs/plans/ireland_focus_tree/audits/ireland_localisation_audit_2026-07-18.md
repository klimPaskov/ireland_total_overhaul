# Ireland localisation and scripted-localisation audit

Date: 2026-07-18  
Scope: Ireland overhaul focus, decision, mission, law, spirit, achievement, GUI, event, and scripted-localisation surfaces in the current workspace.  
Disposition: direct localisation coverage is complete. One narrow wording defect was patched. Several source/runtime wiring defects remain blocked on gameplay-owner decisions.

Status reconciliation (2026-07-22): the direct key-coverage result remains useful, but the stale runtime defect list in this historical audit is superseded where current source evidence shows setters, persistent display values, focus-layout refresh, and GUI scripted-localisation consumers. Relevant evidence is `common/scripted_effects/slopx_ireland_culture.txt`, `common/scripted_effects/slopx_ireland_effects.txt`, `common/national_focus/slopx_ireland_focus_tree.txt`, and `common/scripted_localisation/slopx_ireland_localisation.txt`. Live parse and scenario validation remain not-run; use `docs/plans/ireland_focus_tree/source_of_truth_map.md` for current disposition.

Post-audit repair addendum (2026-07-22): the earlier duplicate Northern-failure branch was removed; `slopx_ireland_sync_plebiscite_state` now sets and clears `slopx_ireland_northern_plebiscite_open`; `slopx_ireland_settlement_bop_value` is initialized and refreshed as a persistent country variable; concealed-evidence counters and reveal state are initialized and synchronized; and the evidence focus explicitly calls `mark_focus_tree_layout_dirty`. The historical issue list below is retained for traceability, but these source/runtime defects are no longer current blockers. Fresh engine and scenario validation remains open.

## Scope and method

This audit inspected the current source files, not the stale localisation handoff. The required repository instructions and skills were read before the audit: `hoi4-events`, `hoi4-decisions-missions`, `hoi4-focus-trees`, `hoi4-text-audio-research`, `hoi4-improvement-loop`, and `hoi4-subagents`. The offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, national focuses, interface modding, and scripted GUI modding were consulted alongside the relevant vanilla documentation.

The requested `fork_context=false` constraint was respected. No custom subagent was spawned because no callable project-subagent tool was available in this session; the audit was performed directly against the workspace. No gameplay design or asset files were changed.

## Exact coverage

The source-ID inventories were compared against `localisation/english/slopx_ireland_l_english.yml`. “Expected” means the exact title/description or engine-localisation surface implied by the source ID; event counts include title, description, and option keys found in the event source.

| Surface | Source IDs / refs | Expected localisation keys | Missing |
|---|---:|---:|---:|
| National focuses | 216 focus nodes | 432 (`id`, `id_desc`) | 0 |
| Decision categories | 13 | 26 (`id`, `id_desc`) | 0 |
| Decisions/actions | 140 | 280 (`id`, `id_desc`) | 0 |
| Missions | 54 | 108 (`id`, `id_desc`) | 0 |
| Ideas/spirits | 63 | 126 (`id`, `id_desc`) | 0 |
| Achievements | 32 | 64 (`id_NAME`, `id_DESC`) | 0 |
| National Settlement BOP sides/ranges | 9 | 18 (`id`, `id_desc`) | 0 |
| Main events | 249 event IDs | 996 event localisation refs | 0 |
| Flavour events | 236 event IDs | 944 event localisation refs | 0 |
| GUI static localisation | 133 unique refs | 133 | 0 |
| GUI scripted-localisation calls | 4 defined names | 4 defined names | 0 |

The three GUI files contain 135 static-reference occurrences, 133 unique static keys, and four scripted calls, for 137 distinct GUI localisation surfaces. The shared `slopx_ireland_gui_close_tooltip` occurrence is intentional. All 20 `localization_key` outputs in `common/scripted_localisation/slopx_ireland_localisation.txt` also exist in the YML.

The law source contains 17 live matrix families in `common/scripted_effects/slopx_ireland_laws.txt`: `censorship`, `constitutional_government`, `economic_control`, `education`, `emergency_authority`, `foreign_access`, `guarantee`, `internment`, `language`, `mobilisation`, `northern_settlement`, `occupation`, `public_order`, `rationing`, `religion`, `tillage`, and `trade_shipping`. The current GUI exposes four generic law-review status outputs (`slopx_ireland_law_review_abuse`, `slopx_ireland_law_review_due`, `slopx_ireland_law_review_active`, and `slopx_ireland_law_review_open`); there are no source references requiring per-family law name/stage keys, so no law key is missing from the current contract.

The 15 route-character IDs in `common/characters/slopx_ireland_route_characters.txt` all have runtime references. Their names are direct character fields rather than missing localisation keys.

## Missing key list

No missing direct keys were found for focuses, decision categories, decisions, missions, spirits, achievements, BOP sides/ranges, main events, flavour events, or static GUI references.

No missing `localization_key` output was found in `common/scripted_localisation/slopx_ireland_localisation.txt`.

This is a coverage result only. It does not certify that every referenced variable or flag is initialized at runtime; those defects are listed below.

## Duplicate key list

- Exact duplicate localisation keys in `localisation/english/slopx_ireland_l_english.yml`: none.
- Duplicate focus, category, decision, mission, spirit, achievement, BOP, main-event, or flavour-event source IDs: none in the inventories above.
- Duplicate scripted-localisation output names: none; the four names are unique and all are used by the GUI.
- A duplicate trigger branch exists in `GetSlopxIrelandNorthernFailureState`, but it is not a duplicate key: lines 88 and 94 of `common/scripted_localisation/slopx_ireland_localisation.txt` both test `slopx_ireland_northern_settlement_failure`.

## Scripted-localisation issue list

1. `common/scripted_localisation/slopx_ireland_localisation.txt:88` and `:94` use the identical trigger `has_country_flag = slopx_ireland_northern_settlement_failure`, with outputs `slopx_ireland_northern_failure_occupation` and `slopx_ireland_northern_failure_settlement` respectively. Scripted localisation selects the first matching branch, so `slopx_ireland_northern_failure_settlement` is unreachable. The source has only one setter for the settlement-failure flag and no second discriminator. This cannot be fixed safely by choosing or inventing a flag in localisation.

2. `GetSlopxIrelandNorthernModel` at `common/scripted_localisation/slopx_ireland_localisation.txt:39` tests `slopx_ireland_northern_plebiscite_open`, but no `set_country_flag` for that ID exists anywhere in the current source. The flag is checked by four event paths (`events/slopx_ireland_events.txt:15064`, `:15153`, `:15242`, `:15331`) and four runtime paths (`common/scripted_effects/slopx_ireland_runtime.txt:7128`, `:7157`, `:7186`, `:7215`). This is a source/runtime ID mismatch and leaves the plebiscite display branch and related gates dead until gameplay code defines the flag or removes the stale references.

3. The other scripted-localisation branches have valid fallback branches and all 20 output keys are present. `GetSlopxIrelandNorthernModel`, `GetSlopxIrelandNorthernRegion`, `GetSlopxIrelandNorthernFailureState`, and `GetSlopxIrelandLawReviewStatus` are all called by the relevant GUI files. No missing scripted-localisation definition was found.

## Dynamic values and opportunities

The YML contains 32 unique dynamic-variable tokens. Decision burden/cost values, active mission counts, Northern settlement values, readiness/provision values, and the law-review status call have source references and localisation keys.

The following dynamic contracts need gameplay-owner work:

- Concealed Evidence counters and reveal state are declared by the GUI contract in `interface/slopx_ireland_concealed_evidence.gui:5-12` and read by `common/scripted_guis/slopx_ireland_scripted_guis.txt:269-293`. The six displayed values are `slopx_ireland_concealed_evidence_credible_count`, `...category_count`, `...region_count`, `...public_knowledge`, `...disqualifier_count`, and `...obligation_count`; the gate is `slopx_ireland_concealed_evidence_revealed`. No gameplay setter was found for those six variables or for the reveal flag. The keys are present, but the values/statuses are not runtime-backed.

- The event and flavour-event strings repeatedly display `[?slopx_ireland_settlement_bop_value|0]` (for example `localisation/english/slopx_ireland_l_english.yml:858-894` and `:1855-1873`). `common/scripted_effects/slopx_ireland_effects.txt:361-362` creates that value with `set_temp_variable`, and `:370` consumes it only inside the BOP meta-effect. A temporary variable is not a persistent country display value; later event/flavour localisation may therefore render an undefined or stale value. The owner must promote a display value to an appropriate persistent scope or change the localisation to a valid persistent variable. No localisation-only substitution is safe without deciding the intended scope.

- The 17 law families currently have generic review-status localisation only because no GUI/source call requests family-specific names or stages. A future law ledger could use dynamic family/stage localisation, but adding keys now would expand design scope and was intentionally not done.

## Hidden-route concealment

The concealed focus branches use `allow_branch = { has_country_flag = slopx_ireland_hidden_permission }` at the first route gates for IRA (`:3180-3181`), Congress (`:3421-3422`), O’Duffy (`:3610-3611`), Clerical (`:3802-3803`), Ailtirí (`:3950-3951`), High King (`:4099-4100`), Five Provinces (`:4245-4246`), and Otherworld (`:4398-4399`) in `common/national_focus/slopx_ireland_focus_tree.txt`. The permission is set by `slopx_ireland_cultural_evidence_ledger` at `:2158`.

The offline focus documentation says `allow_branch` controls visibility and is evaluated on tree load or after `mark_focus_tree_layout_dirty`; `available` alone would leave a locked focus visible. No `mark_focus_tree_layout_dirty` or `load_focus_tree` call was found after the permission flag is set. Therefore route-specific titles/descriptions are concealed only if the game refreshes the focus-tree layout through another mechanism; the source currently provides no explicit refresh proof. This is a runtime blocker, not a reason to replace legitimate route names with generic localisation.

The generic fallback/UI strings remain appropriately indirect: `slopx_ireland_northern_model_contact` and its tooltip (`localisation/english/slopx_ireland_l_english.yml:3044-3045`) avoid naming a locked route, while the evidence ledger uses sealed/public-record wording at `:3150-3161`. Once a route is legitimately visible, its exact focus titles and descriptions are available as intended.

## Source/runtime ID and cross-surface mismatch notes

- The Ailtirí focus `slopx_ireland_corporate_gaelic_nation` was paired with copy referring to O’Duffy’s veteran network. That contradicted the source branch, which sets `slopx_ireland_ailtiri_corporate_state_ready`. It was corrected narrowly in the YML; see the changed-key section below.
- The conditions review click sets and clears `slopx_ireland_conditions_review_requested` at `common/scripted_guis/slopx_ireland_scripted_guis.txt:78` and `:82`, but no consumer was found. Its button says “Open the scheduled review of the national conditions” (`localisation/english/slopx_ireland_l_english.yml:3148-3149`), so the flag currently has no demonstrated review handoff.
- The Northern review click sets and clears `slopx_ireland_northern_review_requested` at `:180` and `:187`. The same click also runs `slopx_ireland_sync_northern_ledger`, `slopx_ireland_apply_northern_core_review`, and achievement tracking, so the review effect is not wholly absent; the request flag itself has no consumer and should not be treated as an event handshake without gameplay confirmation. Its visible copy is present at YML `:3086-3087`.
- The concealed-evidence inspect click sets and clears `slopx_ireland_concealed_evidence_inspection_requested` in `common/scripted_guis/slopx_ireland_scripted_guis.txt`. The request is consumed by `slopx_ireland_sync_gui_requests` in `common/scripted_effects/slopx_ireland_culture.txt`: it records the selected row, refreshes the evidence projection and hidden permissions, clears the request, and dirties the GUI. The button copy (“Open the current evidence record and its unresolved obligations”) is present in the Ireland localisation. Live click/reveal verification remains outstanding.
- The dead Northern plebiscite flag, uninitialized Concealed Evidence contract, unconsumed GUI request flags, and temporary BOP display value are all source/runtime defects rather than missing localisation keys.
- The previous handoff `docs/plans/ireland_focus_tree/localisation/localisation_handoff.md` is stale against the current worktree: it reports 3,015 expected keys, three spirits, and no scripted-localisation file, while the current source has 3,193 YML keys, 63 spirits, and four scripted-localisation definitions. It should not be used as current coverage evidence.

## Encoding and parser concerns

- `localisation/english/slopx_ireland_l_english.yml` is strict UTF-8 with the required UTF-8 BOM (`EF BB BF`). The current file has 3,205 lines; the key-shape audit found no malformed localisation lines and no `:0` keys. The file contains expected Irish diacritics and em dashes; no mojibake was found in the inspected character names.
- `common/scripted_localisation/slopx_ireland_localisation.txt` is strict UTF-8 without a BOM. This is a script file, not a localisation YML, so the YML BOM requirement does not apply.
- The touched source `.txt` files are strict UTF-8 without BOM, consistent with script-file handling. No encoding-only patch is recommended.

## Narrow patch made

Changed path:

- `localisation/english/slopx_ireland_l_english.yml:382`

Changed key:

- `slopx_ireland_corporate_gaelic_nation_desc`

Before, the description referred to “O'Duffy's veteran network,” contradicting the Ailtirí branch. It now reads:

> Make corporate gaelic nation part of a settlement that can be defended in public. Ailtirí na hAiséirghe turns language and youth organisation into a disciplined state project whose coercion is kept in view.

This changes display wording only and does not alter focus effects, route gates, mechanics, or assets.

## Recommended fixes and blockers

1. Gameplay owner: give Northern settlement failure states distinct runtime flags/variables, or intentionally remove one of the two failure outputs. Then update `common/scripted_localisation/slopx_ireland_localisation.txt:88-94` and its source-side contract together.
2. Gameplay owner: either set `slopx_ireland_northern_plebiscite_open` at the intended transition or remove the dead scripted-localisation/event/runtime references.
3. Gameplay/GUI owner: initialize and update the six Concealed Evidence counters and `slopx_ireland_concealed_evidence_revealed`, then wire the inspect request to its intended consumer. Keep the existing generic sealed-state wording until the reveal contract is real.
4. Gameplay owner: make the BOP display value persistent and scoped for later event/flavour localisation, or replace the event text token with an existing persistent settlement value.
5. Focus owner: after setting `slopx_ireland_hidden_permission`, explicitly refresh the focus-tree layout if required by the engine contract, then verify that concealed route titles remain hidden before the gate and appear after it.
6. Optional wording pass, not a coverage defect: review the generic `slopx_ireland_june_1942_public_launch_desc` and repeated Clerical bridge/service/producer descriptions noted in the focus audit after gameplay semantics are finalized. No further wording was changed here because doing so would be taste/design work.

## Validation, skipped checks, and remaining risks

Meaningful validation completed:

- Exact source-ID and localisation-key inventory for all listed surfaces.
- Exact duplicate-key and duplicate-source-ID audit.
- Scripted-localisation output-key and GUI-call cross-check.
- Dynamic-token source search, including concealed-evidence variables and the settlement BOP display token.
- Hidden-route gate and focus-refresh search.
- Strict UTF-8/BOM and malformed-line checks for the YML, plus strict UTF-8 checks for relevant script files.

Skipped meaningful validation:

- No live HOI4 engine parse, GUI click-through, or focus-tree render was available in this session. The remaining issues concern runtime state transitions and cannot be proven from static localisation coverage alone.
- No gameplay, asset, or design changes were made, so balance and asset validation were outside scope.

Remaining risks:

- The first-match scripted-localisation bug may display the wrong Northern failure label.
- The plebiscite branch and concealed-evidence status values may remain permanently on fallback/zero states.
- Event/flavour BOP text may not resolve its temporary variable outside the originating effect chain.
- Concealed route names may fail to appear after unlock if the focus layout is not refreshed.
- GUI review/inspection flags may accumulate without a consumer even where the Northern review effect itself runs.

No requested audit surface was omitted; the unresolved items above are explicit gameplay/runtime blockers, not localisation coverage simplifications.
