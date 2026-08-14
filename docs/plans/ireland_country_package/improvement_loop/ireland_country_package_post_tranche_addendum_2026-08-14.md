# Ireland Country Package Post-Tranche Improvement Addendum

Date: 2026-08-14

Status: accepted and promoted; P0 implementation in progress

Owner after acceptance: parent implementation agent

## Decision

The country package is not ready for closure. The current implementation is mechanically broad and the three latest tranches closed important gaps, including the connected National Question lane, real territorial response chains, real industrial capacity reservations, material enforcement costs, O'Duffy late AI, and Northern outcome gates. The remaining work is narrower and highly visible:

- the five public political families do not read as one centered choice surface
- the Atlantic conclusion currently requires all three settlement-policy focuses even when one lawful policy resolves every relevant holding
- blocked and failed route conclusions are archived by the same terminal helper used for successful conclusions
- the generic postwar suite can close a campaign without a family-specific 1946 to 1951 settlement
- democratic, Congress, fascist, and restoration territorial methods lack recovery surfaces equivalent to the implemented Belfast Compact reopening
- several Atlantic focuses still pay arbitrary stability or equipment alongside their actual capability unlock

This addendum defines one bounded player-facing tranche, followed by two ranked implementation tranches. It does not reopen the completed response-chain or industrial-contract work.

Current-source baseline:

- `f5c7d6a`: National Question campaign, Wales and Cornwall response chains and art, enforcement costs, O'Duffy late AI
- `1b81be0`: nine industrial contracts reserve real civilian factory capacity
- `caf02d8`: route-specific Northern outcome gates and Belfast Compact recovery

Current gameplay source and `implementation_matrix.md` are authoritative. Older 188-focus and 215-focus reports are not evidence for this pass.

## Prior addendum disposition

No earlier country-package improvement-loop addendum is unresolved. Earlier focus-tree plans are recorded as implemented, promoted, or superseded in the country-package planning records. This file becomes the sole open improvement addendum for this gap.

If accepted, keep this file under `docs/plans/ireland_country_package/improvement_loop/` until the first tranche is implemented and audited. Then promote the accepted contracts into the country-package specs listed in the promotion section.

## Evidence from the current implementation

### Focus layout evidence

The current `ireland_focus_tree` contains 218 focuses and 226 connectors. Read-only focus inspection found no connector crossings, no node intersections, and no long connectors. It also found:

- layout bounds from x = -42 to x = 21
- a bounding-center offset of 21 half-columns
- one `FOCUS_LAYOUT_LINEAR_DETOUR` from `ireland_clerical_failure_bridge` to `ireland_clerical_guardianship`
- five family commitments at four different depths:
  - `ireland_republican_government`, x = -16, y = 4
  - `ireland_congress_reform_bridge`, x = -12, y = 3
  - `ireland_vocational_constitution`, x = -8, y = 7
  - `ireland_oduffy_network_revival`, x = -6, y = 10
  - `ireland_high_king_evidence_gate`, x = -4, y = 4

The topology is valid, but the family choice does not present as one readable band beneath `ireland_national_settlement` at x = -12, y = 1.

### Territorial evidence

`common/national_focus/ireland_focus_tree.txt` now has the connected chain from `ireland_unfinished_national_question` through `ireland_authorise_reunification_instruments`, followed by five family methods and five route resolutions. Current operations include Ulster, Highlands, Wales, Cornwall, rights charters, protectorates, reconstruction obligations, and an integration review.

The remaining structural defect is at `ireland_atlantic_settlement_concluded`. It has three separate prerequisite blocks:

- `ireland_local_rights_charter`
- `ireland_protectorate_statutes`
- `ireland_integration_review_commission`

Separate prerequisite blocks are an AND. The current focus therefore requires all three policy focuses. The scripted trigger `ireland_atlantic_settlement_all_relevant_resolved` already owns the correct per-holding resolution test, so the AND is unnecessary and contradicts the per-holding choice model.

