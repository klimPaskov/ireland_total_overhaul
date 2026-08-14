# Exceptional routes depth — focus/AI handoff

Date: 2026-08-14  
Owner: `/root/exceptional_focus_implementation`  
Parent: `/root`

> Superseded implementation snapshot: the figures below describe the first
> focus/AI pass. Parent integration completed all 38 distinct focus sprites and
> shines, added the final visible connectors, and validated the current
> 256-focus/263-connector source. Current evidence is recorded in
> `docs/plans/ireland_country_package/subagent_handoffs/final_focus_audit_256_2026-08-14.md`.

## Result

The accepted addendum is implemented on the focus/AI/localisation/GFX/spec
surfaces. The national tree now has exactly 256 unique focus IDs: the original
218 plus 7 High Kingship, 9 Five Provinces, 18 Otherworld, and 4 convergence
focuses. No focus block was duplicated. The three opening roots remain intact;
the five public family gateways remain on the `y = 14` band. Existing event,
portrait, decision, and asset-source work outside this ownership boundary was
preserved.

## Route coverage

| Route | New focuses | Key route behavior |
| --- | ---: | --- |
| High Kingship | 7 | party capture, captive failure/rescue, witnessed stone and geasa, bounded Living Land, and unbounded-sacral recovery remain mutually exclusive and value-gated |
| Five Provinces | 9 | powers convention, funded federation, protected Empty Chair, confederation, Pentarchy, Fifth Province, and Rival Irelands use mandates/cohesion/budget/consent; no invented Ulster mandate or free territory |
| Otherworld | 18 | exploitation, local guardians, Tuatha-associated court, Fianna certification, regional courts, civil restoration, and Sealed State preserve evidence, rights, trust/veil, and named obligations |
| convergence | 4 | three pair conclusions and the final review are separately selectable; the final focus starts the 180-day review and does not grant a terminal result by itself |

All 38 new completion rewards call `ireland_refresh_exceptional_route_state = yes`.
Existing exceptional focus completions were brought onto the same refresh hook.
Terminal blocks continue to call the parent conclusion helper; the helper reads
`has_completed_focus` history rather than relying on a manually injected
conclusion flag.

The new direct event consumers are `ireland_events.440`–`.460` (with existing
438/439 retained where the route uses them). A local source audit found all 23
event IDs `438` through `460`, unique and directly wired. A focused MCP event
lint of `mod:events/ireland_exceptional_route_events.txt` indexed the source;
the subsequent focus inspect reports no missing event references.

## Focus IDs

High Kingship: `ireland_crown_in_party_hands`,
`ireland_break_the_captive_crown`, `ireland_the_captive_throne`,
`ireland_the_stone_gives_its_answer`, `ireland_geasa_of_the_crown`,
`ireland_high_kingdom_of_the_living_land`, `ireland_unbounded_sacred_rule`.

Five Provinces: `ireland_provincial_powers_convention`,
`ireland_fund_the_federal_compact`,
`ireland_four_provinces_and_an_empty_chair`,
`ireland_council_by_provincial_mandate`, `ireland_irish_confederation`,
`ireland_five_sovereign_orders`, `ireland_pentarchy_of_ireland`,
`ireland_the_fifth_province`, `ireland_rival_irelands`.

Otherworld: `ireland_turn_contact_into_power`,
`ireland_compel_an_answer`, `ireland_the_state_owns_the_mounds`,
`ireland_a_breach_made_deliberately`, `ireland_the_rights_of_local_guardians`,
`ireland_a_law_for_two_orders`, `ireland_recognise_the_elder_claim`,
`ireland_the_courts_beneath_the_hills`,
`ireland_a_government_under_the_mounds`,
`ireland_the_hounds_are_heard_again`, `ireland_muster_a_modern_fian`,
`ireland_no_host_without_equipment`, `ireland_guardians_of_two_irelands`,
`ireland_regional_otherworld_courts`,
`ireland_no_single_story_rules_them_all`, `ireland_the_emergency_must_end`,
`ireland_human_sovereignty_restored`, `ireland_the_sealed_state`.

Convergence: `ireland_high_king_of_two_irelands`,
`ireland_crown_and_five_provinces`,
`ireland_five_courts_of_the_otherworld`,
`ireland_fivefold_high_kingdom_of_two_irelands`.

## AI behavior

`common/ai_strategy_plans/IRE_ireland_strategy_plans.txt` now gives every new
exceptional and convergence ID factor `0` in `IRE_ireland_historical`. The
High Kingship, Five Provinces, and Otherworld plans list all new branch IDs and
use the accepted relative weights: captured `4`, sacral `3`, federal `10`,
confederation `7`, Empty Chair `6`, sovereignty `3`, balanced compact `10`,
containment `6`, Tuatha `4`, Fianna `5`, regional courts `6`, exploitation `2`,
and convergence `1`. `IRE_ireland_exceptional_convergence` is a separate
low-priority plan enabled only by component conclusions/readiness and disabled
while any exceptional recovery mission is active. Recovery and historical gates
remain higher priority than optional terminal selection.

Local AI audit: 256 focus IDs, 869 strategy references, zero unknown focus
references, 37 unique strategy plans, all 38 new IDs present in strategy plans,
and all 38 historical factors explicitly zero.

## Audit findings and priority

- Missing or simplified route content: none within the 38-focus ownership
  boundary. The only visual simplification is replacing selected long visible
  prerequisite connectors with equivalent `available` completion checks to keep
  route AND semantics exact and eliminate public-lane crossings.
