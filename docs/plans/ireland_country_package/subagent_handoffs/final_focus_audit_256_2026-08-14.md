# Final Ireland focus audit — 256 focuses / 265 connectors

Date: 2026-08-14  
Scope: current Ireland focus tree, with priority on the 38-focus exceptional-route tranche  
Owner: `/root/final_focus_audit_256`  
Status: bounded audit complete; one narrow source correction applied

## Verdict

The exceptional tranche is present in the current 256-focus source and its fresh
MCP inspect/render pass is structurally clean: 256 focuses, 265 connectors, zero
crossings, zero node intersections, and zero long connectors. The three Fianna
focus filters were corrected to match their direct effects. No route family,
reward system, asset family, localisation set, AI plan, or thumbnail was
redesigned.

The remaining issues are contract/visibility risks rather than missing route
content: several convergence and Otherworld capstone prerequisite connectors are
intentionally simplified to preserve the current zero-crossing geometry, while
their `available` blocks still enforce the intended AND/OR route conditions.

## References consulted

- `AGENTS.md`.
- `.agents/skills/hoi4-focus-trees/SKILL.md`, `hoi4-subagents`,
  `hoi4-feature-assets`, `hoi4-improvement-loop`, `hoi4-events`, and
  `hoi4-decisions-missions`.
- Offline wiki pages for data structures, triggers, effects, modifiers,
  localisation, scopes, on actions, event/decision/idea/AI modding, and national
  focus modding. In particular, the focus page confirms that multiple entries in
  one `prerequisite` block are OR, multiple blocks are AND, and prerequisite
  connectors are visual while `available` is the live gate.
- Relevant vanilla documentation under
  `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`,
  including focus and AI documentation.
- `docs/plans/ireland_country_package/improvement_loop/ireland_exceptional_routes_depth_addendum_2026-08-14.md`,
  `docs/specs/ireland_country_package/implementation_matrix.md`, and
  `docs/specs/ireland_country_package/ai_balance_assets_and_text.md`.

## Route coverage

| Surface | Current coverage | Evidence / risk |
| --- | --- | --- |
| Opening | Exactly three un-gated roots: `ireland_state_still_defined` (`-12,0`), `ireland_economic_war_review` (`0,0`), and `ireland_defence_estimates` (`12,0`). | Shared settlement/reveal logic sets `ireland_political_routes_revealed`; MCP reports all three roots and clean geometry. |
| High Kingship | Seven tranche focuses: `ireland_crown_in_party_hands`, `ireland_break_the_captive_crown`, `ireland_the_captive_throne`, `ireland_the_stone_gives_its_answer`, `ireland_geasa_of_the_crown`, `ireland_high_kingdom_of_the_living_land`, `ireland_unbounded_sacred_rule`. | Existing evidence gate, claimant convention, elective/guardian crown, charter, provincial compact, Brehon commission, defence council, household council, and capstone remain connected and route-aware. Source additions are around lines 6151–6326. |
| Five Provinces | Nine tranche focuses: `ireland_provincial_powers_convention`, `ireland_fund_the_federal_compact`, `ireland_four_provinces_and_an_empty_chair`, `ireland_council_by_provincial_mandate`, `ireland_irish_confederation`, `ireland_five_sovereign_orders`, `ireland_pentarchy_of_ireland`, `ireland_the_fifth_province`, `ireland_rival_irelands`. | Federal, Empty Chair, confederal, pentarchic, Fifth Province, and Rival Irelands branches have exclusions, mission/event gates, and bounded rewards. Source band is around lines 4214–4554. |
| Otherworld | Eighteen tranche focuses: exploitation (`ireland_turn_contact_into_power`, `ireland_compel_an_answer`, `ireland_the_state_owns_the_mounds`, `ireland_a_breach_made_deliberately`); local-law/Tuatha (`ireland_the_rights_of_local_guardians`, `ireland_a_law_for_two_orders`, `ireland_recognise_the_elder_claim`, `ireland_the_courts_beneath_the_hills`, `ireland_a_government_under_the_mounds`); Fianna (`ireland_the_hounds_are_heard_again`, `ireland_muster_a_modern_fian`, `ireland_no_host_without_equipment`, `ireland_guardians_of_two_irelands`); regional (`ireland_regional_otherworld_courts`, `ireland_no_single_story_rules_them_all`); containment/recovery (`ireland_the_emergency_must_end`, `ireland_human_sovereignty_restored`, `ireland_the_sealed_state`). | Investigation, evidence ledger, compact/containment roots, dominion terminal, and capstone are present. Route branches use events, missions, decisions, obligations, variables, and mutual exclusions; no free units, stockpiles, cores, ownership, or war goals were introduced. Source band is around lines 4598–5193. |
| Convergence | Four focuses: `ireland_high_king_of_two_irelands`, `ireland_crown_and_five_provinces`, `ireland_five_courts_of_the_otherworld`, `ireland_fivefold_high_kingdom_of_two_irelands`. | Pair/conclusion scripted triggers are present in `common/scripted_triggers/ireland_exceptional_routes.txt`; final three-family trigger enforces all pair conclusions, thresholds, and disqualifiers. Source band is around lines 5224–5306. |

