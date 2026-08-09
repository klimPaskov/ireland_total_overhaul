# Final Ireland focus-quality audit — 2026-08-09

## Scope and source state

This bounded audit covers the final shared Ireland tree, its Ireland AI strategy plans, and the focus reward/availability contracts. The parent agent owns the concurrent geometry and localisation changes; this handoff records only the two gameplay/AI patches made by this subagent. No focus coordinates, `initial_show_position`, `allow_branch`, or prerequisite fields were changed here.

The current source contains 150 focus nodes (150 unique IDs) in one tree. The final HOI4 focus MCP revision (`f3eb8148dafc7f96...`) reports 150 nodes and 159 connectors with zero Ireland-local node intersections, crossings, through-node connectors, long connectors, spacing defects, linear detours, or staircase diagnostics. The evidence artifact is `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d4a39796bce33bf7ea6637aead1b99aa1248bd3a340f64e1f3144a367a636e94/421bc58e6e4be5c1a2c9125922e517a6e8c84186840a2b3571cffda032443e43/focus-inspect.f3eb8148dafc7f96.json`.

Required reference checks were made against the offline focus/AI modding wiki pages, the offline core data/effects/triggers/localisation pages, and vanilla AI strategy-plan examples. The AI-order rule used below is the vanilla/wiki rule: `ai_national_focuses` is an ordered queue; while a queue item can be taken, the AI ignores `ai_will_do`/`focus_factors` and only skips an item when it is completed or impossible.

## Patches

### AI coverage and mutually exclusive crown choice

File: `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`, plan `IRE_ireland_route_high_king`.

Before, the queue forced `ireland_elective_crown` and then attempted `ireland_guardian_crown`. Because those focuses are mutually exclusive, the queue could always take elective crown first whenever its mandate was available, starving the rare guardian route. The final queue ends at the shared `ireland_crown_powers_charter` gateway; the two alternatives are selected by fallback factors:

```text
ireland_elective_crown = 80
ireland_guardian_crown = 90
```

`ireland_guardian_crown` is available only when `ireland_high_king_rare_condition` is set, so the higher guardian factor only wins in the intended rare state. Otherwise elective crown remains the available alternative. `ireland_crown_powers_charter` has one prerequisite block containing both crown focuses; per the wiki this is OR semantics, so either completed alternative can enter the shared charter.

Post-patch static validation finds all 150 focus IDs represented by at least one Ireland AI plan queue or factor, with zero unknown AI focus references and zero unplanned focus IDs.

### Maritime reserve reward consumer

File: `common/national_focus/ireland_focus_tree.txt`, focus `ireland_requisition_trawler_hulls`.

`ireland_maritime_reserve` emits `ireland_provision_maritime_project_ready`. The flag previously had no downstream consumer. The trawler focus now accepts either the existing transport project or the maritime reserve project:

```text
OR = {
    has_country_flag = ireland_transport_project_ready
    has_country_flag = ireland_provision_maritime_project_ready
}
has_completed_focus = ireland_provision_baseline
```

This preserves the existing prerequisite (`ireland_rebuild_marine_service`), coordinates, branch visibility, and production rewards while closing the unused maritime project contract. The focus still grants the documented convoys, support equipment, navy experience, and civilian-factory output.

## Route coverage