### Conclusion evidence

`ireland_finalize_route_conclusion` in `common/scripted_effects/ireland_effects.txt` records full, partial, blocked, and failed results. It then sets `ireland_route_closed` and `ireland_route_archived` for all four results. Blocked and failed outcomes therefore become terminal instead of opening recovery.

The postwar category already includes emergency review, rationing, veterans, merchant shipping, reconstruction, the republic question, Commonwealth relations, United Nations admission, aid, and five missions. Those systems should be retained. The gap is the terminal family settlement, not another generic postwar checklist.

## Ranked implementation tranches

| Rank | Tranche | Player-visible impact | Scope |
| --- | --- | --- | --- |
| P0 | Five Families Survive the Peace | Highest | family-band layout, Atlantic prerequisite correction, non-terminal failure, five family settlements, five conclusion reports |
| P1 | Recover the National Question | High | four missing territorial recovery surfaces, preservation of the existing Belfast Compact recovery, territorial status text |
| P2 | Make Every Focus Pay for a Capability | Medium | remove arbitrary Atlantic rewards, add outcome accounting, finish art and AI validation |

P0 is the bounded next tranche. P1 and P2 must remain queued until P0 is implemented, promoted, or rejected with a reason.

## P0: Five Families Survive the Peace

### 1. Reflow the public family choice

Edit surface: `common/national_focus/ireland_focus_tree.txt`

The public choice must become one centered two-row band under `ireland_national_settlement`. Preserve all five existing commitment IDs. Do not add navigation focuses.

Required band order from left to right:

1. democratic: `ireland_republican_government`
2. Congress socialist: `ireland_congress_reform_bridge`
3. producer-estate: `ireland_vocational_constitution`
4. Blueshirt: `ireland_oduffy_network_revival`
5. restoration: `ireland_high_king_evidence_gate`

Layout constraints:

- every commitment must be at y = 3 or y = 4
- the average x position of the five commitments must be within two columns of `ireland_national_settlement`
- adjacent commitments must be at least two columns apart
- no commitment may sit below any of its first profile, economy, security, diplomacy, Northern-method, recovery, or conclusion descendants
- `allow_branch = { has_country_flag = ireland_political_routes_revealed }` remains on all five commitments
- each commitment must have a visible prerequisite connector from `ireland_national_settlement` or from one public constitutional survey directly beneath it
- evidence and crisis flags may remain in `available`, but they must not conceal the branch
- preserve the three existing shortcuts and do not add a fourth shortcut

Use the read-only inspector and renderer after reflow. The implementation agent may use `hoi4.focus_rewrite` for the layout pass, but the rewrite must be limited to coordinates, `relative_position_id`, and the five public prerequisite connectors. It must not rewrite rewards, route locks, or identifiers.

Known collision and detour IDs that the reflow must explicitly resolve:

- `ireland_organise_congress`
- `ireland_clerical_failure_bridge`
- `ireland_clerical_guardianship`
- `ireland_otherworld_investigation`
- `ireland_cultural_evidence_ledger`
- `ireland_close_oduffy_chapter`

Straighten `ireland_clerical_failure_bridge -> ireland_clerical_guardianship` by placing both nodes on the same x coordinate. Preserve their prerequisite and route semantics.

Suggested stable anchor contract:

```text
ireland_national_settlement
  -> democratic commitment
  -> Congress commitment
  -> producer-estate commitment
  -> Blueshirt commitment
  -> restoration commitment
```

The renderer decides the final collision-free x coordinates. The numerical acceptance constraints above are authoritative.

### 2. Correct the Atlantic conclusion prerequisite

Edit surface: `common/national_focus/ireland_focus_tree.txt`

Replace the three separate prerequisite blocks on `ireland_atlantic_settlement_concluded` with one prerequisite block containing:

- `ireland_local_rights_charter`
- `ireland_protectorate_statutes`
- `ireland_integration_review_commission`

