# Ireland focus tree audit — 2026-07-18

Historical snapshot note (reconciled 2026-07-22): this audit retains the MCP layout evidence and its broad-tree warnings, but its missing-setter, missing-AI-plan, and missing-icon-registration findings are superseded by the current source evidence in `common/scripted_effects/ireland_runtime.txt`, `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`, `common/ai_strategy/ireland_ai_strategy.txt`, and `interface/ireland_icons.gfx`. Use `docs/plans/ireland_focus_tree/source_of_truth_map.md` and `docs/plans/ireland_focus_tree/audits/ireland_completion_followup_2026-07-18.md` for current status. Live engine, global-diagnostic, and scenario gates remain open.

## Scope and disposition

Audited `common/national_focus/ireland_focus_tree.txt` against the canonical Ireland focus-tree specifications, route matrices, architecture maps, coding prompts, offline HOI4 wiki pages, vanilla national-focus precedents, the existing Ireland AI registry, localisation, and asset patterns.

The tree is structurally complete at 216 focus nodes. This audit made only local focus-file fixes: one parent-order correction in the Otherworld branch and five duplicate idempotent completion flags. Broader layout, AI queue, icon registration, and runtime gate issues remain handoff work because fixing them would require adjacent systems or a deliberate tree-layout pass.

## Evidence