The addendum's tranche count is exact: 7 High Kingship + 9 Five Provinces +
18 Otherworld + 4 convergence = 38, taking the prior 218-focus source to 256.

## Missing or simplified content

1. The visible prerequisite connector list is narrower than the full logical
   contract in the Otherworld capstone and convergence band:

   - `ireland_otherworld_capstone` visibly lists
     `ireland_a_law_for_two_orders`, `ireland_a_government_under_the_mounds`,
     `ireland_guardians_of_two_irelands`, and `ireland_dominion_claim`; its
     `available` OR also admits `ireland_human_sovereignty_restored` and
     `ireland_the_sealed_state`.
   - `ireland_high_king_of_two_irelands` visibly lists only
     `ireland_high_king_capstone`; `available` requires the High King capstone,
     Otherworld capstone, and `ireland_high_king_otherworld_convergence_ready`.
   - `ireland_crown_and_five_provinces` visibly lists only the High King
     capstone; `available` requires both component capstones and
     `ireland_crown_five_provinces_convergence_ready`.
   - `ireland_five_courts_of_the_otherworld` visibly lists only
     `ireland_five_provinces_capstone`; `available` requires both component
     capstones, `ireland_five_courts_convergence_ready`, and the rights floor.
   - `ireland_fivefold_high_kingdom_of_two_irelands` visibly lists only
     `ireland_crown_and_five_provinces`; `available` requires all three pair
     focuses and `ireland_three_orders_convergence_ready`.

   A test insertion of all exact visible connectors produced 10 crossings, 6
   through-node intersections, and 7 long connectors, so those lines were
   removed and the geometry-safe source retained. This is the main remaining
   route-tooltip/visibility risk; it is not a missing functional availability
   gate.

2. Several coordinates differ from the addendum's ideal reflow. The most visible
   differences are Five Provinces (`ireland_five_province_mandates` at `(23,5)`
   rather than `(25,5)`, `ireland_federal_republic` at `(15,7)` rather than
   `(21,7)`, and capstone at `(23,12)` rather than `(25,11)`),
   `ireland_a_law_for_two_orders` at `(-32,8)` rather than `(-34,8)`, and the
   convergence `ireland_five_courts_of_the_otherworld` at `(23,13)` and
   `ireland_fivefold_high_kingdom_of_two_irelands` at `(8,26)` rather than the
   addendum's `(16,25)` and `(4,27)`. Reflowing these is outside this bounded
   audit because the current render is crossing-free.

3. `ireland_no_single_story_rules_them_all` records its intermediate readiness
   at `ireland_regional_compact_count >= 4`, while its wording says five lawful
   compacts are needed before Five Courts. The final
   `ireland_five_courts_convergence_ready` trigger still requires at least five,
   so this is a wording/flag-state risk rather than an early convergence bypass.

