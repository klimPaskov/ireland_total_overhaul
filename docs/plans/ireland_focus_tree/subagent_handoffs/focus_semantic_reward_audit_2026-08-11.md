# Ireland focus-tree semantic and reward audit — 2026-08-11

Feature slug: `ireland_focus_tree`

Scope: read-only audit of `common/national_focus/ireland_focus_tree.txt`, its
player-facing layout, prerequisite semantics, completion rewards, localisation,
icons, and focus-selection plans. No gameplay files were edited.

## Executive judgement

The current source contains 150 focuses, one visible root, and 159 prerequisite
edges. The fresh `hoi4.focus_inspect` result reports `branchCount = 0`, zero
crossings, zero node intersections, and zero long connectors, but that metric is
not a semantic route audit: the source has eight `allow_branch` entry points and
many route gates hidden in `available = { ... }`. The rendered tree is 11,216 ×
2,092 px (63 columns × 17 rows), and fourteen first-class edges span the full
eight-column horizontal allowance. They are visibly long in the player tree even
though the MCP threshold calls them legal.

The larger player-facing problem is reward opacity. Only nine focuses grant a
direct inventory/experience/political-power/building/technology/event effect;
68 call a route or ledger helper; the other 73 completion rewards only set flags
or variables. The flags are often consumed by runtime gates, but a large subset
of the named `*_project_ready` and `*_ready` flags has no consumer outside the
focus file. Descriptions for those focuses promise food, energy, transport,
air-warning, diplomatic, and containment work that the completion tooltip does
not visibly deliver.

There are also three high-impact hidden-branch issues: Lemass's capstone is
visibly attached to the industrial `development_authority` lane even though its
mandatory Dáil gate comes from the childless `ireland_dail_nomination` focus;
the Lemass AI plan omits that focus; Otherworld Dominion requires the childless
`ireland_containment_protocol` through `available` without a visible edge; and
several shared material prerequisites are available-only rather than visible
connectors. Same-block focus lists are OR in HOI4 (per the offline National focus
modding page); `ireland_northern_question_in_arms`, `ireland_ira_route_capstone`,
`ireland_crown_powers_charter`, `ireland_five_provinces_capstone`, and
`ireland_northern_policy_proof` therefore already represent OR convergence and
must not be “fixed” into AND blocks.

## Route coverage

