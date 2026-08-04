# Ireland decisions, missions, and GUI re-audit — 2026-07-18

Status reconciliation (2026-07-22): category counters, critical-slot reservation, and selected/last-reviewed GUI projections are structurally implemented, but not proven in a live engine session. Shared escalation telemetry remains queued: the source sets family-level escalation flags but does not yet consume the shared `mission_result_escalated` metric. Reusable dynamic cost/availability tooltip presentation is also queued. Evidence and current ownership are tracked in `docs/plans/ireland_focus_tree/source_of_truth_map.md` and `docs/plans/ireland_focus_tree/audits/ireland_completion_followup_2026-07-18.md`.

## Scope and result

This re-audit compares the current Ireland sources with `docs/specs/ireland_focus_tree/`, especially the decision-and-mission map and Part 5 lifecycle contract. It covers the thirteen category surface, 140 actions, 54 mission families, 8/10/12 capacity rules, dynamic Command Power, failure/escalation, AI, cleanup, localisation, and the three decision-owned scripted GUI panels.

Two contained defects were patched. The surface is **not ready for final sign-off** because the declared per-category caps and critical-slot reservation are not represented by the current runtime counters, and escalation is not recorded by the shared result metric.

Custom subagent routing was reviewed with `hoi4-subagents`; this session does not expose a project subagent-spawn tool, so no `fork_context` value could be supplied. The audit was completed directly.

## Exact inventory and category lifecycle

The current source contains exactly **13 categories**, **140 actions**, and **54 mission families**. No decision or mission identifier is duplicated.

| Category | Actions | Missions | Specified concurrent cap | Lifecycle assessment |
| --- | ---: | ---: | --- | --- |
| Settlement Government | 10 | 3 | 2 | Dublin constitutional review, confidence, and settlement closure; visible from campaign opening. |
| Elections and Coalitions | 10 | 3 | 2 | Opens through election, dissolution, formation, or plebiscite gates. |
| Organised Society | 10 | 3 | 2 | Opens through society, labour, education, or rural organisation gates. |
| Cultural and Archival Work | 10 | 3 | 2 | Opens through culture, archive, or hidden-evidence gates. |
| Radical and Underground Transition | 10 | 0 | 2 | Correctly has no timed mission family in the current mapping. |
| National Provision | 16 | 10 | 3 routine / 4 emergency | Persistent material lane. |
| National Readiness | 14 | 8 | 3 routine / 4 war or invasion | Persistent defence lane. |
| Neutrality and Incidents | 10 | 4 | 2 routine / 3 direct incident | Date and spillover gated. |
| Foreign Statecraft | 10 | 4 | 2 | Channel-gated diplomatic lane. |
| Northern Settlement | 10 | 4 | 3 | Contact, negotiation, plan, or stage-review gated. |
| Occupation and Integration | 10 | 4 | 3 | Control and integration lifecycle gated. |
| Regional and External Orders | 10 | 3 | 2 | Regional-order and route gates. |
| Postwar Settlement | 10 | 5 | 3 | Emergency-review, transition, war-end, or 1945 gate. |

All 140 actions have `visible`, `available`, `ai_will_do`, and an IRE guard. All 54 missions have `available`, a deadline, cancellation, timeout, completion, AI weighting, full/partial/failure feedback, an individual active flag, and route-cleanup cancellation.

The global cap itself is correctly centralised in `common/script_constants/ireland_constants.txt` as normal `8`, emergency/war `10`, and simultaneous national emergency plus Northern occupation `12`. The immediate-launch refresh patch makes those global limits effective within the same tick.

## Mission quality notes

Every family is owned by IRE. The listed title is the named objective and the bracketed value is its engine deadline. Each uses a named geographic or political requirement in `available`, records full or partial success on completion, records failure on timeout, and clears its individual active/objective flags on every terminal path. `fire_only_once` plus a matching active flag prevents duplicate launch of a family.

