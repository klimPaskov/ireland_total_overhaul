# Ireland country-package audit handoff

Audit date: 2026-07-29

Scope: read-only country-package audit for `IRE` in Ireland Total Overhaul. Live HOI4 testing was excluded by request. The worktree was already substantially dirty; unrelated edits were preserved.

> Historical handoff note: the route-advisor finding in this dated audit was
> closed by `../ireland_route_advisor_package_tranche_2026-08-01.md`. The
> Northern lifecycle observations remain historical evidence and are superseded
> only where newer Northern source audits explicitly say so.

## Outcome

The Ireland tag, historical start, route leader registry, office registry, three persistent spirit families, law registry, cosmetic tags, flags, focus-tree assignment, source registrations, and AI registry are present. No gameplay or asset source was changed by this audit.

The two material handoff blockers are:

1. The Northern claim ledger is initialized but has no found progression or engine claim effect. Core granting is separately gated, but claim-to-control-to-occupation-to-settlement-to-integration is not fully engine-backed in the audited country surfaces.
2. Route-specific characters are country leaders only. `common/characters/slopx_ireland_route_characters.txt` contains no `advisor = { ... }` blocks; only the inherited vanilla Ireland advisor roster is recruited at game start.

Portrait review remains intentionally unresolved. Seven `needs_user_review` portraits have live character consumers. No review or blocked source was promoted, and no likeness was generated.

## Required baseline and boundaries

The source manifest was read but not modified:

- `docs/plans/ireland_focus_tree/assets/source_manifest.json`
- Manifest baseline: `47 complete`, `55 needs_user_review`, `67 blocked`
- Portrait budget: 60 canonical entries
- Route extensions: `RC-PORTRAIT-01` Daniel Morrissey is C3 and `needs_user_review`; `RC-PORTRAIT-02` Father Edward Cahill is C1 and blocked

Excluded from edits as requested: DDS files, source manifest, decisions, events, focuses, GUI, achievements, and specs. No new source or generated likeness was produced.

## Country-package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Tag registration and country definition | Covered through vanilla inheritance | Vanilla `common/country_tags/00_countries.txt:29` maps `IRE` to `countries/Ireland.txt`; vanilla `common/countries/Ireland.txt` supplies the base country definition. The mod adds route cosmetic tags only. |
| Historical country setup | Covered, with inherited OOB | `history/countries/IRE - Ireland.txt:4-55` keeps capital 113, `IRE_1936`, three research slots, technologies, 10 convoys, politics, and campaign initialization. |
| 1939 setup | Covered | `history/countries/IRE - Ireland.txt:57-105` keeps the vanilla 1939 OOB, technology/doctrine block, special project, and election state. |
| Characters and offices | Partially covered | Vanilla characters and advisors are recruited at `history/countries/IRE - Ireland.txt:20-40`; route leaders are in `common/characters/slopx_ireland_route_characters.txt`; office occupancy and vacancy registry is in `common/scripted_effects/slopx_ireland_offices.txt`. Route advisor blocks are missing. |
| Persistent route spirits | Covered | 63 ideas in `common/ideas/slopx_ireland_spirits.txt`, exactly 21 in each of three families. |
| Law ladders | Covered in registry | 17 law variables and staged lifecycle helpers in `common/scripted_effects/slopx_ireland_effects.txt:131-216` and `common/scripted_effects/slopx_ireland_laws.txt`. |
| Flags and cosmetics | Covered | 18 `IRE_SLOPX_*` cosmetic tags in `common/countries/slopx_ireland_cosmetic.txt`; each has root, medium, and small flag files and three localisation keys. |
| Northern claims and settlement | Incomplete | State 119 deliberately retains only ENG/NIR cores; the final IRE core is separately gated. The claim ledger itself has no found progression or claim effect. |
| Focus loading | Covered | `common/national_focus/slopx_ireland_focus_tree.txt:13-22` defines `slopx_ireland_focus_tree` and assigns it to `tag = IRE`; 217 focus definitions are present. No focus file was edited. |
| Decisions, events, and GUI | Audited only | Existing decision/event/GUI surfaces are outside this handoff's edit boundary. No files were changed. |
| Starting military and industry | Inherited and coherent | Vanilla `history/units/IRE_1936.txt` and `IRE_1939.txt` provide one infantry command, one infantry equipment production line, and no starting navy or air formation. |
| AI and playability | Registry covered, scenarios untested | 30 durable strategies and 10 overlays exist; 30 Ireland strategy plans are present. Live testing was excluded. |
| Localisation and assets | Mostly covered | Route cosmetic keys, spirit names/descriptions, party names, and registered portrait/idea sprites were checked. Direct literal names are used for route characters, matching the existing character-file pattern. |