| Route/lane | Implemented focus surface | Audit result |
| --- | --- | --- |
| Shared opening and constitutional trunk | `ireland_state_still_defined`, `ireland_national_settlement`, election/constitutional/government focuses, Treaty Port transfer | Present. Opening fan is visually spread across x = -10..14, and early reward text is mostly marker-only. |
| Fianna Fáil / Emergency / Lemass | `ireland_republican_government` through `ireland_de_valera_*`, `ireland_emergency_*`, `ireland_lemass_developmental`, `ireland_dail_nomination`, `ireland_lemass_developmental_capstone` | Present but Lemass capstone is in the wrong visible lane and its Dáil gate is omitted from `IRE_ireland_route_lemass_developmental`. |
| Fine Gael / Mulcahy / Costello / Dillon | IDs `ireland_constitutional_opposition` through `ireland_dillon_war_assent` | Present; most intermediate rewards are flags only. Dillon's `ireland_dillon_intervention_caucus` is a one-flag focus with no tangible or visible consumer beyond the route sequence. |
| Labour / Clann / vocational | `ireland_norton_*`, `ireland_clann_*`, `ireland_vocational_*` | Present. Clann and vocational are two-to-three-node route stubs; their capstones call the conclusion helper but intermediate rewards are hidden route markers. |
| Serious culture | `ireland_cultural_survey`, `ireland_archival_record`, `ireland_serious_cultural_stewardship`, `ireland_cultural_evidence_ledger` | Present and shared by hidden routes. All four rewards are flags; no direct archive/site/mission effect is exposed in the focus reward. |
| National Provision | `ireland_provision_baseline` through `ireland_provision_conclusion` | Present as a wide support lane. Food, energy, transport, maritime, manufacturing, credit, stockpile, cooperative, and accounting focuses do not grant a direct project/building/equipment effect; their project-ready flags are generally source-only. |
| National Readiness / maritime | `ireland_readiness_baseline` through `ireland_readiness_conclusion`, plus Marine Service and naval-staff lane | Present. Marine Service has the only substantial tangible ladder. `ireland_command_audit` is a structural leaf whose completion is required by `available` on readiness focuses but has no visible child edge. |
| Neutrality / diplomacy | `ireland_strict_neutrality` through `ireland_neutrality_posture` | Present. `ireland_foreign_safeguards` visibly requires British and American parents but Vatican mediation remains an available-only third gate. Most diplomacy rewards only open channel flags. |
| Northern settlement | `ireland_northern_settlement_ledger` through `ireland_northern_policy_proof` | Present. The three policy models are an intentional OR convergence in one prerequisite block. Labour bridge is a structural leaf and is consumed only through `available` on policy proof. |
| Recovery / material proof | `ireland_recovery_bridge`, `ireland_restore_constitutional_calendar`, `ireland_material_conclusion_proof` | Present, but material proof is a marker-only leaf and does not call `ireland_begin_conclusion_review`; its Northern dependency is available-only. |
| IRA | `ireland_ira_republican_bridge` through `ireland_ira_route_capstone` | Present. Arms-before-authority and authority-before-arms are a correct OR choice; the route capstone's three visible parents are also OR. The visible lane still starts with an eight-column edge from Public Order. |
| Republican Congress | `ireland_congress_reform_bridge` through plural/vanguard capstones | Present with a real mutual-exclusion pair. Vanguard/plural intermediate rewards are mostly path flags; both capstones call the conclusion helper. |
| O'Duffy | `ireland_oduffy_network_revival` through personal/corporate capstones | Present with mutual-exclusion capstones. The network bridge begins eight columns left of `ireland_close_oduffy_chapter`. |
| Clerical / producer | `ireland_clerical_failure_bridge` through `ireland_clerical_route_capstone` | Present but shallow: three route focuses after the bridge and marker-only intermediate rewards. |
| Ailtirí | `ireland_ailtiri_cell_network` through `ireland_ailtiri_total_state_capstone` | Present and correctly hidden/dated. The first bridge is marker-only; no direct state/industry/force reward is visible before the conclusion helper. |
| High Kingship | `ireland_high_king_evidence_gate`, `ireland_elective_crown`, `ireland_guardian_crown`, `ireland_crown_powers_charter`, `ireland_high_king_capstone` | Only the elective/guardian surface is authored. The spec map also promises royal-household, captured-crown, and sacral work; those paths are represented as flags/events but not as player-facing focuses. The charter's same-block elective/guardian prerequisite is already OR. |
| Five Provinces | `ireland_five_province_mandates`, `ireland_federal_republic`, `ireland_pentarchy_guardians`, `ireland_five_provinces_capstone` | Only federal and pentarchy surfaces are authored. Confederation, Crown-and-Five, Four Provinces/Empty Chair, Fifth Province, and Rival Irelands are map-level promises without focus surfaces. The capstone's same-block federal/pentarchy prerequisite is OR. |
| Otherworld | investigation, evidence ledger, compact, containment, dominion, capstone | Core compact/containment/dominion surface exists. Tuatha, Fianna, regional-courts, and exploitation branches from the spec are absent. Dominion's containment requirement is hidden in `available`, leaving `ireland_containment_protocol` visually terminal. |

## Rendered connector audit

The following visible prerequisite edges have `abs(dx) = 8` (the MCP's maximum
legal span) and are the player-visible “long connectors” reported by the user:

| Parent → child | Coordinates |
| --- | --- |
| `ireland_state_still_defined` → `ireland_national_settlement` | (6,0) → (-2,1) |
| `ireland_state_still_defined` → `ireland_defence_estimates` | (6,0) → (14,1) |
| `ireland_national_settlement` → `ireland_public_order_review` | (-2,1) → (-10,2) |
| `ireland_constitutional_draft` → `ireland_election_mandate` | (-4,3) → (-12,4) |
| `ireland_constitutional_draft` → `ireland_replacement_charter` | (-4,3) → (4,4) |
| `ireland_active_neutrality` → `ireland_emergency_opening` | (-16,8) → (-24,9) |
| `ireland_defence_estimates` → `ireland_readiness_baseline` | (14,1) → (22,2) |
| `ireland_readiness_baseline` → `ireland_coastwatch` | (22,2) → (30,3) |
| `ireland_treaty_port_transfer` → `ireland_northern_settlement_ledger` | (-12,7) → (-4,8) |
| `ireland_public_order_review` → `ireland_ira_republican_bridge` | (-10,2) → (-18,3) |
| `ireland_church_labour_consultation` → `ireland_congress_reform_bridge` | (2,2) → (10,3) |
| `ireland_close_oduffy_chapter` → `ireland_oduffy_network_revival` | (-10,9) → (-18,10) |

