# Ireland focus-tree audit handoff — 2026-07-29

Feature slug: `ireland_focus_tree`

Scope: interrupted audit of the 216-focus Ireland tree, its focus-selection
plans, route gates, rewards, conclusion proof, icons, and direct localisation.
No decisions, events, assets, GUI, achievements, or canonical specifications
were edited. HOI4 was not launched.

## Executive judgement

The interrupted 30-focus AI insertion was not desirable as an ordered queue
change. `ai_national_focuses` is a strict ordered list: while any listed focus
is possible, the AI follows that order and ignores node `ai_will_do`. The
insertion placed all 30 review, branch-specific, optional foreign, and
operational focuses ahead of the route opening in `IRE_ireland_historical` and
ahead of provision, readiness, Northern, recovery, and conclusion gates in
`IRE_ireland_route_reactive`.

The worst semantic cases are not merely theoretical:

- `ireland_party_conference`, `ireland_dail_nomination`, and
  `ireland_replacement_charter` are conditional route/recovery content,
  not universal route-reactive work.
- `ireland_interoperability` is listed before its required
  `ireland_foreign_safeguards`; `ireland_maritime_reserve` is
  listed before its required `ireland_transport_priority`; several
  others depend on upstream route or material focuses absent from the same
  queue.
- In the historical plan the block was placed before
  `ireland_republican_government` and the de Valera route sequence. In
  the reactive plan it was placed before `ireland_provision_conclusion`
  and `ireland_readiness_conclusion`. Any eligible item therefore
  pre-empted those route/conclusion candidates for another ten-focus cycle.

The direct correction removes the 30 IDs from both strict ordered lists and
retains their `focus_factors` entries. They remain probabilistic candidates
when the ordered route/conclusion queue has no currently possible target;
they no longer form a mandatory generic detour. A smaller ordered subset was
not justified without live scenario state because availability is distributed
between focus completion, runtime flags, route profiles, missions, and
external partner state.

## Changed files and identifiers

| File | Change |
| --- | --- |
| `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt` | Removed the same 30 IDs from the ordered list of `IRE_ireland_historical` and `IRE_ireland_route_reactive`; retained all 60 plan-level factor entries. |
| `docs/plans/ireland_focus_tree/ireland_focus_tree_focus_audit_handoff_2026-07-29.md` | This dated audit and handoff. |

No focus source, focus localisation, icon registration, runtime, decision,
event, asset, GUI, achievement, or spec file changed.

The 30 reviewed identifiers are:

`civil_war_memory`, `republican_veterans`, `public_order_review`,
`rural_price_board`, `domestic_industry_review`, `command_audit`,
`seanad_panels`, `replacement_charter`, `party_conference`,
`dail_nomination`, `food_ledger`, `maritime_reserve`, `rural_credit`,
`emergency_stockpiles`, `social_cooperatives`, `readiness_command`,
`territorial_reserve`, `coastwatch`, `air_warning`, `port_defence_project`,
`maritime_protection`, `professional_army`, `civilian_oversight`,
`interoperability`, `emergency_mobilisation`, `armed_neutrality`,
`treaty_port_diplomacy`, `british_leverage_management`,
`american_diaspora_mission`, `vatican_small_state_mediation`.

## Route coverage table

All 30 canonical durable profiles have a focus plan. `H` is historical,
`P` is plausible divergence, and `A` is deliberate absurdity after reveal.