| Route/family | Representative implemented chain | Status |
| --- | --- | --- |
| Shared opener and settlement | `ireland_state_still_defined` → `ireland_national_settlement` | Present; ordinary opener is visible at start. |
| Constitutional and stewardship | `ireland_election_timetable`, `ireland_constitutional_draft`, `ireland_government_formation`, `ireland_de_valera_stewardship`, `ireland_constitutional_stewardship` | Present, with reconciliation and recovery links. |
| Emergency government | `ireland_emergency_opening` → `ireland_emergency_direction` → `ireland_statutory_emergency` → `ireland_emergency_review`/`ireland_emergency_repeal` | Present; reviewed capstone `ireland_de_valera_emergency_capstone`. |
| Developmental state | `ireland_lemass_developmental`, `ireland_energy_board`, `ireland_transport_priority`, `ireland_development_authority`, `ireland_lemass_developmental_capstone` | Present; provision outputs feed later focuses. |
| Institutional leaders | Cosgrave, Mulcahy, Costello, Dillon, Norton and Clann sequences ending in their named capstones | Present; each has a terminal conclusion/recovery link or explicit policy endpoint. |
| Vocational/cultural | `ireland_vocational_constitution` → capstone; `ireland_cultural_survey` → `ireland_archival_record` → `ireland_serious_cultural_stewardship` → `ireland_cultural_evidence_ledger` | Present; cultural evidence gates the high-king family. |
| Provision/industry | `ireland_provision_baseline` → food/energy/transport/maritime/industry/rural/social/producer focuses → `ireland_provision_conclusion` | Present; maritime reserve project is now consumed by trawler requisition. |
| Readiness/defence | `ireland_readiness_baseline` → command/coastwatch/air/port/maritime/army/oversight/interoperability/mobilisation → `ireland_readiness_conclusion` | Present; parent’s final gateway keeps command audit in eligibility. |
| Neutrality and diplomacy | `ireland_strict_neutrality`, `ireland_armed_neutrality`, treaty-port, British, American, Vatican and foreign safeguards → posture | Present; channel flags feed decisions/runtime. |
| Northern policy | settlement ledger → local authorities/trade corridor → labour, federal/unitary and wartime bargain → policy proof | Present; both federal and unitary endpoints are reachable. |
| IRA Republican bridge | `ireland_ira_republican_bridge` → GHQ/arms-authority/foreign channel/Northern question/civil authority/army council → capstone | Present; hidden family is intentionally gated. |
| Congress | `ireland_congress_reform_bridge` → organise/plural/vanguard → two capstones | Present; hidden family is intentionally gated. |
| O’Duffy | network revival → personal command/army acceptance or corporate order → two capstones | Present; hidden family is intentionally gated. |
| Clerical/producer | clerical failure bridge → guardianship/producer constitution → capstone | Present; hidden family is intentionally gated. |
| Ailtirí | cell network → public launch → ceannaire state → total-state capstone | Present; hidden family is intentionally gated. |
| High King | evidence gate → elective/guardian crown → crown powers charter → high-king capstone | Present; guardian AI starvation defect fixed. |
| Five Provinces | provincial mandates → federal republic or pentarchy guardians → capstone | Present; hidden family is intentionally gated. |
| Otherworld | investigation → evidence ledger → compact/containment/dominion → capstone | Present; hidden family is intentionally gated. |

The current tree has exactly eight `allow_branch` roots, and no ordinary focus uses `allow_branch`:

1. `ireland_ira_republican_bridge`
2. `ireland_congress_reform_bridge`
3. `ireland_oduffy_network_revival`
4. `ireland_clerical_failure_bridge`
5. `ireland_ailtiri_cell_network`
6. `ireland_high_king_evidence_gate`
7. `ireland_five_province_mandates`
8. `ireland_otherworld_investigation`

This preserves ordinary branch visibility from the initial tree load while keeping only the eight explicitly supernatural/alternate route families hidden.

## Terminal and marker-contract review

The current prerequisite graph has 36 structural leaves. Leaf review found named route capstones calling the conclusion-review helper, policy endpoints setting route state, and readiness/provision endpoints invoking recompute helpers or substantive stockpile/building/experience effects. A broader final pass identified 86 focuses that write at least one single-use `*_ready`, `*_open`, `*_prepared`, or `*_valid` marker, but found zero no-op focus candidates after accounting for focus-ID consumers, consumed flags, direct ledger/project effects, and intentional endpoints. These markers are internal bookkeeping alongside substantive contracts; they are not player-facing localisation claims and were not bulk-deleted.

The marker-only cases were classified as follows (the scan covered `common/`, `events/`, `decisions/`, and `on_actions/` gameplay text):