## File surface checklist and findings

### History, map, and state setup

- `history/countries/IRE - Ireland.txt:4` sets `capital = 113`; vanilla states 113, 134, and 135 remain owned and cored by IRE. Dublin is province 11293 in state 113.
- `history/states/119-Northern Ireland.txt:5-26` sets `owner = ENG`, retains `add_core_of = ENG` and `add_core_of = NIR`, and intentionally omits an opening IRE core. State 119 retains the vanilla province list, VPs, infrastructure 3, one arms factory, two civilian factories, air base 1, two dockyards, naval base 4, manpower, aluminium, and coal.
- The Northern runtime initializer in `common/scripted_effects/slopx_ireland_effects.txt:439-445` separates variables for `slopx_ireland_northern_claim_ledger`, `slopx_ireland_northern_control_ledger`, `slopx_ireland_northern_occupation_ledger`, `slopx_ireland_northern_settlement_ledger`, and `slopx_ireland_northern_integration_ledger`.
- `slopx_ireland_apply_northern_core_review` in `common/scripted_effects/slopx_ireland_runtime.txt:5533` is the only found state-changing Northern core effect. It adds the IRE core to state 119 only after the final review gate. `common/scripted_triggers/slopx_ireland_triggers.txt:1428` and `common/script_constants/slopx_ireland_constants.txt:206-242` enforce the stage-5/final-proof thresholds.
- Follow-up implementation restored the dedicated claim step to `slopx_ireland_northern_settlement_ledger`: state 119 receives `add_claim_by = ROOT` when the focus completes. This records only Ireland's legal claim. It does not transfer ownership or control, mark occupation or settlement, advance integration, or add a core. The separate runtime ledger and stage-5 final review remain authoritative for every later stage.

### Politics, characters, offices, advisors, and parties

