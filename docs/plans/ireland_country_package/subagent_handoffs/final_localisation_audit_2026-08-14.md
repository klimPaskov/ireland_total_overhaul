# Final Ireland country-package localisation audit

Date: 2026-08-14  
Scope: current Ireland package after `f7e5e64`, `317ce37`, and `439e5d4`.

## Outcome

The requested focus, decision/mission, event, scripted-localisation, Parliament GUI, advisor, company, MIO, and report-event surfaces have resolving, non-empty English localisation in the current worktree. No gameplay files were edited by this audit. Eight narrow wording fixes were made in `localisation/english/ireland_l_english.yml`; the parent agent owns review and commit.

The worktree also contains concurrent changes outside this audit, including gameplay files, `thumbnail.png`, and another decision/mission handoff. Those changes were preserved. The same English localisation file contains concurrent edits by other work; the eight keys listed below are the only keys changed by this localisation audit.

## Coverage evidence

- The two mod English localisation files contain 5,911 unique actual keys; no duplicate actual keys or empty values were found in the current scan.
- Both mod English files begin with UTF-8 BOM bytes: `localisation/english/ireland_l_english.yml` and `localisation/english/ireland_game_rules_l_english.yml`.
- `common/national_focus/ireland_focus_tree.txt` contains 218 current focus IDs. Every focus title and `_desc` resolves. The 199 `custom_effect_tooltip` references (198 unique) resolve, as do the six focus `tooltip =` trigger assignments and the company/MIO tooltip references used by focus rewards.
- The P0 postwar category currently contains 26 one-level action/mission blocks. Names, descriptions, and direct/block custom effect tooltips resolve. The P0 text matches the current one-factory settlement/recovery projects and their 180-day/120-day durations; the vanilla `decision_cost_civ_factory_1` key is present in the vanilla English localisation and is intentionally not duplicated in the mod.
- The P1 territorial policy category currently contains 28 one-level action/mission blocks. Names, descriptions, requirements, and direct/block custom effect tooltips resolve. Audited values include 50 Political Power/70 days for the border claim, 180 days for the resulting war goal, 25 Political Power/35 days for method and review actions, 15 Political Power/35 days or one Civilian Factory/120 days for recovery actions, the 180-day/240-day territorial missions, the 180-day cooldown, and the 365-day Atlantic mission. Their described transfer, claim, core, factory, equipment, manpower, stability, war-support, and ledger outcomes match the source effects.
- `events/ireland_country_conclusion_events.txt` `.1`–`.5`, `events/ireland_territorial_diplomacy_events.txt` `.1`–`.27` (including `.25`–`.27`), and `events/ireland_public_conclusion_events.txt` `.432`/`.433` all have resolving titles, descriptions, options, and effect tooltips. The combined event scan found 3,182 localisation references (3,152 unique) with no missing mod-localised reference. Provincial Assent `.25`–`.27` correctly describe recording/adjournment and the absence of territorial, core, factory, equipment, or unit grants where the source has none.
- `common/scripted_localisation/ireland_localisation.txt` and `common/scripted_localisation/ireland_coastwatch.txt` contain 40 defined-text names and 121 `localization_key` outputs. All output keys resolve to non-empty text, and all scanned `GetIreland...` references resolve to a defined helper. The active territorial method/status chain remains method-gated; no hidden route text leakage was found.
- `interface/ireland_parliament_scripted_gui.gui` has 24 current text/button/tooltip references, all resolving. Parliament status/composition helpers and live requirement lines are present. The four current button tooltips now state their fixed outcomes: Dáil +1 routine vote/+4 Mandate/+2 Cohesion/+2 Social Consent; Seanad +2 government seats/+3 Social Consent/+2 Cohesion; Confidence one external-support vote when absent, then +2 routine votes/+5 Mandate/+4 Social Consent/+3 Cohesion; Joint Budget +5% Stability/+5 Administrative Reach/+8 Mandate/+5 Cohesion.
- The 45 advisor `idea_token` name keys in `common/characters/ireland_route_characters.txt` resolve; literal character names are source text rather than missing localisation references. The seven industrial-company names and descriptions in `common/ideas/ireland_industrial_concerns.txt` resolve. The two organisation and five initial/add-trait name keys in `common/military_industrial_organization/organizations/ireland_organizations.txt` resolve.

## Missing keys

None found in the audited current scope after the narrow fixes.

Intentional vanilla fallbacks verified:

- `decision_cost_civ_factory_1` is supplied by vanilla English localisation.
- The two `available_mio_tt` references used by focus rewards are supplied by vanilla English localisation.

## Duplicate and empty-key list

- Duplicate actual keys: none (5,911 unique current mod-English keys).
- Empty values: none.