| Profile | Class | Opening/gateway | Route conclusion or host conclusion | AI plan |
| --- | --- | --- | --- | --- |
| `historical_de_valera` | H | shared opening; de Valera stewardship | constitutional stewardship | `route_de_valera_stewardship` |
| `de_valera_reconciliation` | P | republican government/reconciliation | reconciliation capstone | `route_de_valera_reconciliation` |
| `de_valera_emergency` | P | emergency direction | emergency capstone | `route_de_valera_emergency` |
| `lemass_developmental` | P | Lemass developmental | developmental capstone | `route_lemass_developmental` |
| `cosgrave_institutional` | P | constitutional opposition/Cosgrave | Cosgrave capstone | `route_cosgrave_institutional` |
| `mulcahy_civil_defence` | P | Mulcahy succession | Mulcahy capstone | `route_mulcahy_civil_defence` |
| `costello_coalition` | P | Costello coalition | Costello capstone | `route_costello_coalition` |
| `dillon_intervention` | P | Dillon public dissent | Dillon war assent/conclusion handoff | `route_dillon_intervention` |
| `norton_parliamentary` | H/P | Norton parliamentary | Norton capstone | `route_norton_parliamentary` |
| `clann_agrarian_broker` | H/P | Clann founding | rural producer host conclusion | `route_clann_agrarian_broker` |
| `constitutional_vocational` | P | vocational constitution | vocational capstone with Dáil supremacy | `route_constitutional_vocational` |
| `serious_cultural_stewardship` | H/P | cultural survey | culture completion/host conclusion | `route_serious_cultural_stewardship` |
| `ira_civil_republican` | P | IRA republican bridge | IRA route capstone | `route_ira_republican` |
| `ira_ghq_command` | P | IRA command branch | IRA route capstone | `route_ira_ghq_command` |
| `congress_plural` | P | Congress reform bridge | Congress plural capstone | `route_congress_plural` |
| `congress_vanguard` | P | Congress reform bridge | Congress vanguard capstone | `route_congress_vanguard` |
| `odiffy_personal` | P | O'Duffy network revival | O'Duffy personal capstone | `route_oduffy_personal` |
| `odiffy_corporate` | P | O'Duffy network revival | O'Duffy corporate capstone | `route_oduffy_corporate` |
| `clerical_guardianship` | P | clerical failure bridge | clerical host capstone | `route_clerical_guardianship` |
| `producer_council_state` | P | clerical/producer bridge | producer constitution through clerical host conclusion | `route_producer_council_state` |
| `emergency_admin_restoration` | P | emergency opening | recovery/restoration conclusion path | `route_emergency_admin_restoration` |
| `ailtiri_total_state` | P/A | dated Ailtirí cell network | Ailtirí capstone | `route_ailtiri_total_state` |
| `high_king_constitutional` | P | High King evidence gate | High King capstone | `route_high_king` |
| `high_king_sacral` | A | High King evidence/convention reveal | High King capstone | `route_high_king` |
| `five_provinces_federal` | P | Five Provinces mandates | Five Provinces capstone | `route_five_provinces` |
| `five_provinces_pentarchy` | A | Five Provinces mandates/convention | Five Provinces capstone | `route_five_provinces` |
| `otherworld_compact` | A | Otherworld investigation/evidence | Otherworld capstone | `route_otherworld` |
| `otherworld_dominion` | A | Otherworld verified dominion | Otherworld capstone | `route_otherworld` |
| `otherworld_containment` | P/A | Otherworld investigation/containment | Otherworld capstone | `route_otherworld` |
| `convergence_order` | A | convergence components | convergence order capstone | `route_convergence` |

Shared opening evidence is `ireland_state_still_defined`,
`institutional_survey`, and `national_settlement`, followed by the
constitutional, sovereignty, Emergency, material, Readiness, neutrality,
Northern, recovery, and conclusion lanes. The source contains exactly 216
authored focus blocks; the `focus_tree` wrapper is not counted.

## H/P/A, route locks, and openings

- Historical AI is restricted to the historical profile and has no ordered
  hidden-route commitment. Hidden and radical profiles open through their
  named flags, dated gates, permission checks, or route transitions.
- Ordinary P routes use visible mutual-exclusion gateways and route-specific
  plans. Ailtirí has a dated launch and explicit hidden/rare-AI permission;
  its only node-level `ai_will_do` is deliberately zeroed for historical or
  unpermitted AI states at
  `common/national_focus/ireland_focus_tree.txt:4050`.