The two true AND convergences with the highest visual cost are:

* `ireland_regional_maritime_defence_pact` has separate prerequisite blocks for
  `ireland_atlantic_convoy_office` (38,9) and `ireland_interoperability` (26,7),
  converging at (32,10), with one diagonal of `dx = 6, dy = 3`.
* `ireland_foreign_safeguards` has separate blocks for British leverage (24,5)
  and American diaspora (22,4); its Vatican requirement is hidden in
  `available`, not a visible connector.

The emergency-stockpile AND (`ireland_energy_board` +
`ireland_transport_priority` → `ireland_emergency_stockpiles`) is spatially
reasonable. `branchCount = 0` should therefore be read as an MCP layout-plan
classification limit, not as proof that the eight hidden branches are absent.

## Completion-reward inventory (all 150 IDs)

Classification is based on the top-level effects in each `completion_reward`:

* **A — direct tangible (9):** `ireland_rebuild_marine_service`,
  `ireland_requisition_trawler_hulls`, `ireland_coastal_patrol_flotilla`,
  `ireland_marine_service_reserve`, `ireland_establish_naval_staff`,
  `ireland_lough_swilly_watch`, `ireland_atlantic_convoy_office`,
  `ireland_regional_maritime_defence_pact`, `ireland_high_king_capstone`.
* **B — hook/ledger (68):** `ireland_state_still_defined`,
  `ireland_economic_war_review`, `ireland_rural_price_board`,
  `ireland_defence_estimates`, `ireland_command_audit`,
  `ireland_1938_trade_settlement`, `ireland_treaty_port_transfer`,
  `ireland_de_valera_stewardship`, `ireland_constitutional_stewardship`,
  `ireland_de_valera_reconciliation`,
  `ireland_de_valera_reconciliation_capstone`, `ireland_emergency_direction`,
  `ireland_de_valera_emergency_capstone`, `ireland_lemass_developmental`,
  `ireland_lemass_developmental_capstone`,
  `ireland_cosgrave_institutional`, `ireland_cosgrave_capstone`,
  `ireland_mulcahy_succession`, `ireland_mulcahy_capstone`,
  `ireland_costello_coalition`, `ireland_costello_capstone`,
  `ireland_dillon_public_dissent`, `ireland_dillon_war_assent`,
  `ireland_norton_parliamentary`, `ireland_norton_parliamentary_capstone`,
  `ireland_clann_founding`, `ireland_clann_by_election`,
  `ireland_vocational_constitution`,
  `ireland_vocational_constitution_capstone`,
  `ireland_cultural_evidence_ledger`, `ireland_provision_baseline`,
  `ireland_food_ledger`, `ireland_energy_board`,
  `ireland_transport_priority`, `ireland_maritime_reserve`,
  `ireland_domestic_manufacturing`, `ireland_rural_credit`,
  `ireland_emergency_stockpiles`, `ireland_development_authority`,
  `ireland_social_cooperatives`, `ireland_producer_accounting`,
  `ireland_provision_conclusion`, `ireland_readiness_baseline`,
  `ireland_readiness_command`, `ireland_coastwatch`, `ireland_air_warning`,
  `ireland_port_defence_project`, `ireland_maritime_protection`,
  `ireland_professional_army`, `ireland_civilian_oversight`,
  `ireland_interoperability`, `ireland_emergency_mobilisation`,
  `ireland_readiness_conclusion`, `ireland_recovery_bridge`,
  `ireland_ira_republican_bridge`, `ireland_ira_route_capstone`,
  `ireland_congress_reform_bridge`, `ireland_congress_plural_capstone`,
  `ireland_congress_vanguard_capstone`, `ireland_oduffy_network_revival`,
  `ireland_oduffy_personal_capstone`,
  `ireland_oduffy_corporate_capstone`, `ireland_clerical_failure_bridge`,
  `ireland_clerical_route_capstone`, `ireland_ailtiri_cell_network`,
  `ireland_ailtiri_total_state_capstone`,
  `ireland_five_provinces_capstone`, `ireland_otherworld_capstone`.