| Category and region | Mission families: named objective and deadline | Requirement, outcome, and duplicate-risk notes |
| --- | --- | --- |
| Settlement — Dublin Metropolitan Region | Maintain Cabinet Discipline [90d]; Assemble Seventy Routine Votes [45d]; Complete the Six-Month Settlement Review [180d] | Cabinet consent, Dáil mandate, and settlement thresholds; the 45-day vote deadline is urgent but its urgency is not explained in the player-facing description. |
| Elections — Dublin Metropolitan Region | Conduct a Free General Election [105d]; Form a Government after the Poll [60d]; Protect a By-election [100d] | Election and formation thresholds; 60 days is appropriate to a formation crisis but should be labelled as such. |
| Society — national service network | Deliver the Education Settlement [150d]; Keep Essential Services Running [60d]; Audit Parish Service Contracts [120d] | Service, education, and contract thresholds; the 60-day service deadline is credible as a strike/emergency response but not explicitly framed as urgent. |
| Cultural — five regions and evidence sites | Collect a National Folklore Cycle [180d]; Hold a Five-Region Cultural Congress [210d]; Verify Restoration Evidence [270d] | Named cultural/evidence objectives with long research windows. |
| Radical — route and crisis gates | No timed family | No duplicate or mission-cap concern in this category. |
| Provision — counties, Dublin/Cork corridor, coast, west | Meet the County Tillage Schedule [150d]; Bring the Harvest to Market [120d]; Commission the Protected Workshop Network [180d]; Complete a Developmental Plant [270d]; Supply the Capital through Winter [120d]; Cut and Dry the Turf [120d]; Restore the Dublin-to-Cork Corridor [180d]; Keep an Essential Cargo Route Open [120d]; Replace a Lost Merchant Vessel [270d]; Deliver a Western Regional Portfolio [300d] | Concrete material and regional objectives; duplicate protection is present, but the current global-only category flag does not enforce the specified 3/4 Provision cap. |
| Readiness — command districts, Dublin/Belfast, coast, treaty ports | Prove the Command District [105d]; Equip a Reserve Brigade [150d]; Secure the Dublin-to-Belfast Corridor [120d]; Complete a Coastwatch Sector [120d]; Defend a Treaty Port [210d]; Patrol the Neutral Approaches [105d]; Protect Plan W [120d]; Demobilise without Losing the Cadre [210d] | Named force, corridor, port, and plan objectives; duplicate protection is present, but the specified 3/4 Readiness cap is not. |
| Neutrality — airspace, waters, Blacksod | Resolve an Aircrew Internment Case [90d]; Investigate a Merchant Sinking [120d]; Maintain Equal Belligerent Rules [150d]; Keep the Blacksod Station Reporting [105d] | Incident and weather objectives use named cases; direct-incident concurrency is not separately represented. |
| Foreign — British, American, German, and Vatican channels | Deliver a British Supply Agreement [150d]; Complete an American Procurement Mission [240d]; Test a German Arms Promise [150d]; Conclude a Vatican Relief Mediation [120d] | Named partner channels and reciprocal tests; no decision-owned country target is dereferenced without a gate. |
| Northern — border health, convention, plebiscite, settlement | Open the Cross-Border Health Service [150d]; Secure a Representative Northern Convention [210d]; Conduct a Supervised Plebiscite [240d]; Ratify the Federal Settlement [300d] | Regional consent and settlement objectives; core review remains guarded by the canonical trigger. |
| Occupation — Belfast and stage-five integration | Take and Hold Belfast [150d]; Restore Ordinary Policing [240d]; Reopen Belfast Industry [300d]; Complete the Stage-Five Integration Review [365d] | Ownership, control, policing, industry, and integration gates prevent a free core loop. |
| Regional — member order and five sites | Ratify a Regional Charter [240d]; Meet the Member Contribution Schedule [180d]; Fulfil the Compact at Five Sites [300d] | External-order obligations with named regional objectives. |
| Postwar — national reconstruction | End Wartime Rationing Safely [240d]; Settle the Demobilised Forces [300d]; Bring the Republic Settlement into Force [150d]; Build Support for United Nations Admission [300d]; Complete National Reconstruction [365d] | Postwar material, political, and recognition objectives; full/partial/failure cleanup is present. |

## Issue list, sorted by severity

1. **High — category caps and critical reservations are not implemented as specified.** `ireland_rebuild_mission_counters` sets every `ireland_category_*_at_capacity` flag from the one global `ireland_active_mission_count >= ireland_mission_capacity` comparison. There are no per-category counters. The 53 ordinary mission activations also reject `ireland_critical_slot_reserved`, but there is no critical-family classification or reservation below the global cap. This does not meet the map’s 2/3/4 category caps or one/two/three critical reserves. Do not patch this piecemeal; see the follow-up handoff.