- High Kingship, Five Provinces pentarchy, Otherworld commitment, and
  convergence retain their hidden/reveal boundaries. The focus tree does not
  turn cultural study or evidence work into automatic sovereignty.
- The source parser found one true no-prerequisite/no-gate focus only:
  `ireland_state_still_defined`. The other 38 no-prerequisite focus
  blocks have explicit availability, allow-branch, or bypass gates. The
  parser found 165 focuses with one prerequisite block, 11 with two, and one
  with three; separate prerequisite blocks are treated as AND.

## Dillon intervention audit

`ireland_dillon_public_dissent`,
`ireland_dillon_intervention_caucus`, and
`ireland_dillon_war_assent` form the dedicated intervention sequence in
the focus source. The route plan lists the constitutional opposition,
sovereignty, active neutrality, dissent, caucus, and assent sequence. The
focus source keeps war behind the authored material, Dáil, sovereignty, home
reserve, contribution, command, and consent gates; the AI profile also
requires the Dillon predicate and the canonical Readiness/Provision floors.
The audit found no local prerequisite or mutual-exclusion defect in this
sequence. The runtime writer for the existing
`ireland_armed_neutralty_mandate` spelling matches the focus trigger;
that spelling is preserved because correcting it would cross the permitted
focus-AI scope without changing behavior.

## Northern boundary

The focus source does not grant Northern territory, cores, or occupation
control. `ireland_northern_regional_review` requires the authored core-
eligible integration-stage threshold, Readiness conclusion, and one completed
federal, unitary, wartime, or recovery preparation. It is followed by
`ireland_northern_policy_proof`, which records policy selection only
after integration or deferment. Core/occupation execution remains outside
this focus audit and is not weakened by the AI queue correction.

## Rewards and conclusions

- All 216 authored focuses have a completion reward. The reviewed 30 use
  route or subsystem flags and existing recompute helpers; they do not grant
  free factories, equipment, units, fuel, shipping, territory, cores,
  recognition, or alignment.
- Provision and Readiness conclusion focuses retain their explicit bottleneck
  and display floors. Readiness conclusion also requires
  `ireland_interoperability`.
- Route capstones call the existing conclusion-review helper only after the
  source-level government/law, Provision, Readiness, foreign, Northern,
  emergency/identity, and cleanup proofs. No conclusion reward was changed.
- The audit found no reward/localisation mismatch among the reviewed focus
  IDs. The existing typo-like `armed_neutralty` flag is an established runtime
  contract, not a newly introduced mismatch.

## Icon and localisation coverage

| Surface | Result | Evidence |
| --- | --- | --- |
| Focus IDs | 216 unique authored IDs | `common/national_focus/ireland_focus_tree.txt` |
| Focus icon references | 216 unique references | source `icon = GFX_focus_ireland_*` scan |
| Base GFX registrations | 216 matching names | `interface/ireland_icons.gfx` |
| Shine registrations | 216 paired definitions | `interface/ireland_focus_shine.gfx` |
| Runtime goal textures | 216 DDS files | `gfx/interface/goals/ireland/` |
| Focus title/description localisation | 216/216 direct pairs | `localisation/english/ireland_l_english.yml` |
| Localisation encoding | UTF-8 with BOM; no `:0` keys | same file |

The first icon scan counted the focus-tree wrapper as a pseudo-ID and used a
too-narrow shine-name pattern; the authoritative focus surface count is 216,
and the paired-shine registration is confirmed by the existing icon ledger
and `interface/ireland_focus_shine.gfx`. No icon or localisation file
was edited.

## AI behaviour before and after

| Plan | Before this correction | After this correction |
| --- | --- | --- |
| `IRE_ireland_historical` | 77 ordered focuses, with the 30 shared IDs between neutrality posture and republican government; 41 factor entries | 47 ordered focuses; same 30 IDs remain factors only; route opening resumes after neutrality posture |
| `IRE_ireland_route_reactive` | 69 ordered focuses, with the 30 shared IDs before provision/readiness/conclusion work; 64 factor entries | 39 ordered focuses; same 30 IDs remain factors only; conclusion/Northern/recovery spine retains strict priority |