- Localisation/reward mismatches: none found. All 114 focus keys resolve, and
  each reward tooltip describes the corresponding event, ledger, mission,
  conclusion, or bounded record without free cores, wars, units, manpower,
  equipment, or resources.
- AI behavior gaps: source routing is complete; live AI selection, failure
  recovery priority, and historical reveal behavior still require the parent's
  country-package scenarios.
- Highest-priority integration fixes are (1) rerun the integrated focus/event
  inspection after all parent changes, (2) run the no-free-core/war/unit/resource
  and 180-day convergence failure scenarios, then (3) review the final asset
  manifest and commit only the integrated plan surface.

## Localisation and icon coverage

- `localisation/english/ireland_l_english.yml`: all 114 keys (`title`, `_desc`,
  `_reward_tt` for 38 focuses) present; file begins with UTF-8 BOM.
- `interface/ireland_icons.gfx`: all 256 focus icon references resolve to a
  registered sprite. The 32 distinct new sprite consumers use the future
  `GFX_focus_ireland_<id>` names and `goal_ireland_<id>.dds` paths. Six planned
  nodes reuse the exact registered route sprites specified by the addendum:
  State Owns the Mounds, Guardians of Two Irelands, the three pair focuses, and
  the final convergence.
- `interface/ireland_focus_shine.gfx`: all 32 distinct new sprite consumers
  have one-frame shine registrations; reused nodes use their existing shine
  family. A local file audit found all 32 planned new DDS files present in
  `gfx/interface/goals/ireland/` after the parallel asset workstream.

## Layout and validation evidence

Latest `hoi4.focus_inspect` metrics:

- `focusCount = 256`, bounds x `-44..31`, y `0..27`;
- 253 connectors;
- crossings `0`, node intersections `0`, long connectors `0`;
- same-row spacing minimum `2`, too-close pairs `0`;
- max horizontal span `8`, max vertical span `4`, max Manhattan span `10`.

The authored hidden `available` locks on the convergence pair/final nodes and
selected terminal corridors intentionally avoid unrelated public-lane
crossings. MCP reports nonblocking isolated-card/detour advisories for those
locks and legacy clerical corridors. The latest render artifacts are:

- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4e2b7b3b4062fd0421f2536d5ea7c010187cbf0bf388d61dd7abac82a37cc433/0f949235b3e9ddcf70198ded164e976fc493d1b6156ccd98aee2d8e075ed2c3d/ireland_focus_tree.focus.html`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4d40303d34a8f805b4dad5ee60b347bfc35a0f24ebc425adbb53df563a0884fb/194016ca3f0306894a78dbe9e6948128a857527d7b6d27c2c639722dc126eed0/ireland_focus_tree.focus.svg`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/3f155fa9674e384737ed2e55a75f876c336b928ebf2cf0a098364256429fdfdb/a685a1b64e629c127e0ab3d9f995980a5683502a8cd0d3a75706bdcca2d287ee/ireland_focus_tree.focus.json`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/29db0a7c598624cab3c5a3de952c619701916efd68fe9cd2fe22fb57fe07eb47/1c483d821064b3097566232aa6cd1704276afa3870c04b0fc45615ed9497516e/focus-inspect.86a4f895b026618a.json`
- `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/a75ce5fa38968d8136e9c47441b2ff1153bd5212ea695fb9271599542528e906/96f6e5d27bfd601a98385f29af727aaafa5dc978bc5f182245a29837102e6c67/event-lint-cd31d9573859.json`

Local source audits also found no unknown focus prerequisites, no duplicate IDs,
no unsupported `<=`/`>=`, strict filter tokens, 32/32 new icon registrations,
32/32 new shine registrations, and 38/38 refresh hooks.

## Files changed by this subagent

- `common/national_focus/ireland_focus_tree.txt`
- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`
- `localisation/english/ireland_l_english.yml`
- `interface/ireland_icons.gfx`
- `interface/ireland_focus_shine.gfx`
- `docs/specs/ireland_country_package/index.md`
- `docs/specs/ireland_country_package/campaign_architecture.md`
- `docs/specs/ireland_country_package/systems_and_lifecycles.md`
- `docs/specs/ireland_country_package/ai_balance_assets_and_text.md`
- `docs/specs/ireland_country_package/implementation_matrix.md`
- this handoff

## Remaining integration risks / skipped validation

1. Focus inspection still reports nonblocking isolated-card and linear-detour
   advisories for the hidden `available` locks and retained legacy corridors.
   The requested crossing, intersection, long-connector, and spacing metrics are
   all zero. It also reports one unrelated vanilla continuous-focus localisation
   warning (`continuous_restrict_freedom_desc`).
2. The MCP event scan is workspace-wide and deferred helper projections; it did
   not provide a bounded route proof for the new events. The local event-ID
   audit and parent event-agent validation remain the evidence for source
   ownership.
3. No live-game scenario, country-package audit, or final feature-completion
   audit was run by this subagent. Parent owns those release gates, including
   the no-free-core/war/unit/resource acceptance scenarios and runtime AI
   behavior.
4. No commit was created, per parent instruction. Parent owns integration and
   commit boundaries.

No route family was simplified, no fallback tree was substituted, and no
requested focus, AI, localisation, icon registration, shine registration, or
spec promotion was omitted within this ownership boundary.
