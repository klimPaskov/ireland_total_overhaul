# Final Focus Reward/Layout Audit Handoff — 2026-08-13

## Final post-implementation audit — 2026-08-13

Scope was read-only against the stable shared source. No gameplay, layout,
localisation, or icon files were edited by this audit.

Source checked:

- \`common/national_focus/ireland_focus_tree.txt\`
- SHA-256: \`66737832af1add00924ae0179045a03eb01f748849bae92ababfe6fb25ebba31\`
- MCP focus-inspect revision: \`e258d0a62196463712f88468cba4764f705b9af265d66f739dac6c048f1fe898\`

## Verdict

**Conditionally complete; no blocking parser or reachability defect.**

The requested three-trunk structure, progressive reveal model, 150-focus
coverage, reward-key coverage, concrete-effect syntax, and final MCP layout
inspection all pass. Follow-up is still warranted for the two semantic
tooltip omissions below, five low-severity omitted XP mentions, one stale
historical addendum, and the strict “no marker/ledger-only payoff” target.
The latter is a design-density warning, not an engine-load blocker.

## Route and layout proof

Visible opening shortcuts remain exactly three:

| Trunk | Focus | Coordinates |
| --- | --- | --- |
| Government/politics | \`ireland_state_still_defined\` | \`(-7, 0)\` |
| National development | \`ireland_economic_war_review\` | \`(3, 0)\` |
| Defence/security | \`ireland_defence_estimates\` | \`(15, 0)\` |

Seven additional no-prerequisite nodes are gated support families
(Norton, Clann, vocational, cultural, Naval Staff, strict neutrality, and
Northern settlement); they are not opening trunks. Fifteen \`allow_branch\`
families retain explicit prerequisite/flag/date reveal gates:

\`ireland_norton_parliamentary\`,
\`ireland_clann_founding\`,
\`ireland_vocational_constitution\`,
\`ireland_cultural_survey\`,
\`ireland_establish_naval_staff\`,
\`ireland_strict_neutrality\`,
\`ireland_northern_settlement_ledger\`,
\`ireland_ira_republican_bridge\`,
\`ireland_congress_reform_bridge\`,
\`ireland_oduffy_network_revival\`,
\`ireland_clerical_failure_bridge\`,
\`ireland_ailtiri_cell_network\`,
\`ireland_high_king_evidence_gate\`,
\`ireland_five_province_mandates\`,
\`ireland_otherworld_investigation\`.

No prerequisite, \`allow_branch\`, or AI reachability edits were made in this
audit.

Current MCP inspect metrics:

- 150 focuses, 150 connectors, 150 resolved titles.
- Bounds \`x -15..26\`, \`y 0..16\`; 41-column authored span.
- Crossings: 0; connector-through-node intersections: 0; long connectors: 0.
- Same-row spacing defects: 0; minimum spacing: 2.
- Maximum connector span: horizontal 7, vertical 2.
- Validation passed. The 22 diagnostics are non-blocking linear-detour or
  staircase layout warnings (not parse, connector, or reachability failures).

Inspect artifact:
\`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/46f1eb80252bb3548fdf4cf9988a68d9383a356789d7ec76eff5fa4b70afacf6/2cf9c2b68b2c272b804e6e4c9fbf37145481b2e8d48a76110f90868afc356088/focus-inspect.e258d0a621964637.json\`

Current render artifacts:

- HTML: \`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/5d4057d3f199e0c496bbdb9fcaf275b9bedfe0578d837eee40f71629e4cd44cf/5e08c7d12a84348a671b735e8d542eedbf08b8602bdc0308622d15becb676845/ireland_focus_tree.focus.html\`
- SVG: \`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/d99442897488300c79cba1f78470c30f472e70cd04ac68df600dd451fa8e5db1/614c7bfe8138f113565310b385e88079e5c39b0f7e558c5d0dc54f84d081a0e5/ireland_focus_tree.focus.svg\`
- JSON: \`hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/f484822e2fb8347a30e5726c4aef68ab4b05848dd7e6bdbc0297c56ee9176fae/ccf9167ebdce159c2155d9929a209693fd2b59455ceb176bbb47a7852afed5a5/ireland_focus_tree.focus.json\`

## Coverage and identifier checks

- 150 unique focus IDs; 123 unique source focus references; unknown focus
  references: 0.
- Every focus has a title key and description key.
- Every focus has exactly one matching
  \`custom_effect_tooltip = ireland_<focus>_reward_tt\` call: 150/150.
- All 150 reward keys exist, are non-empty, and have unique text. Localisation
  is UTF-8 with BOM (\`efbbbf\`). No backend flag/recompute tokens leak into
  reward text.
- 150 unique focus icons resolve through
  \`interface/ireland_icons.gfx\` and
  \`interface/ireland_focus_shine.gfx\`; all referenced runtime DDS files are
  present.
- AI source has 30 \`ai_national_focuses\` blocks. All 150 IDs occur in AI
  plans; 132 are in ordered lists and 18 are represented by
  \`focus_factors\` only. Focus-level \`ai_will_do\` exists on 28 focuses.
  Unknown AI focus tokens: 0. The 18 factor-only IDs are a tuning risk, not an
  unreachable-focus defect.
- There are 60 unlock calls across 59 focuses, covering 58 unique existing
  actions/missions; unknown definitions: 0.
- All 15 file-local \`@IRELAND_FOCUS_*\` constants resolve. Shared
  \`constant:ireland.*\` references resolve against
  \`common/script_constants/ireland_constants.txt\` and
  \`ireland_maritime_constants.txt\`.
- The current 32 material/construction/fuel IDs use recognised equipment,
  building, and fuel effects. The 24 capability IDs use valid technology,
  doctrine, agency, or event forms. State IDs 113, 119, 134, and 135 are
  present in the vanilla/mod state files; \`GFX_intelligence_agency_logo_ireland\`
  is defined; \`ireland_events.432\` exists.

## Twelve requested delivery packages

The 12-package tranche is syntactically valid and inside the documented
balance bands:

| Focus | Delivery |
| --- | --- |
| \`ireland_transport_priority\` | 25 motorized equipment, 2 trains |
| \`ireland_maritime_reserve\` | 5 convoys |
| \`ireland_domestic_manufacturing\` | 1 civilian factory + shared slot |
| \`ireland_emergency_stockpiles\` | 300 infantry equipment + 50 support equipment |
| \`ireland_development_authority\` | 1 infrastructure level |
| \`ireland_provision_conclusion\` | 1 civilian factory + shared slot |
| \`ireland_readiness_command\` | 200 infantry equipment + 25 support equipment |
| \`ireland_air_warning\` | 1 anti-air level in Dublin + one-use electronics bonus |
| \`ireland_professional_army\` | 200 infantry equipment + 25 support equipment + support-tech bonus |
| \`ireland_interoperability\` | 25 motorized equipment + 25 support equipment + support-tech bonus |
| \`ireland_emergency_mobilisation\` | 300 infantry equipment |
| \`ireland_readiness_conclusion\` | 1 military factory + shared slot |

The full tree also contains the pre-existing Marine, defence, neutrality, and
exceptional-route packages. Across all source packages (not one guaranteed
playthrough), the current raw totals are approximately 2,750 infantry
equipment, 325 support equipment, 125 motorized equipment, 2 trains,
30 convoys, and 500 fuel. Because several packages are route-gated or
alternative, this is a balance-review warning rather than proof of a single
route stacking all totals.

## Actionable tooltip/effect mismatches

1. **\`ireland_german_channel\`** — source
   \`common/national_focus/ireland_focus_tree.txt:3307-3311\` grants a one-use
   50% \`support_tech\` research bonus, but
   \`ireland_german_channel_reward_tt\`
   (\`localisation/english/ireland_l_english.yml:4228\`) only describes the
   German emissary/delivery-proof actions. Add the support-tech bonus to the
   tooltip.

2. **\`ireland_northern_settlement_ledger\`** — source
   \`...ireland_focus_tree.txt:2904-2905\` executes
   \`119 = { add_claim_by = ROOT }\`, while
   \`ireland_northern_settlement_ledger_reward_tt\`
   (\`ireland_l_english.yml:4214\`) omits the legal claim. Add wording such as
   “records Ireland’s legal claim to Northern Ireland; it grants no core or
   control” so the boundary is explicit.

3. **Low-severity tooltip completeness:** the following concrete XP effects
   are not named in their otherwise accurate tooltips:
   - \`ireland_requisition_trawler_hulls\`: Navy XP 5
     (source line 2144; loc line 4205).
   - \`ireland_coastal_patrol_flotilla\`: Navy XP 10
     (source line 2191; loc line 4206).
   - \`ireland_establish_naval_staff\`: Army XP 5 and Navy XP 15
     (source lines 2287-2288; loc line 4208).
   - \`ireland_lough_swilly_watch\`: Air XP 10
     (source line 2419; loc line 4211).
   - \`ireland_atlantic_convoy_office\`: Navy XP 15
     (source line 2459; loc line 4212).
   These do not make the effects invisible or break loading, but adding the
   amounts would make all direct reward text fully exhaustive.

## Residual strict reward-density warning

Static effect classification (priority: material/capability/claim, then
decision/mission unlock, XP/command power, ledger, marker) is:

- 46 direct material/capability/claim IDs (32 material/construction/fuel;
  24 capability IDs with overlap; one legal claim).
- 35 unlock-only IDs (named decision/mission procedures).
- 3 XP/command-power-only IDs:
  \`ireland_rebuild_marine_service\`,
  \`ireland_marine_service_reserve\`,
  \`ireland_regional_maritime_defence_pact\`.
- 15 ledger-only IDs:
  \`ireland_clann_founding\`,
  \`ireland_clerical_failure_bridge\`,
  \`ireland_congress_reform_bridge\`,
  \`ireland_containment_protocol\`,
  \`ireland_cosgrave_institutional\`,
  \`ireland_crown_powers_charter\`,
  \`ireland_de_valera_reconciliation\`,
  \`ireland_dillon_intervention_caucus\`,
  \`ireland_dillon_public_dissent\`,
  \`ireland_emergency_direction\`,
  \`ireland_ira_republican_bridge\`,
  \`ireland_material_conclusion_proof\`,
  \`ireland_mulcahy_succession\`,
  \`ireland_oduffy_network_revival\`,
  \`ireland_vocational_constitution\`.
- 51 marker/helper-only IDs:
  \`ireland_active_neutrality\`,
  \`ireland_ailtiri_total_state_capstone\`,
  \`ireland_authority_before_arms\`,
  \`ireland_clerical_guardianship\`,
  \`ireland_clerical_route_capstone\`,
  \`ireland_close_oduffy_chapter\`,
  \`ireland_compact_with_otherworld\`,
  \`ireland_congress_plural_capstone\`,
  \`ireland_congress_plural_republic\`,
  \`ireland_congress_vanguard_capstone\`,
  \`ireland_constitutional_opposition\`,
  \`ireland_corporate_order\`,
  \`ireland_cosgrave_capstone\`,
  \`ireland_costello_capstone\`,
  \`ireland_de_valera_emergency_capstone\`,
  \`ireland_de_valera_reconciliation_capstone\`,
  \`ireland_dillon_war_assent\`,
  \`ireland_dominion_claim\`,
  \`ireland_elective_crown\`,
  \`ireland_emergency_opening\`,
  \`ireland_emergency_repeal\`,
  \`ireland_emergency_review\`,
  \`ireland_federal_republic\`,
  \`ireland_five_province_mandates\`,
  \`ireland_five_provinces_capstone\`,
  \`ireland_guardian_crown\`,
  \`ireland_high_king_evidence_gate\`,
  \`ireland_ira_civil_authority\`,
  \`ireland_ira_route_capstone\`,
  \`ireland_june_1942_public_launch\`,
  \`ireland_labour_as_conscience\`,
 \`ireland_lemass_developmental_capstone\`,
 \`ireland_mulcahy_capstone\`,
  \`ireland_norton_parliamentary_capstone\`,
  \`ireland_oduffy_corporate_capstone\`,
  \`ireland_oduffy_personal_capstone\`,
  \`ireland_organise_congress\`,
  \`ireland_otherworld_capstone\`,
  \`ireland_otherworld_evidence_ledger\`,
  \`ireland_otherworld_investigation\`,
  \`ireland_pentarchy_guardians\`,
  \`ireland_producer_constitution\`,
  \`ireland_public_order_review\`,
  \`ireland_reassemble_ghq\`,
  \`ireland_recovery_bridge\`,
  \`ireland_republican_government\`,
  \`ireland_restore_constitutional_calendar\`,
  \`ireland_state_still_defined\`,
  \`ireland_statutory_emergency\`,
  \`ireland_vocational_constitution_capstone\`,
  \`ireland_written_coalition_charter\`.

These 66 IDs are not parser failures: many are route anchors, evidence gates,
or capstones whose flags/helpers are consumed by existing decisions/events.
They are, however, the remaining strict “fairy-dust” risk if the acceptance
rule requires every focus to grant a direct material, capability, or named
playable unlock rather than a state transition.

## Documentation follow-up

\`docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_concrete_reward_density_addendum_2026-08-13.md\`
still contains a pre-pass effect inventory (15 equipment calls, 11 building
calls, and zero unlock calls) that no longer describes the stable source.
Reconcile that historical section or mark it explicitly superseded. The current
completion report and source-of-truth map carry the current 150-focus/32-material/
24-capability/59-unlock summary.

## Changes made by this audit

Only this handoff file was created/updated. No gameplay, layout, localisation,
icon, AI, decision, event, or scripted-system source was changed.

## Closure verdict — 2026-08-13 (post-patch, MCP b1c475)

The seven patched reward strings are present and aligned with their focus effects:

- ireland_german_channel names the one-use 50% Support Technology bonus and German-channel actions.
- ireland_northern_settlement_ledger names the state 119 legal claim and explicitly excludes a core or control transfer.
- ireland_requisition_trawler_hulls names 50 support equipment, 5 convoys, and 5 Navy Experience.
- ireland_coastal_patrol_flotilla names the Cork naval base, 50% naval bonus, and 10 Navy Experience.
- ireland_establish_naval_staff names Naval Staff/agency, 5 Army Experience, 15 Navy Experience, and destroyer research.
- ireland_lough_swilly_watch names the Donegal radar station and 10 Air Experience.
- ireland_atlantic_convoy_office names 15 convoys and 15 Navy Experience.

Parent MCP focus-inspect revision b1c475 reports 150 focuses/connectors with zero long connectors, crossings, node intersections, or same-row spacing defects. Coordinates are compacted to x -20..21; route structure remains unchanged.

Route/branch/institution tooltips are valid player-facing rewards for political, cultural, diplomatic, Northern, and concealed focuses. They reveal named branches, advance Parliament, open decisions or missions, commit route choices, establish institutions, record visible ledger/proof outcomes, or complete capstones. These focuses do not require arbitrary equipment or factories to avoid fairy-dust classification.

Final verdict: COMPLETE. No remaining blocker was found in this narrow post-patch verification. The only residual concern is balance tuning of alternative route packages, not tooltip alignment, identifiers, reachability, or layout.