- `hoi4.focus_inspect` workspace: `mod_ireland_total_overhaul_65a6b5f140a7`
- Latest inspect artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/33033a0fb062917dc2795ce19a39ce6f639e782ae8412e8f43923c669a6f02f4/4bd5020706184469d96f2e7b83f87fcb40308aa099c0e469614f60b83575625c/focus-inspect.eb3c382561c3dd0e.json`
- MCP result after the local patch: `focusCount = 216`, `resolvedTitleCount = 216`, zero same-row spacing violations, zero parent-order violations in the source audit.
- MCP layout metrics remain broad-tree warnings: 375 connectors, 2,567 crossings, 269 node intersections, and 180 long connectors. The render request was blocked by the fixed PNG dimension ceiling at the available review scale, so no render artifact was produced.

## Route coverage

| Route or lane | Focus coverage | Status |
| --- | --- | --- |
| Shared 1936/1937/1938 opening, Emergency and neutrality gateway | `ireland_state_still_defined` through `ireland_active_neutrality` (1–32) | Present |
| De Valera stewardship, reconciliation, and Emergency | `republican_government` through `de_valera_emergency_capstone` (33–50) | Present; H/P boundary labelled |
| Lemass developmental | `lemass_developmental` through `lemass_developmental_capstone` (51–58) | Present; P |
| Fine Gael/Cosgrave, Mulcahy, Costello | `constitutional_opposition` through `costello_capstone` (59–76) | Present; H/P |
| Dillon intervention | `dillon_public_dissent` through `dillon_war_assent` (77–79) | Present; dated and runtime-gated |
| Norton parliamentary, Clann agrarian, vocational constitution | `norton_parliamentary` through `vocational_constitution_capstone` (80–92) | Present; P |
| Serious cultural stewardship and evidence | `cultural_survey` through `culture_completion` (93–102) | Present; H/P |
| Provision, Readiness, neutrality, and foreign safeguards | `provision_baseline` through `foreign_safeguards` (103–134) | Present; support lanes |
| Northern ledger, settlement models, and final review | `northern_settlement_ledger` through `northern_policy_proof` (135–144) | Present; final runtime setter missing |
| Recovery, demobilisation, reconstruction, postwar proof | `recovery_bridge` through `material_conclusion_proof` (145–151) | Present; H/P |
| Concealed IRA/Army Council | `ira_republican_bridge` through `ira_route_capstone` (152–162) | Present; A/hidden permission |
| Concealed Congress plural/vanguard | `congress_reform_bridge` through `congress_vanguard_capstone` (163–170) | Present; A/hidden permission |
| Concealed O’Duffy personal/corporate | `oduffy_network_revival` through `oduffy_corporate_capstone` (171–178) | Present; A/hidden permission and death-date gate |
| Concealed clerical/producer | `clerical_failure_bridge` through `clerical_route_capstone` (179–184) | Present; A/hidden permission |
| Dated Ailtirí | `ailtiri_cell_network` through `ailtiri_total_state_capstone` (185–190) | Present; A/hidden permission and June 1942 date gate |
| Concealed High King | `high_king_evidence_gate` through `high_king_capstone` (191–196) | Present; A/hidden permission |
| Concealed Five Provinces | `five_province_mandates` through `five_provinces_capstone` (197–202) | Present; A/hidden permission |
| Concealed Otherworld | `otherworld_investigation` through `otherworld_capstone` (203–212) | Present; A/hidden permission; local parent order fixed |
| Crown/Province/Otherworld convergence | `crown_province_convergence` through `convergence_order_capstone` (213–216) | Present; conclusion proof gates present |

## Findings and remaining gaps

### High priority

1. `ireland_dillon_intervention_caucus` (`common/national_focus/ireland_focus_tree.txt`, `available`) requires `ireland_dillon_mandate_complete`, but that flag has one repository occurrence and no setter. The canonical `ireland_can_dillon` trigger exists in `common/scripted_triggers/ireland_triggers.txt` and contains the numeric Dillon gate, but it is used at `dillon_war_assent`, not as a replacement for the missing caucus-stage runtime handoff. Add the setter in the decision/event lifecycle or explicitly reconcile the focus gate with the canonical trigger; do not set it from an unrelated focus reward.
2. `ireland_northern_regional_review` requires `ireland_northern_regional_review_ready` and `northern_integration_stage >= constant:ireland.northern_stage_core_eligible`. The constant is 5, and `ireland_can_northern_core_review` correctly also requires `northern_final_review_passed` and no core-review block. The ready flag has one repository occurrence and no setter. The setter must come from the final rights/service/resistance/policing/guarantee review surface; adding it to the focus would bypass the required stage-5 proof.
3. Focus AI selection is not route-aware: the focus file has zero `ai_will_do` blocks and there is no Ireland `ai_strategy_plans`/`focus_factors` file. `common/ai_strategy/ireland_ai_strategy.txt` does contain the required 30 durable profiles and 10 overlays, but its route strategy links do not by themselves weight the national-focus queue. Add profile-aware visible-route weights and explicit zero/default handling for concealed gateways in a separate AI/focus pass.
4. All 216 focus icon references are unresolved in the current interface scan: the focus file uses `GFX_focus_ireland_*`, while no matching focus definitions are registered under `interface/`. Source focus atlases exist under `assets/ireland_focus_tree/icons/source_atlases/`, but no final focus-icon DDS package or `.gfx` registration was found. Register regular and shine sprites for all 216 IDs using the asset ledger; do not substitute generic filler.
5. The authored layout has a broad overlap problem beyond the fixed parent-order defect. The MCP report retains connector-through-node warnings and reports 2,567 crossings and 269 node intersections. A full compaction/reflow would change the current design and was intentionally not performed in this narrow audit.

### Route logic and safety checks

- The tree has 19 mutual-exclusion blocks covering the route gateway choices. The seven multi-focus prerequisite blocks are intentional OR choices for regional review, IRA command, Congress transition, crown powers, Five Provinces, Otherworld statecraft, and convergence; ordinary mandatory prerequisites are separate blocks and therefore ANDed.
- Date gates found: 1938 trade settlement (`date > 1938.2.1`), Emergency opening/direction (`date > 1939.9.1`), Dillon public dissent (`date > 1942.1.1`), Clann founding (`date > 1939.6.29`), Clann by-election (`date > 1940.1.1`), O’Duffy personal command (`date < 1944.11.30`), and the duplicated Ailtirí branch/availability guard plus June 1942 public launch (`date > 1942.6.1`). No date gate was simplified.
- Static reward audit found no focus effects granting Northern cores, territory, buildings, equipment, units, fuel, shipping, administration, alignment, or recognition. The only direct Northern map effect is the intended legal claim on state 119 in `ireland_northern_settlement_ledger`; it is not a core or control reward.
- The focus header and section comments preserve the H/P/A boundary. Concealed branches use `ireland_hidden_permission` and their named reveal flags rather than ordinary visible-route access.
- The exact 216 focus IDs have 216 title keys and 216 description keys in `localisation/english/ireland_l_english.yml`; the file has a UTF-8 BOM. No missing localisation was found.

### Localisation and reward mismatches

- The localisation surface is complete, but several descriptions are generic relative to their route-specific handoffs. `ireland_june_1942_public_launch_desc` is generic and does not explain the dated public launch, while `ireland_corporate_gaelic_nation_desc` describes O’Duffy’s veteran network although the focus belongs to the Ailtirí route. `clerical_failure_bridge`, `service_state`, and `producer_constitution` repeat the same settlement phrasing.
- The 216 completion rewards are primarily flags, variables, and scripted lifecycle helper calls. This is consistent with the file header’s handoff design and the no-free-material rule, but downstream consumers must provide the promised mechanical unlocks; the focus file alone does not prove those rewards are player-visible or route-specific.

## Local changes

Changed only `common/national_focus/ireland_focus_tree.txt`:

- `ireland_otherworld_evidence_ledger`: moved from `y = 37` to `y = 38` so its `otherworld_witnesses` prerequisite is above it.
- `ireland_compact_with_otherworld`: moved from `y = 38` to `y = 39` so both Otherworld prerequisites are above it.
- Removed duplicate idempotent completion flags from `ireland_site_stewardship`, `ireland_emergency_accounting`, `ireland_high_king_convention`, `ireland_federal_convention`, and `ireland_ulster_rule`.

Post-patch source audit: 216 focus nodes, no duplicate IDs, no duplicate coordinates, and zero parent-order violations. No route, reward gate, localisation key, icon reference, date gate, or Northern claim behavior was changed.