Multiple focuses inside one prerequisite block are an OR. Keep `ireland_atlantic_settlement_all_relevant_resolved = yes` in `available`. This produces the intended rule:

- one policy focus is enough when it resolves every relevant holding
- two or three policy focuses remain available when different holdings need different outcomes
- the conclusion cannot complete while any controlled holding or protectorate obligation remains unresolved

Do not add cores. Do not make all three policy focuses mutually exclusive.

### 3. Make failed conclusions recoverable

Edit surfaces:

- `common/scripted_effects/ireland_effects.txt`
- `common/scripted_triggers/ireland_triggers.txt`
- `common/decisions/ireland_decisions.txt`
- `common/script_constants/ireland_constants.txt`

Split `ireland_finalize_route_conclusion` into evaluation and archival:

- retain `ireland_finalize_route_conclusion` as the evaluator
- add `ireland_archive_successful_route`
- add `ireland_open_family_conclusion_recovery`
- add `ireland_postwar_foundation_ready`
- add `ireland_family_postwar_settlement_complete`

Full and partial outcomes:

- require `ireland_family_postwar_settlement_complete`
- record the durable route-specific conclusion flag
- dispatch the matching family conclusion event
- archive only after the conclusion event option calls `ireland_archive_successful_route`

Blocked and failed outcomes:

- do not set `ireland_route_closed`
- do not set `ireland_route_archived`
- set `ireland_conclusion_recovery_open`
- preserve every named blocked-surface flag
- dispatch the matching family conclusion event in its recovery state
- allow another 180-day conclusion review only after the family recovery action completes

`ireland_postwar_foundation_ready` must require all of the following:

- date after 1946.1.1
- Ireland is not at war, or the recorded major war has ended
- `ireland_action_review_the_emergency_declaration_complete`
- full or partial result for `ireland_mission_end_wartime_rationing_safely`
- full or partial result for `ireland_mission_settle_the_demobilised_forces`
- full or partial result for `ireland_mission_complete_national_reconstruction`
- a recorded republic or Commonwealth settlement through `ireland_mission_bring_the_republic_settlement_into_force`
- a recorded United Nations admission attempt through `ireland_mission_build_support_for_united_nations_admission`, or an explicit alternate-order resolution when United Nations admission is not a valid world-state path
- no active route-review critical mission

The date opens the postwar era. It does not replace the material requirements.

### 4. Add five family settlement actions

Edit surface: `common/decisions/ireland_decisions.txt`, inside `ireland_postwar`

These are one-time 180-day projects. Each uses one civilian factory through `modifier = { civilian_factory_use = 1 }`. Each is visible only for its family, requires `ireland_postwar_foundation_ready`, and sets the shared `ireland_family_postwar_settlement_complete` flag on completion.

| Family | New action ID | Required route proof | Institutional result |
| --- | --- | --- | --- |
| Democratic | `ireland_action_ratify_the_postwar_republic` | `ireland_family_democratic` and a democratic capstone | records coalition or Fianna Fáil constitutional continuity, settles Republic Act or association status, and unlocks the final review |
| Congress | `ireland_action_civilianise_the_workers_congress` | `ireland_family_communist` and plural or vanguard capstone | records civilian congress supremacy, closes wartime command bodies, and unlocks the final review |
| Blueshirt | `ireland_action_place_the_directorate_under_statute` | `ireland_family_fascist` and personal or corporate capstone | chooses a bounded statutory directorate or demobilised corporate state, closes temporary mobilisation authority, and unlocks the final review |
| Producer-estate | `ireland_action_convert_contracts_to_reconstruction_credit` | `ireland_family_oligarchic` and vocational or producer capstone | converts completed industrial contracts into a dated reconstruction ledger, records creditor obligations, and unlocks the final review |
| Restoration | `ireland_action_define_the_postwar_crown` | `ireland_family_restoration` and High King capstone | records constitutional crown, provincial council, or abdication settlement, closes temporary crown authority, and unlocks the final review |