## Scripted-localisation issue list

No broken or missing scripted-localisation output was found. Seven defined-text helpers currently have no active source/interface reference in the scan:

- `GetIrelandAchievementA22Status`
- `GetIrelandAchievementA27Status`
- `GetIrelandAchievementA28Status`
- `GetIrelandConditionsSelection`
- `GetIrelandLawReviewStatus`
- `GetIrelandNorthernFailureState`
- `GetIrelandNorthernRegion`

These appear to be retained or future/legacy UI surfaces, not broken outputs; do not remove them without an owner decision.

## Dynamic-text opportunities

- The active Parliament GUI uses dynamic stage, ownership, completion, majority, and Political Power status helpers. The older unreferenced `ireland_parliament_power_dail_tt`, `ireland_parliament_power_seanad_tt`, `ireland_parliament_power_confidence_tt`, and `ireland_parliament_power_budget_tt` remain broad static copies. They can be retired or made dynamic if a later GUI cleanup explicitly owns those keys.
- The seven unused defined-text helpers above can be reconciled with their intended achievement/law/conditions/Northern UI owners in a later cleanup.
- P0/P1 durations and costs are currently stated exactly against the source constants. If those constants become tunable, expose the live values through dynamic localisation or update the wording in the same change.
- No new dynamic localisation was required by this audit; existing dynamic outputs were validated rather than duplicated.

## Cross-surface mismatch notes

The following directly evidenced clarity mismatches were corrected:

1. P0 settlement/recovery requirement text said “the displayed duration” without stating the current 180/120-day project duration.
2. Parliament button tooltips named broad result categories without their fixed ledger deltas.
3. Workers Border Campaign rebuild text omitted its three source-side `+3` changes to Northern Nationalist Consent, Social Consent, and Labour Cooperation.
4. Provincial Assent reconvene requirements said only that consent/legitimacy had to improve, while the source trigger uses 25 Northern Unionist Consent, 50 Northern Nationalist Consent, or 55 Royal Legitimacy.

No unresolved event-title/description/option/effect mismatch was found in the conclusion or territorial `.25`–`.27` surfaces. No raw trigger text or prematurely revealed route label was found in the active scripted-localisation chain.

## Files and keys changed by this audit

Only `localisation/english/ireland_l_english.yml` was intentionally edited. The eight changed keys are:

- `ireland_postwar_family_settlement_requirements_tt` — “displayed duration” changed to “Reserve 1 Civilian Factory for 180 days.”
- `ireland_postwar_family_recovery_requirements_tt` — “displayed duration” changed to “Reserve 1 Civilian Factory for 120 days.”
- `ireland_parliament_dail_button_tt` — added exact no-cost +1/+4/+2/+2 outcomes.
- `ireland_parliament_seanad_button_tt` — added exact +2/+3/+2 outcomes.
- `ireland_parliament_confidence_button_tt` — added the conditional external-support-vote result and exact +2/+5/+4/+3 outcomes.
- `ireland_parliament_budget_button_tt` — added exact +5%/+5/+8/+5 outcomes.
- `ireland_territorial_rebuild_workers_border_campaign_desc` — added the three +3 ledger changes before campaign relaunch.
- `ireland_territorial_reconvene_provincial_assent_requirement_tt` — replaced vague improvement wording with the three exact OR thresholds.

Before/after behavior: players previously saw broad or incomplete requirements/results; they now see the current source cost/duration/threshold/outcome text while the underlying gameplay remains unchanged. No scripted-localisation helper was added or changed.

## Encoding and validation

Task-specific checks included key extraction and duplicate/empty-value scanning across both mod English files, BOM byte checks, focus ID/title/description/reward reference coverage, P0/P1 action/mission reference coverage, event reference coverage, scripted-localisation output/reference resolution, Parliament GUI reference coverage, and advisor/company/MIO key checks. The current localisation scan reports 5,911 unique non-empty keys and BOM on both files.

No full game load or in-game GUI raster/render validation was run: this was a source-level localisation audit, no gameplay was changed, and no game session or engine diagnostic artifact was available. The offline wiki, vanilla localisation/scripted-GUI documentation, and vanilla `decision_cost_civ_factory_1` precedent were consulted as required.

## Unresolved wording decisions

- The existing P0 alternate-order wording says “after 1 January 1946,” matching the source’s `date > 1946.1.1` gate in plain language; no change was needed.
- The four unreferenced Parliament power tooltip copies and seven unreferenced defined-text helpers should remain until their ownership/retirement is decided.
- No broader prose rewrite was made for style; only source-evidenced clarity corrections were applied.

Handoff path: `docs/plans/ireland_country_package/subagent_handoffs/final_localisation_audit_2026-08-14.md`