* **C — flags/variables only (73):** `ireland_national_settlement`,
  `ireland_public_order_review`, `ireland_church_labour_consultation`,
  `ireland_election_timetable`, `ireland_constitutional_draft`,
  `ireland_election_mandate`, `ireland_government_formation`,
  `ireland_replacement_charter`, `ireland_emergency_opening`,
  `ireland_active_neutrality`, `ireland_republican_government`,
  `ireland_statutory_emergency`, `ireland_emergency_review`,
  `ireland_emergency_repeal`, `ireland_dail_nomination`,
  `ireland_constitutional_opposition`, `ireland_close_oduffy_chapter`,
  `ireland_security_under_law`, `ireland_written_coalition_charter`,
  `ireland_dillon_intervention_caucus`, `ireland_labour_as_conscience`,
  `ireland_cultural_survey`, `ireland_archival_record`,
  `ireland_serious_cultural_stewardship`, `ireland_harbour_defence_board`,
  `ireland_cobh_dockyard_programme`, `ireland_strict_neutrality`,
  `ireland_armed_neutrality`, `ireland_treaty_port_diplomacy`,
  `ireland_british_leverage_management`,
  `ireland_american_diaspora_mission`,
  `ireland_vatican_small_state_mediation`, `ireland_foreign_safeguards`,
  `ireland_neutrality_posture`, `ireland_northern_settlement_ledger`,
  `ireland_northern_local_authorities`, `ireland_northern_trade_corridor`,
  `ireland_northern_labour_social_bridge`,
  `ireland_northern_federal_preparation`,
  `ireland_northern_unitary_preparation`,
  `ireland_northern_wartime_bargain`, `ireland_northern_policy_proof`,
  `ireland_restore_constitutional_calendar`,
  `ireland_material_conclusion_proof`, `ireland_reassemble_ghq`,
  `ireland_arms_before_authority`, `ireland_authority_before_arms`,
  `ireland_german_channel`, `ireland_northern_question_in_arms`,
  `ireland_ira_civil_authority`, `ireland_ira_army_council`,
  `ireland_organise_congress`, `ireland_congress_plural_republic`,
  `ireland_congress_vanguard_cell`, `ireland_oduffy_personal_command`,
  `ireland_army_acceptance`, `ireland_corporate_order`,
  `ireland_clerical_guardianship`, `ireland_producer_constitution`,
  `ireland_june_1942_public_launch`, `ireland_ceannaire_state`,
  `ireland_high_king_evidence_gate`, `ireland_elective_crown`,
  `ireland_guardian_crown`, `ireland_crown_powers_charter`,
  `ireland_five_province_mandates`, `ireland_federal_republic`,
  `ireland_pentarchy_guardians`, `ireland_otherworld_investigation`,
  `ireland_otherworld_evidence_ledger`,
  `ireland_compact_with_otherworld`, `ireland_containment_protocol`,
  `ireland_dominion_claim`.

### Exact shallow-reward candidates

The following source-only readiness/project flags have no consumer outside the
focus file (they are not opened by a decision, mission, event, or idea in the
current workspace):