These projects must not grant free factories, equipment, cores, or generic stability. Their payoff is institutional transformation and access to the terminal report.

Add five matching recovery actions. They are visible only when `ireland_conclusion_recovery_open` and the matching family is active:

- `ireland_action_reconstitute_the_postwar_coalition`
- `ireland_action_reconvene_the_workers_congress`
- `ireland_action_demobilise_the_failed_directorate`
- `ireland_action_rebalance_the_producer_estates`
- `ireland_action_reconvene_the_crown_council`

Recovery actions run for 120 days and use one civilian factory. They must repair their named family failure, set `ireland_family_conclusion_recovery_complete`, clear only the relevant blocked-surface flags, clear `ireland_conclusion_recovery_open`, and call `ireland_begin_conclusion_review`. They must not erase durable failure history.

### 5. Add five terminal family reports

New event file: `events/ireland_country_conclusion_events.txt`

Namespace: `ireland_country_conclusion`

| Event | Family | Triggered by |
| --- | --- | --- |
| `ireland_country_conclusion.1` | democratic | final evaluation with `ireland_family_democratic` |
| `ireland_country_conclusion.2` | Congress | final evaluation with `ireland_family_communist` |
| `ireland_country_conclusion.3` | Blueshirt | final evaluation with `ireland_family_fascist` |
| `ireland_country_conclusion.4` | producer-estate | final evaluation with `ireland_family_oligarchic` |
| `ireland_country_conclusion.5` | restoration | final evaluation with `ireland_family_restoration` |

Each report has result-specific options:

- full: records the family settlement and calls `ireland_archive_successful_route`
- partial: records the compromise, preserves the partial-history flag, and calls `ireland_archive_successful_route`
- blocked or failed: explains the named blocked surfaces and opens the matching recovery action without archiving

Do not set `fire_only_once`. A failed review can return after recovery. Guard successful variants with durable family report flags so a successful report cannot repeat.

Temporal variants:

- 1946 to 1947 reports frame the result as reconstruction and constitutional preparation
- the democratic report after 1948.4.17 can reference the enacted Republic settlement or continued external-association compromise according to the recorded mission outcome
- 1948 to 1951 reports frame the result as the settled postwar order
- reports after 1951 remain playable and use an overdue-settlement variant, but do not invent a hard failure or remove the recovery path

The date variants are presentation and historical framing. Material result flags remain authoritative.

Event cadence contract:

- dispatch directly from `ireland_finalize_route_conclusion`
- do not add an on-daily or world-country scan
- do not put these reports in the monthly flavour candidate pool
- do not fire more than one family conclusion report per evaluation
- recovery re-evaluation is paced by the existing 180-day conclusion review

### 6. Postwar tuning constants

Edit surface: `common/script_constants/ireland_constants.txt`

Add these keys to the existing `ireland` category:

```text
postwar_family_settlement_days = 180
postwar_family_recovery_days = 120
postwar_family_factory_use = 1
postwar_family_review_days = 180
```

Use the existing action-burden and AI score constants. Do not add per-action magic numbers.

### 7. P0 AI behavior

Edit surfaces:

- `common/ai_strategy/ireland_ai_strategy.txt`
- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`
- `common/scripted_effects/ireland_runtime.txt`
- `common/scripted_triggers/ireland_triggers.txt`

Required behavior:

- family settlement actions become critical when a capstone is complete and `ireland_postwar_foundation_ready` is true
- recovery actions receive `constant:ireland.ai_recovery_bonus`
- the final conclusion action receives `constant:ireland.ai_route_conclusion_bonus` only after the family settlement action is complete
- historical AI retains factor 0 on coercive territorial focuses and decisions
- democratic historical AI prefers `ireland_atlantic_security_compacts` and a rights-charter settlement
- Congress AI prefers `ireland_republics_across_the_channel` and non-annexation support
- producer-estate AI prefers `ireland_atlantic_concessions` and protectorate or commercial settlements
- restoration AI may claim the Highlands only with the current evidence, strength, and readiness gates
- O'Duffy AI may use coercive options only with historical focuses off and all current material gates satisfied
- blocked AI must choose recovery before any optional postwar action

The focus plans already list the Atlantic focuses. Update their focus weights only where the OR conclusion prerequisite changes the valid endpoint. Do not duplicate decision scoring inside strategy plans.

## P1: Recover the National Question

This tranche fills four missing recovery surfaces. The existing `ireland_territorial_reopen_belfast_compact` is the producer-estate recovery and must remain the canonical implementation.

Edit surfaces:

- `common/decisions/ireland_expansion_decisions.txt`
- `common/decisions/ireland_decisions.txt`
- `common/scripted_effects/ireland_effects.txt`
- `common/scripted_triggers/ireland_triggers.txt`
- `events/ireland_territorial_diplomacy_events.txt`
- `common/script_constants/ireland_constants.txt`

### Democratic recovery

Add `ireland_territorial_reopen_supervised_plebiscite`.

Reveal when:

- `ireland_territorial_method_democratic`
- `ireland_mission_conduct_a_supervised_plebiscite_failure_recorded` or cancellation recorded
- no plebiscite mission is active
- no territorial diplomacy request is active

Completion:

- preserve failure history
- set `ireland_territorial_plebiscite_reopened`
- clear only the action lock that prevents relaunch
- relaunch the existing `ireland_mission_conduct_a_supervised_plebiscite` through the existing capacity trigger
- apply a 180-day route-specific cooldown

Partial plebiscite success remains a valid input for `ireland_settlement_under_law` and does not need recovery.

### Congress recovery

Replace the guaranteed completion of `ireland_territorial_workers_border_campaign` with a mission-backed campaign:

- launcher retains ID `ireland_territorial_workers_border_campaign`
- new mission ID `ireland_mission_sustain_the_workers_border_campaign`
- 180-day duration
- full result requires the current social-consent and Northern-nationalist thresholds
- partial result remains usable by `ireland_all_island_workers_republic`, but marks the route partial
- failure opens `ireland_territorial_rebuild_workers_border_campaign`

The recovery decision consumes one civilian factory for 120 days, restores civilian organisers, and relaunches the mission. It must not create equipment or political power.

### Fascist recovery

Add `ireland_territorial_withdraw_border_enforcement`.

Reveal when:

- ultimatum refusal or rejected counteroffer is recorded
- `ireland_territorial_border_enforcement_open`
- readiness later falls below the enforcement gate, the target becomes an ally or faction partner, or the target controller ceases to be valid
- no war goal has been issued

Completion:

- clears pending demand and diplomacy targets
- does not refund consumed reserves
- sets `ireland_territorial_fascist_enforcement_withdrawn`
- opens the non-annexation Atlantic-security exit
- records a partial territorial conclusion

This is a recovery from an invalid coercive path. It is not a second ultimatum.

### Restoration recovery

Convert `ireland_territorial_convene_provincial_assent` from guaranteed assent into an explicit domestic response event:

- `ireland_territorial_diplomacy.25`: Provincial Assent convened
- `ireland_territorial_diplomacy.26`: assent recorded
- `ireland_territorial_diplomacy.27`: convention adjourned

Outcome weights use Northern unionist consent, nationalist consent, crown legitimacy, and administrative reach. The historical AI cannot force assent.

Add `ireland_territorial_reconvene_provincial_assent` after adjournment. It consumes one civilian factory for 120 days, requires improved consent or legitimacy, preserves the first adjournment record, and fires `.25` again.

### Territorial status text

Add scripted localisation for the existing `ireland_territorial_policy` category description. It must show:

- current family method
- current target or holding
- active response or cooldown
- recorded refusal, partial result, or recovery state
- unresolved Highlands, Wales, Cornwall, Scottish protectorate, or Welsh protectorate obligation
- next valid action

Use `localisation/english/ireland_scripted_localisation_l_english.yml` or the repository's existing dynamic-text file. Do not add a scripted GUI.

## P2: Make Every Focus Pay for a Capability

Edit surface: `common/national_focus/ireland_focus_tree.txt`

Remove rewards that are unrelated to the focus action:

- remove generic stability from `ireland_atlantic_security_compacts`
- remove the free support-equipment delivery from `ireland_republics_across_the_channel`
- remove generic stability from `ireland_atlantic_concessions`
- remove generic stability from `ireland_postwar_settlement_office`
- remove generic stability from `ireland_local_rights_charter`
- remove generic stability from `ireland_atlantic_settlement_concluded`

Keep or strengthen these concrete payoff classes:

- `ireland_atlantic_security_compacts`: unlocks basing negotiation
- `ireland_republics_across_the_channel`: unlocks Welsh and Scottish republican support operations, with material costs on those operations
- `ireland_gaelic_marches`: claim plus gated Highlands demand
- `ireland_atlantic_concessions`: unlocks commercial basing and concession operations
- `ireland_dal_riata_claim`: claim plus gated Highlands demand
- `ireland_postwar_settlement_office`: opens the settlement mission and per-holding policies
- `ireland_local_rights_charter`: unlocks rights operations
- `ireland_protectorate_statutes`: unlocks release and reconstruction obligations
- `ireland_integration_review_commission`: unlocks compliance-gated review
- `ireland_atlantic_settlement_concluded`: closes all resolved obligations and mission capacity through a new helper `ireland_finalize_atlantic_settlement`

`ireland_finalize_atlantic_settlement` records which holdings used rights, protectorate, withdrawal, or integration. It applies no free cores and no generic resource reward.

## Asset handoff

No new focus icons are required because the family-band pass reuses existing focus IDs.

Create distinct static decision icons for the ten new P0 settlement and recovery actions. Register them in `interface/ireland_decision_icons.gfx` and place final DDS files under `gfx/interface/goals/decisions/ireland/`.

Create five report images:

- `GFX_report_event_ireland_postwar_democratic_settlement`
- `GFX_report_event_ireland_postwar_congress_settlement`
- `GFX_report_event_ireland_postwar_blueshirt_settlement`
- `GFX_report_event_ireland_postwar_producer_estates_settlement`
- `GFX_report_event_ireland_postwar_restoration_settlement`

Asset source rules:

- use sourced archival material for the democratic Republic Act or inter-party setting when a verified public-domain or licensed source is available
- use generated alternate-history report art for Congress, Blueshirt, producer-estate, and restoration outcomes
- do not generate a likeness of a real leader when a sourced portrait or photograph is required
- record source, crop, processing, and licence status in the country-package asset manifest

Animation is out of scope. These are discrete decisions and terminal reports. Static icons and reports communicate their state without adding a new visual system.

## Localisation direction

Localise every new action, mission, event, trigger tooltip, outcome, cancellation, and recovery state in the existing English country-package files. Provide wording direction, not implementation-history text.

Player-facing text must distinguish:

- a full family settlement
- a compromise settlement
- a named blocked surface
- a failed settlement with a lawful recovery path
- territorial refusal from an invalid target or a material-readiness collapse

Do not describe values as caps, gates, hardcoded limits, or reworked mechanics.

## Historical and regional basis

The design is grounded in the accepted country-package research:

- rural electrification begins in 1946 and belongs in postwar reconstruction rather than an early free-factory reward
- the first inter-party government in 1948 supports a democratic coalition settlement
- the Republic of Ireland Act 1948 supports a dated republic and association decision
- Ireland's immediate postwar United Nations applications support an active admission attempt with an alternate-order resolution when the organisation is unavailable
- Irish Shipping, founded in March 1941, supports a merchant-fleet handoff into reconstruction
- emergency-law rollback, housing, migration, welfare, and export policy belong in the postwar foundation before archival
- Northern consent, provincial institutions, and British flexibility remain more appropriate inputs than automatic cores

No new historical claim is introduced by this addendum. Alternate family conclusions are design extrapolations and must be presented as alternate history.

## Vanilla and engine precedents

Implementation must continue to mirror:

- vanilla focus prerequisite semantics from National Focus modding documentation
- decision mission lifecycle fields from vanilla `common/decisions/ENG.txt` and `common/decisions/ITA.txt`
- country event targeting and cleanup from vanilla `events/MTG_USA.txt` and `events/BFTB_Turkey.txt`
- official `script_concept_documentation.md`, especially Script Constants
- official effects and triggers documentation for decision activation, country events, event targets, date triggers, idea swaps, and state control

The implementation must not introduce a whole-world daily, weekly, or monthly scan.

## Acceptance tests

### Layout

- exactly 218 focuses remain unless another accepted tranche deliberately adds content
- all five family commitments are visible after `ireland_national_settlement`
- all five commitments sit at y = 3 or y = 4
- the commitment band average x is within two columns of `ireland_national_settlement`
- no crossing, intersection, duplicate-position, long-connector, or linear-detour diagnostic remains
- three shortcuts remain

### Atlantic settlement

- one policy focus can lead to `ireland_atlantic_settlement_concluded` when every relevant holding is resolved by that policy
- mixed holdings can use two or three policy focuses
- an unresolved controlled holding blocks conclusion
- an unresolved protectorate reconstruction obligation blocks conclusion
- no external holding receives an automatic core

### Postwar conclusion

- no family can conclude before 1946.1.2
- each family has a distinct 1946 to 1947 preparation variant, a 1948 to 1951 settlement variant, and a post-1951 overdue variant
- no family can conclude while its required postwar missions are missing
- each family has one distinct settlement action and one distinct recovery action
- full and partial outcomes archive only after the family report option
- blocked and failed outcomes remain playable and expose recovery
- a recovered route waits another 180 days before re-evaluation
- a successful report cannot repeat
- a failed report can return once after recovery

### Territorial recovery

- failed democratic plebiscite can be prepared and relaunched
- partial democratic plebiscite remains valid without recovery
- Congress campaign can produce full, partial, and failed records
- Belfast Compact uses the existing reopening decision
- fascist enforcement can be withdrawn when its target or readiness becomes invalid before a war goal
- restoration assent can adjourn and be reconvened
- no recovery refunds consumed material reserves

### AI

- historical AI never selects coercive expansion
- each nonhistorical family completes its own postwar settlement before conclusion
- blocked AI selects recovery before optional work
- AI does not start a settlement or recovery action without one free civilian factory
- AI resolves Atlantic obligations instead of idling on the conclusion focus

Run named scenarios for democratic historical, Congress nonhistorical, O'Duffy nonhistorical, producer-estate nonhistorical, and restoration nonhistorical. Use probability inspection for event option weights before claiming balance completion.

## Scope stop

Do not add:

- a sixth public political family
- another focus-tree shortcut
- a scripted GUI for territorial or postwar status
- automatic external cores
- Isle of Man state content
- a new music or voice package
- animated decision icons or animated report art
- another generic postwar event pool

Those additions would add surface area without repairing the current player-facing gaps.

## Promotion into source specs

If accepted and implemented, merge:

- family-band and conclusion contracts into `docs/specs/ireland_country_package/campaign_architecture.md`
- Atlantic prerequisite and recovery contracts into `docs/specs/ireland_country_package/territorial_campaign.md`
- postwar foundation and five family settlements into `docs/specs/ireland_country_package/economy_defence_and_statecraft.md`
- event, mission, and cleanup lifecycle into `docs/specs/ireland_country_package/systems_and_lifecycles.md`
- AI, tuning, asset, and test contracts into `docs/specs/ireland_country_package/ai_balance_assets_and_text.md`
- final disposition and implementation evidence into `docs/specs/ireland_country_package/implementation_matrix.md`

Until that promotion occurs, this addendum remains a plan and is not implementation evidence.