- `history/countries/IRE - Ireland.txt:42-53` starts democratic with popularity `democratic = 98`, `fascism = 1`, and `communism = 1`; elections are allowed every 48 months. The 1939 politics block is present at lines 99-105.
- Vanilla characters recruited at lines 20-40 include the four vanilla leader candidates, one commander, 15 advisors, and Ernest Walton as scientist. The vanilla source is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/IRE.txt`.
- Route definitions in `common/characters/slopx_ireland_route_characters.txt` cover real-person leader IDs `slopx_ireland_w_t_cosgrave`, `slopx_ireland_richard_mulcahy`, `slopx_ireland_john_costello`, `slopx_ireland_james_dillon`, `slopx_ireland_sean_lemass`, `slopx_ireland_daniel_morrissey`, `slopx_ireland_joseph_blowick`, `slopx_ireland_frank_ryan`, `slopx_ireland_peadar_odonnell`, and `slopx_ireland_gearoid_o_cuinneagain`.
- The same file defines institutional leaders `slopx_ireland_civil_republican_directorate`, `slopx_ireland_workers_party_executive`, `slopx_ireland_workers_smallholders_congress`, `slopx_ireland_corporate_estate_council`, `slopx_ireland_oduffy_command`, `slopx_ireland_gaelic_producer_council`, `slopx_ireland_christian_national_council`, `slopx_ireland_regional_ailtiri_council`, `slopx_ireland_ailtiri_state_directorate`, `slopx_ireland_clerical_guardianship`, `slopx_ireland_ira_army_council`, `slopx_ireland_high_king`, `slopx_ireland_five_provinces_steward`, and `slopx_ireland_compact_steward`. Institutional names and collective portraits follow the no-invented-person rule.
- `common/scripted_effects/slopx_ireland_offices.txt:9-23` defines the 15 office occupancy variables: president, Taoiseach, Tanaiste, party leader, parliamentary leader, cabinet minister, chief of staff, security chief, movement leader, armed-wing commander, council chair, provincial chair, High King, Compact Steward, and Transitional Administrator. Vacancy flags and aggregate counts are rebuilt at lines 146-224.
- Historical finding: route characters had no advisor role blocks at this audit date. The 2026-08-01 tranche now provides the route-specific advisor/high-command/minister package; this paragraph is retained to explain the earlier audit boundary.
- Party and route names are localized in `localisation/english/slopx_ireland_l_english.yml`; the country history uses the inherited vanilla party setup until the runtime route transition.

### Exactly three route-spirit families and law registry

- `common/ideas/slopx_ireland_spirits.txt` contains exactly three families, each with 21 definitions: governing, society, and security. The opening trio is added by `common/scripted_effects/slopx_ireland_effects.txt:428-435`:
  - `slopx_ireland_spirit_governing_order`
  - `slopx_ireland_spirit_organised_society`
  - `slopx_ireland_spirit_security_external_position`
- Route refresh logic in `common/scripted_effects/slopx_ireland_runtime.txt:2468-2574` removes/replaces one family at a time and includes failure/corruption states. All 63 idea names/descriptions are present in `localisation/english/slopx_ireland_l_english.yml`, and all 63 idea pictures are registered in `interface/slopx_ireland_secondary_assets.gfx`.
- The law registry contains exactly 17 ladders: constitutional government, emergency authority, censorship, rationing, tillage, mobilisation, internment, public order, occupation, education, religion, language, economic control, trade/shipping, foreign access, Northern settlement, and guarantee. Lifecycle helpers are in `common/scripted_effects/slopx_ireland_laws.txt`.

### Flags, cosmetics, and identity cleanup

- `common/countries/slopx_ireland_cosmetic.txt` defines exactly 18 route cosmetic tags, from `IRE_SLOPX_ARMY_COUNCIL` through `IRE_SLOPX_CONVERGENCE_ORDER`.
- Every one has root, medium, and small `.tga` files under `gfx/flags`; the corresponding `NAME`, `ADJ`, and `DEF` keys are present in `localisation/english/slopx_ireland_l_english.yml:5-58`.
- `common/scripted_effects/slopx_ireland_runtime.txt:3363-3495` clears old route identity before applying one cosmetic tag. No stale tag-reference or missing flag surface was found.

### Portrait source archive, registrations, and consumers

Archive check:

- All 56 canonical P entries with a non-`not_created` source path have an exact filename copy under `docs/portraits` (including the C1 recheck and blocked-queue sources).
- P-45, P-50, P-54, and P-55 have `source_path = not_created` in the manifest and therefore have no source to archive.
- Daniel Morrissey's `RC-PORTRAIT-01` source is preserved under `docs/portraits/source_originals`; Father Edward Cahill `RC-PORTRAIT-02` has no portrait source and remains blocked.
- `docs/portraits/README.md` remains the archive policy record. No archive file was changed.

Exact live `needs_user_review` portrait consumers:

| Manifest ID | Sprite | Live consumer | Consumer location |
| --- | --- | --- | --- |
| P-05 John A. Costello | `GFX_slopx_ireland_portrait_john_costello` | `slopx_ireland_john_costello` | `common/characters/slopx_ireland_route_characters.txt:28-35` (sprite line 31); registration `interface/slopx_ireland_sourced_assets.gfx:55` |
| P-06 James Dillon | `GFX_slopx_ireland_portrait_james_dillon` | `slopx_ireland_james_dillon` | `common/characters/slopx_ireland_route_characters.txt:39-46` (sprite line 42); registration line 56 |
| P-27 Joseph Blowick | `GFX_slopx_ireland_portrait_joseph_blowick` | `slopx_ireland_joseph_blowick` | `common/characters/slopx_ireland_route_characters.txt:72-79` (sprite line 75); registration line 58 |
| P-43 Frank Ryan | `GFX_slopx_ireland_portrait_frank_ryan` | `slopx_ireland_frank_ryan` | `common/characters/slopx_ireland_route_characters.txt:83-90` (sprite line 86); registration line 59 |
| P-46 Peadar O'Donnell | `GFX_slopx_ireland_portrait_peadar_odonnell` | `slopx_ireland_peadar_odonnell` | `common/characters/slopx_ireland_route_characters.txt:94-101` (sprite line 97); registration line 60 |
| P-56 Gearoid O Cuinneagain | `GFX_slopx_ireland_portrait_gearoid_o_cuinneagain` | `slopx_ireland_gearoid_o_cuinneagain` | `common/characters/slopx_ireland_route_characters.txt:105-112` (sprite line 108); registration line 61 |
| RC-PORTRAIT-01 Daniel Morrissey | `GFX_slopx_ireland_portrait_daniel_morrissey` | `slopx_ireland_daniel_morrissey` | `common/characters/slopx_ireland_route_characters.txt:61-68` (sprite line 64); registration line 57 |

The remaining canonical `needs_user_review` IDs with no non-interface consumer are `P-09`, `P-13`, `P-14`, `P-17`, `P-18`, `P-19`, `P-20`, `P-21`, `P-22`, `P-23`, `P-25`, `P-28`, `P-29`, `P-30`, `P-34`, `P-36`, `P-37`, `P-40`, `P-42`, `P-44`, `P-47`, `P-49`, `P-52`, `P-53`, `P-58`, and `P-60`. P-20, P-37, P-42, and P-60 have no live `.gfx` registration; the other registration-only entries remain review status and were not promoted by this audit.

### Starting military, technology, industry, supply, and production

- `history/countries/IRE - Ireland.txt:8-18` sets three research slots, infantry weapons, trucks, fuel silo, basic train, and 10 convoys.
- Vanilla `history/units/IRE_1936.txt` and `IRE_1939.txt` are used because no mod OOB override exists. Each has one infantry division template with nine infantry battalions at Dublin province 11293, no starting naval or air formation, and one `infantry_equipment_1` production line using one factory. 1936 progress is 0.75; 1939 progress is 0.77.
- Vanilla state 113 provides Dublin's capital, 5 civilian factories, one arms factory, one air base, naval base 6, infrastructure 4, steel 2, and coal 1. States 134 and 135 retain their vanilla Irish ownership/core and infrastructure/industry. Northern state 119 retains its historical ENG setup as noted above.
- No separate mod rail, navy, air, fuel-stockpile, or equipment-stockpile setup was found. This is coherent with the small historical start, but dynamic supply and AI survival remain untested because live HOI4 testing was excluded.

### AI and playability

- `common/ai_strategy/slopx_ireland_ai_strategy.txt` has exactly 40 definitions: 30 durable profiles and 10 temporary overlays.
- `common/ai_strategy_plans/IRE_slopx_ireland_strategy_plans.txt` contains the historical/reactive layer and route plan definitions, all gated by `original_tag = IRE` or Ireland route flags.
- The AI registry preserves the historical opening and explicitly reacts to office vacancy, Northern occupation/integration, invasion danger, provision breakdown, demobilisation, and route conclusion review. No static missing-ID issue was found.
- Live AI focus, supply, diplomacy, and survival scenarios were not run by request.

## Changed files

Only this new handoff file was added:

- `docs/plans/ireland_focus_tree/audits/ireland_country_package_audit_handoff_2026-07-29.md`

No country, character, idea, interface, localisation, DDS, source manifest, decision, event, focus, GUI, achievement, or specification file was modified. There are no changed tags, state IDs, leaders, parties, focus IDs, localisation keys, or formable IDs from this audit.

## Validation and skipped validation

Read-only checks completed:

- Confirmed manifest baseline `47/55/67` without editing the manifest.
- Counted 63 spirit ideas as 21/21/21 across the three families and checked their localisation and sprite registrations.
- Checked the 17 law-family registry and lifecycle file.
- Checked 18 cosmetic tags, all three flag sizes, and three localisation keys per tag.
- Compared every source-bearing canonical portrait manifest entry with the `docs/portraits` archive; no found source lacked an archive copy.
- Traced all canonical review portrait sprites and identified the seven live consumers above.
- Checked country history, vanilla OOB references, state 119 ownership/cores, focus-tree assignment, office registry, and AI definition counts.

Skipped: live HOI4 launch, save-game scenarios, focus rendering, event/decision/GUI runtime validation, and any asset reprocessing. These were excluded by the user or by the requested file boundary.

## Remaining blockers and parent handoff

- Decide whether to approve, replace, or leave each of the seven live review consumers pending. Do not promote C3/C1 sources without the required clearance decision.
- Complete and audit the route-specific advisor/high-command/minister definitions being implemented under the canonical country-package scope. The current route leaders and office variables must not be treated as equivalent to advisor coverage.
- Keep `RC-PORTRAIT-02` blocked until an exact, cleared Father Edward Cahill portrait source exists. Do not substitute or generate a likeness.
- Live-game and save-game scenario testing is outside the completion boundary by user instruction. This handoff makes no live-runtime claim, and that exclusion is not a completion blocker.

No simplification was silently substituted. The country-package audit is complete; the source-clearance and advisor items above remain open.