| Lane | Focus IDs / source-only flags |
| --- | --- |
| Provision | `ireland_food_ledger` → `ireland_provision_food_project_ready`; `ireland_energy_board` → `ireland_provision_energy_project_ready`; `ireland_transport_priority` → `ireland_transport_project_ready`; `ireland_maritime_reserve` → `ireland_provision_maritime_project_ready`; `ireland_domestic_manufacturing` → `ireland_material_projects_ready`; `ireland_rural_credit` → `ireland_rural_credit_project_ready`; `ireland_emergency_stockpiles` → `ireland_emergency_stockpile_project_ready`; `ireland_social_cooperatives` → `ireland_social_cooperative_project_ready`; `ireland_producer_accounting` → `ireland_producer_accounting_project_ready`. |
| Readiness / defence | `ireland_readiness_command` → `ireland_readiness_command_ready`; `ireland_port_defence_project` → `ireland_port_defence_project_ready`; `ireland_civilian_oversight` → `ireland_civilian_oversight_ready`; `ireland_interoperability` → `ireland_interoperability_project_ready`; `ireland_professional_army` → `ireland_professional_army_ready`; `ireland_strict_neutrality` → `ireland_strict_neutrality_ready`; `ireland_armed_neutrality` → `ireland_armed_neutrality_ready`. |
| Diplomacy | `ireland_treaty_port_diplomacy` → `ireland_treaty_port_diplomacy_ready`; `ireland_american_diaspora_mission` → `ireland_american_mission_ready`; `ireland_vatican_small_state_mediation` → `ireland_vatican_mediation_ready`; `ireland_foreign_safeguards` → `ireland_foreign_safeguards_ready`. |
| Politics / hidden routes | `ireland_dail_nomination` → `ireland_lemass_dail_mandate_ready`; `ireland_dillon_intervention_caucus` → `ireland_dillon_intervention_caucus_complete`; `ireland_ira_army_council` → `ireland_ira_army_council_transition_ready`; `ireland_crown_powers_charter` → `ireland_crown_powers_charter_complete`; `ireland_containment_protocol` → `ireland_otherworld_containment_path`. |

These are not automatically “wrong”—some are historical evidence markers—but
the completion descriptions promise a concrete office, project, service, or
protocol. Each needs either a visible consumer (decision/mission/idea/event) or
a smaller direct reward. The most conspicuous mismatches are
`ireland_food_ledger`, `ireland_energy_board`, `ireland_transport_priority`,
`ireland_maritime_reserve`, `ireland_readiness_command`, `ireland_air_warning`,
`ireland_maritime_protection`, `ireland_civilian_oversight`,
`ireland_armed_neutrality`, `ireland_treaty_port_diplomacy`,
`ireland_foreign_safeguards`, `ireland_material_conclusion_proof`, and
`ireland_containment_protocol`: their localisation describes a tangible
programme while the reward is only a marker/recompute call.

## Leaves and hidden consumers

The structural DAG has 36 leaves. Most are intentional capstones, but the
following leaves deserve a consumer or explicit capstone treatment:

* `ireland_command_audit` is a leaf even though `ireland_readiness_baseline`
  and `ireland_coastwatch` require it in `available`.
* `ireland_dail_nomination` is a leaf even though it is the only writer of
  `ireland_lemass_dail_mandate_ready`, required by the Lemass capstone.
* `ireland_provision_conclusion` and `ireland_readiness_conclusion` are leaves
  whose descriptions say “conclusion review”, but their rewards only set a
  ready flag and recompute a ledger; neither calls
  `ireland_begin_conclusion_review`.
* `ireland_material_conclusion_proof` is a marker-only leaf and its Northern
  proof is available-only.
* `ireland_containment_protocol` is a marker-only leaf; Dominion requires it
  only through `available`, so the rendered branch visibly terminates at
  containment.
* `ireland_marine_service_reserve`, `ireland_civilian_oversight`,
  `ireland_emergency_mobilisation`, `ireland_armed_neutrality`,
  `ireland_vatican_small_state_mediation`, `ireland_neutrality_posture`, and
  `ireland_northern_labour_social_bridge` are structural leaves with subsystem
  flags or ledger hooks. They can remain leaves only if the corresponding
  decision/mission/event surface is made clearly visible in the focus tooltip.

Intentional route endpoints include the constitutional capstones, Congress and
O'Duffy capstones, `ireland_clerical_route_capstone`,
`ireland_ailtiri_total_state_capstone`, `ireland_high_king_capstone`,
`ireland_five_provinces_capstone`, `ireland_otherworld_capstone`, and the
tangible regional maritime pact. Those call the conclusion helper or grant a
direct final reward and should not be merged merely to eliminate leaves.

## Exact bounded fixes for the parent implementation

1. **Expose Lemass's real branch.** Change the visible prerequisite of
   `ireland_lemass_developmental_capstone` from
   `ireland_development_authority` to `ireland_dail_nomination`, or add a
   second visible prerequisite only after moving the node to a midpoint. Keep
   the material/Provision gates in `available`. Add
   `ireland_dail_nomination` immediately before the capstone in
   `IRE_ireland_route_lemass_developmental`; otherwise the plan can reach an
   unavailable capstone because no other file writes
   `ireland_lemass_dail_mandate_ready`.