- Gateway/state-record focuses (for example `ireland_national_settlement`, `ireland_constitutional_draft`, `ireland_cultural_survey`, and `ireland_restore_constitutional_calendar`) open later route contracts or record a completed policy state. Their structural completion and neighbouring focus prerequisites are the substantive contract even when a particular descriptive flag is not read elsewhere.
- Production/readiness/maritime focuses also perform recompute calls, variables, equipment, buildings, political power, or experience changes. Examples include `ireland_food_ledger`, `ireland_readiness_baseline`, `ireland_requisition_trawler_hulls`, `ireland_harbour_defence_board`, and `ireland_regional_maritime_defence_pact`.
- Capstones set conclusion validity and/or call `ireland_begin_conclusion_review`; these are intentional terminal outputs rather than dead ends.

No focus was found whose completion reward consisted solely of an unconsumed marker with no route/state contract. Several visually terminal nodes are consumed through `has_completed_focus` availability rather than a second flag read: `ireland_public_order_review` gates cultural and alternate-route work, `ireland_church_labour_consultation` gates constitutional/Northern/alternate work, `ireland_vatican_small_state_mediation` feeds foreign safeguards, and `ireland_northern_unitary_preparation` feeds Northern policy proof. Other leaves feed decisions or runtime (`ireland_coastwatch`, `ireland_coastal_patrol_flotilla`, `ireland_marine_service_reserve`, `ireland_containment_protocol`). Thus the single-use flags are bookkeeping on top of a substantive focus contract, not the only player-facing reward.

The one clearly hollow project output found in this bounded pass was `ireland_provision_maritime_project_ready`; it is now consumed by `ireland_requisition_trawler_hulls`. `ireland_trawler_hull_project_ready` remains a state marker emitted with substantive trawler rewards but has no separate downstream read; it is not the sole reward of that focus and is retained as bookkeeping. A future broad marker-contract pass may wire or retire such compatibility flags, but no safe one-line consumer was justified without expanding this patch beyond the parent-approved scope.

## Localisation and icon coverage

| Surface | Result |
| --- | --- |
| Focus IDs | 150 unique IDs; no duplicate focus IDs. |
| Title localisation | 150/150 title keys found. |
| Description localisation | 150/150 `_desc` keys found. |
| Focus icons | 150/150 `GFX_focus_ireland_*` definitions found. |
| Shine sprites | 150/150 `_shine` definitions found; no duplicate icon IDs. |
| Reward wording | `ireland_requisition_trawler_hulls_desc` describes convoys, support equipment, transport provision and factory output granted by the reward; no mismatch found. Guardian Crown wording matches its constitutional flags. |

No localisation or icon files were changed by this audit.

## Constant and AI reference checks

- Current gameplay source has no `constant:ireland.maritime.*` references; all maritime calls use the valid `constant:ireland_maritime.<key>` category/key form.
- Static constant resolution over `common/script_constants` reports zero undefined category/key pairs.
- AI-plan validation after the crown patch reports 150/150 focus coverage, zero unknown IDs, and zero orphaned focus IDs.

## Remaining risks and skipped validation

- Rare guardian-condition selection is established by the plan queue/factor contract: neither mutually exclusive crown is forced in the ordered queue, guardian has the higher factor when its rare availability condition is true, and elective remains the available ordinary alternative.
- The final MCP inspection and static source checks close the geometry, reference, and constant-category defects for this task.
- The 86 focuses with single-use state markers retain them as compatibility/bookkeeping alongside substantive contracts. They are documented rather than bulk-deleted because deleting marker state could break consumers outside the bounded focus/AI surface.

## Changed files and review handoff

- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`: `IRE_ireland_route_high_king`; removed mutually exclusive crown alternatives from the ordered queue and added elective/guardian fallback factors.
- `common/national_focus/ireland_focus_tree.txt`: `ireland_requisition_trawler_hulls.available`; consumed the maritime reserve project flag through an OR contract. This file also contains concurrent parent edits; review only the availability hunk for this handoff.
- `docs/plans/ireland_focus_tree/subagent_handoffs/final_focus_quality_audit_2026-08-09.md`: this audit and validation record.

No simplification or fallback route was introduced. No coordinates, initial camera position, hidden-family count, or prerequisite semantics were changed by this subagent.