4. MCP reports nine nonblocking layout detour/staircase diagnostics (existing
   paths such as de Valera stewardship, German channel/IRA council, clerical
   failure, northern mandates, federal compact, and provincial council), plus
   one unrelated vanilla `continuous_restrict_freedom_desc` localisation
   diagnostic. There are no crossing, intersection, or long-connector
   diagnostics.

5. The full tree retains 150 older 100x88 legacy DDS assets. This is outside the
   requested exceptional tranche; all 38 tranche assets are correctly sized
   94x86. No thumbnail was changed.

## Icon coverage

| Route tranche | Count | Regular definition | Shine definition | Asset result |
| --- | ---: | --- | --- | --- |
| High Kingship | 7 | `interface/ireland_icons.gfx` | `interface/ireland_focus_shine.gfx` | 7/7 regular + 7/7 shine; DDS RGBA 94x86 |
| Five Provinces | 9 | `interface/ireland_icons.gfx` | `interface/ireland_focus_shine.gfx` | 9/9 regular + 9/9 shine; DDS RGBA 94x86 |
| Otherworld | 18 | `interface/ireland_icons.gfx` | `interface/ireland_focus_shine.gfx` | 18/18 regular + 18/18 shine; DDS RGBA 94x86 |
| Convergence | 4 | `interface/ireland_icons.gfx` | `interface/ireland_focus_shine.gfx` | 4/4 regular + 4/4 shine; DDS RGBA 94x86 |
| **Exceptional total** | **38** | `GFX_focus_ireland_<id>` | `GFX_focus_ireland_<id>_shine` | **38/38 complete; no duplicate texture paths** |

The full source tree also has all 256 regular icon references registered and all
256 corresponding `_shine` names resolved across the interface GFX files,
including the pre-existing public-family and expansion shine files. Exceptional
shine definitions have matching animation mask/texture files and one-shot
animation blocks. No icon IDs were changed in this audit.

## Localisation and reward audit

- All 256 focus title and `_desc` keys resolve.
- All 38 exceptional title, description, and custom reward-tooltip keys resolve;
  reward text matches the finite event/mission/decision/idea/variable effects.
- No exceptional reward grants an unbounded free division, equipment stockpile,
  core, ownership, or war goal.
- Localisation files use UTF-8 with BOM and the parser found no duplicate keys.
- Nonblocking wording issue: `ireland_no_single_story_rules_them_all` describes
  the five-compact threshold while the component-ready flag is raised at four;
  the final trigger correctly requires five.
- A generic `available_mio_tt` reference remains unresolved in two pre-existing
  nonexceptional focus blocks; it was not changed because it is outside the
  current tranche.

## AI behavior

All 256 focus IDs have at least one reference in
`common/ai_strategy_plans/IRE_ireland_strategy_plans.txt`. Every exceptional
focus has a historical factor `0` entry plus a route-aware plan reference:

| Family | Current plan behavior |
| --- | --- |
| High Kingship | Historical zero; independent household 10, captured 4, sacral 3, recovery 4, with route-specific terminal factors. |
| Five Provinces | Historical zero; federal 10, confederation 7, Empty Chair 6, sovereignty/pentarchy 3, and route failure factors. |
| Otherworld | Historical zero; balanced compact 10, containment 6, Tuatha 4, Fianna 5, regional 6, exploitation 2, and sealing/recovery gates. |
| Convergence | Historical zero; all four conclusions receive low route-aware factor 1 references and are gated by their readiness triggers. |

No missing AI plan reference or historical-AI leakage was found. No AI file was
changed.

## Narrow patch applied

Changed file:

- `common/national_focus/ireland_focus_tree.txt`

Changed focus IDs:

- `ireland_muster_a_modern_fian`
- `ireland_no_host_without_equipment`
- `ireland_guardians_of_two_irelands`