2. **Expose Otherworld containment.** `ireland_dominion_claim` already requires
   `has_completed_focus = ireland_containment_protocol` in `available`; add a
   second prerequisite block for `ireland_containment_protocol` so its visible
   line is present. This is a semantic-preserving layout fix and is a short
   (4,11) → (2,12) edge.
3. **Expose short available-only convergences.** Consider visible prerequisite
   blocks for `ireland_vatican_small_state_mediation` →
   `ireland_foreign_safeguards`, `ireland_maritime_reserve` and
   `ireland_emergency_stockpiles` → `ireland_provision_conclusion`, and
   `ireland_emergency_mobilisation` and `ireland_interoperability` →
   `ireland_readiness_conclusion`. These are already hard gates in
   `available`; adding lines makes branch consumers legible. Do not expose the
   Northern/material gate without first moving the nodes, because it would
   create a 20-column diagonal.
4. **Compress the worst long edges in one bounded coordinate pass.** Suggested
   anchors are: move `ireland_economic_war_review` 12→10,
   `ireland_defence_estimates` 14→12, `ireland_public_order_review` -10→-6,
   `ireland_election_mandate` -12→-10, `ireland_replacement_charter` 4→2,
   `ireland_emergency_opening` -24→-20,
   `ireland_northern_settlement_ledger` -4→-8,
   `ireland_ira_republican_bridge` -18→-14,
   `ireland_congress_reform_bridge` 10→6, and
   `ireland_oduffy_network_revival` -18→-14. Shift each affected child lane
   by the same local offset rather than introducing a new focus. The naval pact
   can be tightened by placing the Atlantic office near x34 and the pact at x32,
   while keeping the interoperability branch at x28–30.
5. **Reward/consumer tranche.** Start with the nine Provision project flags and
   the readiness/diplomacy flags in the shallow-reward table. Either wire each
   flag to an existing decision/mission/idea/event with a player-facing tooltip,
   or replace the marker with a narrow direct effect that matches the existing
   ledger constants. Do not grant free territory, cores, units, or generic
   factories; the spec explicitly forbids those shortcuts.
6. **Plan-level AI.** Add the Dáil focus to the Lemass route plan, then review
   the historical/reactive queues for available-only dependencies before adding
   more ordered entries. The 28 focus-level `ai_will_do` blocks are route-entry
   and hidden-route guards; they do not by themselves make every capstone
   route-aware.

## Icon and localisation coverage

| Surface | Result |
| --- | --- |
| Focus IDs / icon references | 150 / 150; all unique |
| Base registrations (`interface/ireland_icons.gfx`) | 150 current names resolve; 226 total definitions, leaving 76 stale definitions from the retired larger tree |
| Shine registrations (`interface/ireland_focus_shine.gfx`) | 150 current `_shine` names resolve; 226 total definitions |
| Ireland goal DDS files | 226 files; all current icon paths exist |
| English focus localisation | 150 / 150 title keys and 150 / 150 `_desc` keys |

No Ireland icon or localisation reference is missing. The raster pass reported
only nine decoder errors for unrelated vanilla generic continuous-focus DDS
textures and the unrelated `continuous_restrict_freedom_desc` warning.

## AI behaviour gaps

The source has 28 direct `ai_will_do` blocks. All 150 focus IDs are referenced by
the Ireland plan file either in an ordered list or a factor block, but 20 focuses
are not in any explicit `ai_national_focuses` queue and rely only on factors or
fallback selection: `ireland_rural_price_board`,
`ireland_replacement_charter`, `ireland_dail_nomination`,
`ireland_food_ledger`, `ireland_rural_credit`,
`ireland_emergency_stockpiles`, `ireland_social_cooperatives`,
`ireland_readiness_command`, `ireland_air_warning`,
`ireland_maritime_protection`, `ireland_civilian_oversight`,
`ireland_emergency_mobilisation`, `ireland_armed_neutrality`,
`ireland_treaty_port_diplomacy`, `ireland_british_leverage_management`,
`ireland_american_diaspora_mission`,
`ireland_vatican_small_state_mediation`, `ireland_elective_crown`, and
`ireland_guardian_crown` (plus the tree wrapper is not a focus). This is not
automatically a defect, but it leaves support and alternate-choice focuses to
factor races. The concrete route deadlock is the Lemass Dáil omission described
above.