2. **Medium — escalation is named but never recorded as the shared escalation result.** Every mission timeout sets a family-specific `_escalated` flag, but all 54 record result `3` (failure), never `constant:ireland.mission_result_escalated` (`5`). `ireland_missions_escalated` therefore remains unused/zero even as failure escalation flags accumulate. The resolution needs an explicit decision whether escalation is a second telemetry dimension or a mutually exclusive terminal result.

3. **Medium — availability and dynamic-cost clarity are below the stated tooltip standard.** None of the 194 entries use `custom_trigger_tooltip`, `custom_cost_trigger`, or a decision-surface scripted-localisation reference. The long raw availability blocks contain the actual named requirement and scarcity bands. Action effects display `ireland_action_burden_tt`, but the dynamic surcharge is not a pre-click custom cost contract.

4. **Low — terminal capacity presentation can remain one mission high until the next daily tick.** `ireland_record_mission_result` rebuilds counters before each family clears its active flag. The next `on_daily_IRE` corrects it, and the patched next launch also corrects it, so this is conservative blocking rather than an overflow exploit. Moving the terminal refresh after every family cleanup is a mechanical but broad 54-family change.

5. **Low — 26 row-selection variables and two request flags are write-only.** The Conditions, Northern, and Evidence row handlers set selected-row variables which no GUI text, trigger, or gameplay source consumes. The Conditions Review and Evidence Inspect flags are also write-only. The existing tooltips make the rows informative, so this is inert UI state rather than an AI/gameplay exploit. Remove the clicks or add a selection detail surface only after product ownership chooses the intended interaction.

6. **Low — GUI asset diagnostics remain unresolved outside this narrow audit.** The GUI inspector reports two reused mechanic-ledger textures and cannot resolve static fallbacks for animated sprites. Source inspection confirms paired static GUI elements and mutually exclusive animation/fallback triggers, so those overlap diagnostics are not a direct visibility failure. Asset ownership should decide whether duplicate texture registrations are intentional and whether the animation metadata needs explicit fallback links.

## Costs, requirements, AI, cleanup, and exploit risk

- Base Political Power costs vary from `13` to `19`. Base Command Power varies from `20` to `35`; the scarcity surcharge is at most `10`, giving a verified maximum of **45**, below the required `<= 60` ceiling.
- The action surface includes 13 stockpile and 11 manpower effects, uses burden/component variables, and has no positive Political Power action effect. The 86 non-mission actions likewise contain no positive Political Power result. This is not a passive Political Power store or free-unit loop.
- Thirty-two actions do not have a re-enable timer because each is one-shot locked by its completion/remove lifecycle. The other actions use cooldowns; no repeatable free-equipment, core, war-goal, or manpower loop was found.
- All 194 entries have AI weights; all 140 actions and 54 missions reference route cleanup, and every mission cancels on route cleanup or loss of IRE identity. The strategy plans are route-abort aware. Fixed AI strategy targets are major tags (ENG, GER, ITA); decision scripts do not hold unsafe country event targets.
- No mission-specific event target is saved anywhere in current common/events/history sources. The shared cleanup clears two unused global mission target names, which is safe but redundant.
- Localisation is complete for all 140 actions and 54 mission names/descriptions. The English file retains UTF-8 BOM encoding. The remaining localisation issue is requirement/cost discoverability, not missing keys.

## GUI wiring and evidence

The category bindings are present: Conditions on Settlement Government, Concealed Evidence on Cultural and Archival Work, and Northern Ledger on Northern Settlement. All **32 GUI buttons** have exactly one scripted `<element>_click` effect and `<element>_click_enabled` trigger; no handler is orphaned.

The narrow GUI patch makes status layers exclusive:

- Conditions: critical when a component is below 30; otherwise warning below 60; otherwise ready.
- Northern: critical below the critical security/integration threshold; otherwise warning for security/flexibility; otherwise ready only at stage five with no warning condition.
- Concealed Evidence: critical for a disqualifier; otherwise warning below public-knowledge threshold; otherwise ready.

Post-patch inspector artifacts:

- Conditions inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/3901fde490bacb479b2cc1f5e9448ae44f15dac9cfeb2bd22e1bc8e0d179f46b/6d2d73195b7b8ed99d473cfb3dc68549aba9e4aebfcc0fa43c7fa5cd22e1ad6c/gui-inspect.98e0261b43de1ee3.json`
- Northern inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/0737f0374e4e6924ff9f93bd1d46f9c40795e2f45da31f46a3db5813b5971596/8d7f53e1c9c1e429162179f7a14b9e09df0a17397db020181b417fdf7ec0f186/gui-inspect.d02804a3ca1b1e04.json`
- Evidence inspect: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/eee2fa5110ce414f0c9764040c794dc2be45a5e523d5f89b033b8f4068d26fbd/d0c560d560333afd6240dff7906901dc34fafa6dfd445dadf37568f3539b34f2/gui-inspect.f8c02d144a5399ca.json`
- Conditions render and click map: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/87a264550da83f33c0c7086be289abe13b633686ee651a263f699c973e032e3d/8f8ce0a8a45269740107f2b2f5082dc571770b6e7dabd90f5f8929bd679699c7/ireland_conditions_panel_window-full.png` and `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/a84da1d3bc3c9d03f5cab79b0f60dc6dcdf5ecfcb8b243de651114f296b51d3f/5917ee648eb3cb15f170327b3fd37307ee28733125fee98e5da90ceee0832899/ireland_conditions_panel_window-click-regions.png`

The renderer still reports geometric overlap because its offline scenario does not evaluate the scripted GUI visibility predicates. Source-level threshold truth tables are the meaningful validation for this patch. Its `GUI_AI_EQUIVALENT_MISSING` warning applies to presentation-only row/refresh clicks; actual Northern core review also runs through `on_daily_IRE`, so AI is not dependent on a GUI click.

## Changes made

| File | Identifiers | Before | After |
| --- | --- | --- | --- |
| `common/decisions/ireland_decisions.txt` | all 54 `activate_mission` launch sites | Active flag was set, but capacity/counter flags waited for the daily IRE hook. | Calls `ireland_update_mission_capacity = yes` immediately after activation, enforcing the current 8/10/12 global cap in the same tick. |
| `common/scripted_guis/ireland_scripted_guis.txt` | the three ready/warning/critical visibility trigger sets | Multiple status icons could be true at the same position. | Explicit critical > warning > ready priority; Neutrality Integrity is included in Conditions warning/ready evaluation. |

## Validation performed

- Parsed the current decisions: 13 categories, 140 actions, 54 missions, and 54 unique launchers.
- Verified all 54 active flags are set before activation and all 54 now call the capacity refresh immediately after activation.
- Verified all 54 missions have availability, deadline, cancellation, terminal result recording, full/partial/failure feedback, AI, family cleanup, and a named escalation flag.
- Checked action-cost ranges and confirmed maximum dynamic Command Power cost is 45.
- Checked the three status-priority truth tables at normal, warning, and critical thresholds; each yields one intended status layer.
- Inspected and rendered the linked GUI panels. The renderer’s remaining overlap warnings are the known predicate-evaluation limitation described above.
- Ran a narrow event state-flow inspection of `ireland_mission_result`: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/0fb84756111ef5ff03ade89b06a82539200dcf421d0ab22f7c14ab5ca16c2d38/167e3dbdce46191278e9268a2e995625812b3293606e9c1b73b56e472aabbeb1/event-state_flow-c68cb1910645.json`.

## Remaining blockers and recommended ownership

The route design was not changed. The following require parent/architect decisions before implementation:

1. Implement category-specific counters, cap constants, critical-family classification, and reserve admission in `common/scripted_effects/ireland_runtime.txt`, `common/scripted_triggers/ireland_triggers.txt`, and the 54 mission activation sites.
2. Define whether `_escalated` is a secondary metric or an exclusive terminal result, then align `ireland_record_mission_result` and the 54 timeout effects.
3. Introduce a reusable availability/cost tooltip helper and dynamic localisation before touching the 194 raw player-facing trigger blocks.
4. Decide whether the write-only GUI selection/request controls should become an actual detail interaction or non-clickable informational rows.
5. Assign the duplicate texture and animation-fallback metadata diagnostics to the asset/UI owner.

The associated non-route redesign handoff is [`ireland_decision_mission_gui_reaudit_followup.md`](../ireland_decision_mission_gui_reaudit_followup.md).