Before: `FOCUS_FILTER_POLITICAL` + `FOCUS_FILTER_ARMY_XP`.  
After: `FOCUS_FILTER_POLITICAL` only.

These focuses establish a template/readiness/mission/idea state and do not grant
direct Army XP. Removing the misleading Army XP filter aligns the UI filter with
the actual reward contract and does not alter prerequisites, availability,
mutual exclusions, route state, or rewards. No localisation keys or icon IDs
changed. The focus file has a large concurrent parent diff; review the three
filter-line edits in context rather than treating the whole file diff as this
subagent's patch.

## Fresh validation and artifacts

Fresh `hoi4.focus_inspect` after the final source state:

- 256 focuses / 265 connectors
- crossing count `0`
- node-intersection count `0`
- long-connector count `0`
- bounds x `-44..31`, y `0..26`; column span `75`, row span `26`
- minimum spacing `2`, too-close count `0`
- artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/44d62168666857ccdecf31bb40fcae97943f1f9effa4366971e7a6601a878f1b/bc8adb9a30fe9cf3dc5afa6ba07cf0467360fd8476e36c868b52180d359d0c1d/focus-inspect.3a975d54fc65df5e.json`

Fresh `hoi4.focus_render` after the final source state passed validation:

- HTML: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/7004185dbbb37fc575a86921b99717c49b41889578bbf7f3975842ecb85fbe2a/b28ca2d889efe072548d412a902775deb3002e741f79df6cee59b817740e3feb/ireland_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/758b707b81e9bbf4167f383841d6f03b0a07fdaf79b6b76aa0c9c64856c9cef7/f849efdd89fdd909649e9493b71eeffd756fa1bbbabbdeca427c7e49e0ba8013/ireland_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/021d909a2802e3685b4c7054abd9e06e6436437fda17d963704d5ac5328922a3/75d90796b1a4ca1f6e7bc56ab8ddff577758b53180a278b064f38f335c72d339/ireland_focus_tree.focus.json`
- source map: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/3324532cbc6449261d95842af8b2c45939c0cd882df9d696beecd13011190d38/814687ded2e9124c17bb9955c86a7d5cf113a2db3b35601c09c8d258ac34cb08/ireland_focus_tree.focus.source-map.json`
- plan: `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/5af4cfd03839d1bfdc0743281380ee5b8e1861387ee841047408cf5058fb983f/d874139a8a7d4b03780a9194301ca08324b80d7bc388eb658ed09fb169bd1edb/ireland_focus_tree.focus.plan.json`
- rendered dimensions: `13504 x 3252`

Additional task-specific checks:

- Parsed all source focus IDs, connector counts, filters, prerequisites,
  availability blocks, rewards, and AI plan references.
- Parsed all interface GFX registrations and verified every exceptional regular
  and shine sprite; Pillow inspection confirmed all 38 exceptional DDS files are
  RGBA 94x86 with no duplicate texture paths.
- Parsed all Ireland focus/localisation keys; all exceptional title, description,
  and reward tooltip references resolve.

Skipped meaningful validation: `hoi4.focus_raster` was attempted but timed out
after 180 seconds. Source-level GFX/DDS verification and the validated SVG render
cover icon wiring; no live game session was run by this subagent.

## Handoff / remaining risks

Parent review should focus on the five visible prerequisite simplifications in
the convergence/Otherworld capstone band, the addendum coordinate deviations,
and the four-vs-five intermediate readiness wording. The current source is
geometry-safe and functionally gated, but the visible focus-tree tooltip may not
expose every component requirement until those connectors are reflowed as part
of a separately approved layout pass.

No broad route redesign, historical archive expansion, new formable chain,
fallback tree, thumbnail edit, localisation rewrite, GFX rewrite, AI rewrite,
or commit was made by this subagent. Handoff path:
`docs/plans/ireland_country_package/subagent_handoffs/final_focus_audit_256_2026-08-14.md`.