## Validation and artifacts

Required offline wiki pages and vanilla documentation were consulted, including
Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions,
Event modding, Decision modding, Idea modding, AI modding, National focus modding,
and the installed `effects_documentation.md`, `triggers_documentation.md`,
`modifiers_documentation.md`, and script-concept documentation.

Fresh MCP artifacts (all read-only):

* Inspect JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/f4bb7c8ad0528d9cadedcb73e3360362037fd335a67b6b9a9701e1e96432dca3/792b00b1e1ad409c8f80a6d5e488b0e90f9db2483e1c6848071026aa0775ab55/focus-inspect.75210a628d7f86c6.json`
* Structural HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4b998600688da0effb679e604ef8d8f8d965e0cb41d5e11a1a4c7a8ed20ac3092b/887f92913fb7c4a5999e98609ce68464521f40f544b6ee586fb375822543ccfe/ireland_focus_tree.focus.html`
* Structural SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/5d0ac457bf131d40da0b1b10f063c7ad85504291b41a4352e2b1b2f492294361/9f909e017fa85ab11770e958adf8ecfa16c63804d89b523d1c34273a0c56fbd3/ireland_focus_tree.focus.svg`
* Render JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d1b0d3a720839074c2ecd4599b20d410965e152d3091b699693f6e278d60e528/0b3ea9e84cfc913deeb6ff8d800e52dbea23532424aba9628a6ce9c92c802710/ireland_focus_tree.focus.json`
* Decoded raster PNG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/048cc26e327bfcc8321b66ff6c8be6ee9284c5d2647c711e220c13a74883ffcb/726f770a20795ebe5677f939bf0c080a30ca5585088bc0af0eb28978af9e29da/ireland_focus_tree.focus.png`
* Raster review SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/e955d094a78300aed4a979d735923da83cc2bb596a85c0e2855d62da13a18b02/704323d723cc01545bba0b5c389e4104d28151276631963d6420b2cfd90f28ec/ireland_focus_tree.focus.svg`

The raster validation is false only because the nine unrelated vanilla generic
continuous-focus DDS textures fail decoding; no Ireland icon failed. No game
launch or live-save validation was performed. This handoff is the only file
written by this audit.

Remaining risk: the large spec-level branch families (High Kingship, Five
Provinces, and Otherworld) need an improvement-plan/design decision before new
focus content is added; the bounded fixes above do not create those missing
routes.

## Final current-state verdict — 2026-08-12

This section supersedes the pre-fix measurements and proposed-fix wording
above. The audit was repeated against the stable post-implementation workspace
and was read-only; no gameplay file was changed.

### Accepted implementation evidence

* `common/national_focus/ireland_focus_tree.txt` still contains exactly 150
  focus IDs. Every ID is referenced by the Ireland AI plan file; the Lemass
  queue now includes `ireland_dail_nomination` before
  `ireland_lemass_developmental_capstone`.
* The current MCP revision is `e5a1b36f958de9f48d0792b70ffce2b4598c66429be656a9fc0d41044cffeef6`.
  It reports one root, 150 connectors, zero crossings, zero connector/node
  intersections, zero long connectors, zero same-row spacing defects, maximum
  horizontal span six, and maximum vertical span two. The rendered surface is
  `14736 x 2092` with bounds `x=-30..52`, `y=0..16`.
* The seven player-facing lane anchors are registered as shortcuts for
  politics, culture, industry, diplomacy, Northern policy, army/air readiness,
  and Naval Service. The eight authored `allow_branch` roots remain the only
  progressive hidden families. `branchCount = 0` is still returned by MCP, but
  that field does not infer semantic lanes from shortcuts, coordinates, or
  `allow_branch`; it is not a source defect.
* The bounded reward tranche is present: 37 distinct custom reward tooltips
  are wired to named ledger, experience, project, or institutional outcomes,
  115 variable-delta lines remain route-specific, and the focus source contains
  no generic `political_power`/`add_political_power` completion effect. The
  formerly shallow operational IDs now include the Provision, Readiness,
  diplomacy, Dáil, Dillon, High Kingship, IRA, and Otherworld reward contracts
  listed by their `*_reward_tt` keys in the source.