All 30 IDs resolve to source focus blocks. No duplicate ordered IDs or factor
IDs were found in the two edited plans. The profile/overlay registry remains
exactly 30 durable profiles plus 10 temporary overlays. The 31 Ireland focus
plans remain present; this correction does not add a profile, overlay, route,
or focus.

The factor-only disposition is intentional: the engine's ordered queue now
selects the first currently possible route/conclusion target, while the
review/operational pool can still compete through plan-level multipliers when
the ordered targets are completed or unavailable. This is the safe static
choice because a smaller ordered subset would require declared campaign
states and live selection evidence that are not available in the offline
workspace.

## Validation and blockers

Completed task-specific validation:

- Offline `hoi4.focus_inspect` on workspace
  `mod_ireland_total_overhaul_65a6b5f140a7`: 216 focuses, 216 resolved titles, 197
  connectors, authored layout hash
  `1cfbb1f7ca61d5fe3683561dd504dd6ec82d606112dc036ea314f09e64339847`, zero
  Ireland-local layout diagnostics. Inspect artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/b5987c2a3e5d9ac111b1e8c9fc13d509bb60e52e5dbfb33350020e18915c2e7/8e7beea4877d82deb8953fdde0df19e05ebc07f09af94bf755dcbf4a0ef131b9/focus-inspect.04d965ce3078aea9.json`.
- Offline `hoi4.focus_render` returned HTML, SVG, JSON, source-map, and plan
  artifacts for the same tree and hash. Fresh full raster was blocked by the
  authored 79,504-pixel width; the prior valid 14,288-pixel raster artifact
  remains recorded in `docs/plans/ireland_focus_tree/focus_layout_inspection_2026-07-28.md`.
  Fresh HTML artifact:
  `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/3288b4b5daa821daba242dc3b6d1c76c6ca8e7c4d8ee2321ae2955742941191f/a8ea252387b448096cf78be59128c018988e769ce8336cdb2249ea16cdddc6ef/ireland_focus_tree.focus.html`.
- Source parser: exactly 216 focus blocks and 216 unique focus IDs after
  excluding the `focus_tree` wrapper; 216 icon refs;
  216 base GFX names; 216 shine registrations; 216 goal DDS files; 216
  title/description pairs; no duplicate localisation keys; no `:0` keys.
- AI-plan parser: 31 `IRE_ireland_*` plans; edited historical/reactive ordered
  counts are 47 and 39; all factor and ordered identifiers resolve; the 30
  reviewed IDs occur only in factor blocks after the correction.
- Profile/overlay roster scan: exactly 30 durable profile keys and 10
  overlay keys.

Global offline validation is not a clean pass: the focus inspector reports
14 unrelated vanilla continuous-focus missing-sprite/localisation diagnostics
under `game:common/continuous_focus/generic.txt` and one related warning.
They are outside Ireland and were not edited. No HOI4 launch or live scenario
validation was performed, per request.

## Remaining route risks and handoff

- Live engine priority among multiple simultaneously active strategy plans,
  profile transitions, focus completion timing, runtime flag writers, and
  factor-race probabilities remain unproven offline.
- The factor-only disposition avoids a forced detour but does not prove every
  optional shared focus will be selected in every profile. Route-specific
  plans remain the source of political/material prerequisites for their own
  routes.
- Northern occupation, integration, and core execution remain owned by the
  existing runtime/decision/event surfaces; this audit intentionally did not
  inspect or alter them beyond the focus boundary proof.
- The source/icon/localisation audit is structural evidence, not an in-game
  readability or asset-render proof.

Handoff path: this file. Parent review should specifically inspect the
factor-only plan semantics and decide whether a later scenario-backed,
route-specific small ordered subset is warranted; no such subset is claimed
here.