* The two previously hidden semantic dependencies are corrected in source:
  `ireland_lemass_developmental_capstone` visibly follows
  `ireland_dail_nomination` while retaining development/material gates in
  `available`, and `ireland_dominion_claim` has separate visible prerequisite
  blocks for both `ireland_compact_with_otherworld` and
  `ireland_containment_protocol`.
* English localisation is complete for all 150 title and description keys.
  All 150 Ireland icon references resolve to base and shine registrations and
  to `gfx/interface/goals/ireland/goal_<id>.dds` files.

### Exact residuals (not Ireland-local blocking defects)

1. **MCP semantic branch metric.** The fresh inspector still says
   `branchCount = 0`; this is a tool limitation, while the seven shortcut
   anchors and eight `allow_branch` roots are present in source and render.
2. **Raster decoder noise.** The high-fidelity raster reports nine DDS decode
   errors for vanilla generic continuous-focus textures and one unrelated
   `continuous_restrict_freedom_desc` localisation warning. No Ireland-owned
   focus icon, shine, or localisation reference fails.
3. **Optional AI ordering.** All 150 IDs are covered by the plan, but 18
   support/alternate focuses remain factor-only rather than appearing in an
   ordered `ai_national_focuses` list:
   `ireland_air_warning`, `ireland_american_diaspora_mission`,
   `ireland_armed_neutrality`, `ireland_british_leverage_management`,
   `ireland_civilian_oversight`, `ireland_elective_crown`,
   `ireland_emergency_mobilisation`, `ireland_emergency_stockpiles`,
   `ireland_food_ledger`, `ireland_guardian_crown`,
   `ireland_maritime_protection`, `ireland_readiness_command`,
   `ireland_replacement_charter`, `ireland_rural_credit`,
   `ireland_rural_price_board`, `ireland_social_cooperatives`,
   `ireland_treaty_port_diplomacy`, and
   `ireland_vatican_small_state_mediation`. They have factor coverage and do
   not create a hard route deadlock; they are a future AI sequencing polish
   item only.
4. **Intentional available-only proof gates.** The visible graph deliberately
   keeps several cross-lane proof requirements out of the connector field:
   Vatican mediation on `ireland_foreign_safeguards`, maritime/emergency
   component proofs on `ireland_provision_conclusion`, emergency/
   interoperability proofs on `ireland_readiness_conclusion`, labour and
   integration proof on `ireland_northern_policy_proof`, and the full
   material/foreign/Northern proof on `ireland_material_conclusion_proof`.
   These remain tooltip/availability gates rather than broken prerequisites;
   exposing them would reintroduce the long cross-lane connectors the current
   layout pass removed.

No Ireland-local structural, prerequisite, localisation, icon, AI-coverage,
or reward-contract defect remains in the requested seven-lane implementation.
The spec-level omitted subfamilies (additional High Kingship, Five Provinces,
and Otherworld route nodes) remain a future design decision, not a defect in
this fixed 150-focus tree.

### Current read-only artifacts

* Inspect JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/638f546274af9f2688f9c33c74cfb2e6337b1e830fe2327b675eaff4e79d8243/bfd2397cd16eff11d8a0e9299f98a5cd46ffd323d969768b0d3e48a11b6e431c/focus-inspect.e5a1b36f958de9f4.json`
* Structural render HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/0f9501fc221c42155cac3ac66aa33cede2cba3e7f4bf08b07bc5a85a1aa73ea2/7b61e92441dda7b16c3c2dd4bc61d82b402bcf48d53dcb942f1430d09fac6c22/ireland_focus_tree.focus.html`
* Structural render SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/fc705256de1e2c1f862acd9eeb0fcc2fa01d6842dbf82fd8b0efe6681b7e7de9/a5ae14ca485090da53aaeb7b13bee3f581529744339bb24c06167983b68b15ec/ireland_focus_tree.focus.svg`
* Structural render JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ba991583dbdf2214c72da03fdad62450cbfb19d74afcd6adc9b3da6d77465688/c2fb94e411bf8f47ddfc7ffa334ac371046a23e22de019d44d1afe86e7cbc096/ireland_focus_tree.focus.json`
* High-fidelity raster PNG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/15cf201ce13947b67834a4a1fa6924373584cf7c2ea2a361c18a13a27b273a5a/d8f9f0d646d6fff4b03ee9043d730d4504a2c8c4876bd3cb155d53a7812da62c/ireland_focus_tree.focus.png`
