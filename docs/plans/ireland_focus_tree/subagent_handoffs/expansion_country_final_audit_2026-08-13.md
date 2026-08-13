# Ireland country-package final audit — 2026-08-13

## Scope and verdict

This handoff audits the current shared working tree for Ireland's country
integration: country history, the 67 mod route characters, all 45 advisor
cards and lifecycle rules, five advisor pools, seven ordinary industrial
concerns, the Ford Cork and Harland & Wolff MIOs, nine company focuses and
contracts, family locks, and historical/ahistorical AI. Focus coordinates,
territorial events/decisions, unrelated concurrent edits, and `thumbnail.png`
were not changed.

**Verdict:** the package is statically cross-wired after one narrow
localisation repair. The prior audit found that 34 of the 45 advisor
`idea_token` IDs had no explicit localisation name key; those keys now resolve
to the exact character display names. This fresh pass found no further missing
or duplicate localisation, country, advisor, MIO, company, contract, event,
Parliament, focus, icon, or AI reference in the audited surfaces.

The source currently contains **215 gameplay focus blocks**. The separate
`focus_tree = { id = ireland_focus_tree }` wrapper is not a gameplay focus;
an earlier count included that wrapper. This audit did not alter focus layout
or count.

## Required references consulted

- `AGENTS.md`.
- `.agents/skills/hoi4-subagents/SKILL.md`,
  `.agents/skills/hoi4-focus-trees/SKILL.md`, and
  `.agents/skills/hoi4-feature-assets/SKILL.md`.
- Offline Paradox wiki pages in `paradox_wiki/` for data structures, triggers,
  effects, modifiers, localisation, scopes, on actions, event/decision/idea/AI
  modding, country creation, national focuses, characters, MIOs, and graphical
  assets.
- Vanilla documentation in
  `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`
  for effects, triggers, script concepts, dynamic variables, and related
  engine syntax.
- Vanilla Ireland country/history/character files and vanilla MIO/industrial
  concern precedents.

## Country-package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Tag/history | Pass | `history/countries/IRE - Ireland.txt` uses the existing `IRE` tag, capital `113`, `IRE_1936`, and `IRE_1939`; 67 mod route characters are recruited. |
| Opening politics | Pass | 1936 start remains democratic, elections enabled, 98/1/1 popularity, 3 research slots, and 10 convoys. |
| 1939 history | Pass | The later history block keeps the vanilla-style OOB/technology transition and does not create a second tag or capital. |
| Characters | Pass | `common/characters/ireland_route_characters.txt` has 67 top-level mod character definitions; every mod history recruit resolves. |
| Advisors | Pass | Exactly 45 definitions with unique `idea_token`, slot/traits, IRE allowance, route/date/office gates, and runtime lifecycle calls. |
| Advisor cards | Pass | `interface/ireland_advisors.gfx` and the approved 2026-08-13 manifest each contain 45 cards; all 45 runtime DDS files exist. |
| Advisor localisation | Repaired/pass | All 45 `idea_token` IDs now have BOM-safe name keys in `localisation/english/ireland_l_english.yml`; no duplicate keys. |
| Political families | Pass | The five gateway focuses are mutually exclusive and each requires `NOT = { has_country_flag = ireland_political_family_committed }` before setting one durable family flag. |
| Industrial concerns | Pass | Seven ordinary `industrial_concern` ideas have IRE allowance, unlock flags, costs, traits, modifiers, research, icons, and name/description localisation. |
| MIOs | Pass | Ford Cork and Harland & Wolff are two real MIO organizations with vanilla generic includes, gated availability, traits, icons, localisation, and focus size grants. |
| Company focuses | Pass | Nine company focuses set the corresponding flags, show the concern/MIO tooltip, and give the documented material reward. |
| Contracts | Pass | Nine one-shot decisions are visible from the nine company flags and have localisation, costs, effects, icons, and AI weights. |
| Historical AI | Pass (static) | `IRE_ireland_historical` follows the shared constitutional/material trunk, chooses the democratic gateway, and includes ordinary company focuses while withholding Harland & Wolff until the lawful Northern route. |
| Ahistorical AI | Pass (static) | Family and route-reactive plans cover all family/route focus references; all 215 plan references resolve to gameplay focus IDs. |

## File-surface checklist and identifiers

### History, characters, leaders, and advisors

- `history/countries/IRE - Ireland.txt`: `capital = 113`, `oob = "IRE_1936"`,
  `ireland_initialize_campaign = yes`, and the 1939 transition remain intact.
  All 67 `ireland_*` history recruits resolve to definitions in
  `common/characters/ireland_route_characters.txt`; the remaining vanilla
  `IRE_*` recruits resolve to the vanilla Ireland character file.
- `common/characters/ireland_route_characters.txt`: 67 top-level definitions,
  45 advisor definitions, 45 unique `idea_token` values, and 45 small advisor
  portrait references. The roster uses historical people for one-person
  offices; collective route offices use institutional names and emblems rather
  than invented personal random-name pools. No opposite-gender portrait/name
  pairing or unsupported female metadata was found.
- `common/scripted_effects/ireland_runtime.txt`: each of the 45 advisor idea
  tokens has a matching `deactivate_advisor`; each advisor character has a
  matching retirement path. Date limits (for example Hyde/O'Kelly,
  O'Donovan/command, Michael Price, Charles Kerins, and Ailtirí successors) are
  paired with route/pool/office guards. Thekla Beere, P. J. Coughlan, and J. J.
  Walsh retain their pool-specific retirement guards.
- `common/scripted_triggers/ireland_triggers.txt`: constitutional, republican,
  Fine Gael, Norton, Clann, vocational/clerical, IRA, Congress, Blueshirt,
  restoration, and Ailtirí advisor selectors are present and namespaced.

### Political family flags and profile locks

The gateway focus/flag crosswalk is:

| Gateway focus | Durable family flag | Lock |
| --- | --- | --- |
| `ireland_republican_government` | `ireland_family_democratic` | `ireland_political_family_committed` required false before completion |
| `ireland_congress_reform_bridge` | `ireland_family_communist` | same durable lock |
| `ireland_oduffy_network_revival` | `ireland_family_fascist` | same durable lock |
| `ireland_vocational_constitution` | `ireland_family_oligarchic` | same durable lock |
| `ireland_high_king_evidence_gate` | `ireland_family_restoration` | same durable lock |

The family flags are intentionally durable: the player-facing gateway
localisation describes the competing families as closed. Runtime profile
selection clears transient profile flags and selects one ordered profile; it
does not silently reopen a committed family.

### Industrial concerns and MIOs

Seven ordinary concern IDs in `common/ideas/ireland_industrial_concerns.txt`:

1. `ireland_company_electricity_supply_board`
2. `ireland_company_irish_sugar_company`
3. `ireland_company_turf_development_board`
4. `ireland_company_great_southern_railways`
5. `ireland_company_aer_lingus_air_link`
6. `ireland_company_irish_shipping_registry`
7. `ireland_company_steel_holdings`

The two vehicle/ship producers are correctly represented as MIOs rather than
ordinary concerns:

- `ireland_ford_cork_works_organization` in
  `common/military_industrial_organization/organizations/ireland_organizations.txt`
  includes `generic_motorized_mechanized_organization` and is gated by
  `ireland_company_ford_cork_unlocked`.
- `ireland_harland_wolff_belfast_organization` includes
  `generic_task_force_ship_organization` and is gated by
  `ireland_company_harland_wolff_unlocked`; the focus and contract additionally
  require lawful state `119` ownership/control and Northern final review.

Company focus/flag/preview crosswalk in
`common/national_focus/ireland_focus_tree.txt`:

| Focus | Unlock flag | Preview |
| --- | --- | --- |
| `ireland_irish_sugar_company_charter` | `ireland_company_sugar_unlocked` | `ireland_company_irish_sugar_company` |
| `ireland_esb_supply_contracts` | `ireland_company_esb_unlocked` | `ireland_company_electricity_supply_board` |
| `ireland_turf_development_board_programme` | `ireland_company_turf_unlocked` | `ireland_company_turf_development_board` |
| `ireland_great_southern_railways_contract` | `ireland_company_railways_unlocked` | `ireland_company_great_southern_railways` |
| `ireland_ford_cork_works_agreement` | `ireland_company_ford_cork_unlocked` | `ireland_ford_cork_works_organization` |
| `ireland_aer_lingus_air_link` | `ireland_company_aer_lingus_unlocked` | `ireland_company_aer_lingus_air_link` |
| `ireland_irish_shipping_registry` | `ireland_company_shipping_unlocked` | `ireland_company_irish_shipping_registry` |
| `ireland_steel_holdings_programme` | `ireland_company_steel_unlocked` | `ireland_company_steel_holdings` |
| `ireland_harland_and_wolff_access` | `ireland_company_harland_wolff_unlocked` | `ireland_harland_wolff_belfast_organization` |

`interface/ireland_industrial_concerns.gfx` registers nine company sprites and
all nine referenced DDS files exist under
`gfx/interface/ideas/ireland/companies/`. All nine focus icon references are
also registered in the focus GFX surfaces. The nine contract IDs are:
`ireland_contract_esb_grid_works`, `ireland_contract_transport_fleet`,
`ireland_contract_merchant_tonnage`, `ireland_contract_state_materials`,
`ireland_contract_ford_motor_works`, `ireland_contract_aer_lingus_transport`,
`ireland_contract_turf_fuel_reserve`, `ireland_contract_steel_foundry`, and
`ireland_contract_belfast_refit`.

### AI and playability

- `common/ai_strategy/ireland_ai_strategy.txt` contains the durable profile
  registry and uses `original_tag = IRE` on the Ireland strategies.
- `common/ai_strategy_plans/IRE_ireland_strategy_plans.txt` contains the
  historical, route-reactive, five family, route, and temporary overlay plans.
  Static crosswalk: 215 gameplay focus IDs in the tree and 215 Ireland focus
  references in plans, zero missing references.
- Historical AI follows the shared institutional, neutrality, readiness,
  provision, and ordinary company lane before the democratic route. It does not
  queue the Blueshirt, Congress, vocational, restoration, or Harland & Wolff
  route as a historical company choice.
- Ahistorical AI enables family programmes from their durable family flags and
  then uses route/profile plans. Runtime priority/support flags are cleared and
  recomputed by the profile helper; Ford and Harland MIO AI weights consume the
  corresponding provision/readiness priority/support flags.
- Static setup evidence shows no new unsupported army, navy, air, production,
  supply, or state ownership assumptions in the audited country package. A live
  game playthrough was not run by this subagent.

## Narrow patch made

Changed file:

- `localisation/english/ireland_l_english.yml`: added 34 missing advisor
  `idea_token` name keys, using the exact display names from
  `common/characters/ireland_route_characters.txt` (including accents and
  apostrophes). The file retains its UTF-8 BOM and uses no `:0` keys.

Before: 45 advisor tokens existed, but 34 had no explicit localisation key and
would rely on the literal character name fallback.

After: all 45 advisor tokens have one exact name key; no duplicate localisation
keys remain. This changes presentation only and does not alter advisor gates,
traits, costs, portraits, or lifecycle behavior.

No other gameplay, focus, map, decision, event, or asset source was changed by
this audit. No commit was created.

## Validation evidence

- Character parser: 67 mod definitions; 45 advisor definitions; 45 unique
  tokens; 67/67 mod history recruit IDs resolve.
- Lifecycle crosswalk: 45/45 advisor tokens have `deactivate_advisor` and
  retirement calls; advisor small-sprite set is exactly 45/45 against
  `interface/ireland_advisors.gfx`.
- Advisor assets: manifest has 45 cards, approved state
  `approved by advisor_card_independent_approval_2026-08-13`, zero missing
  runtime DDS files, and zero runtime SHA-256 mismatches.
- Localisation: UTF-8 BOM `EF-BB-BF`; 45/45 advisor token name keys present;
  zero duplicate actual keys and no `:0` keys; all 215 gameplay focus title,
  description, and reward keys are present (the two `available_mio_tt` calls
  resolve through vanilla English); 7/7 ordinary concern names/descriptions,
  2/2 MIO names, 9/9 focus names/descriptions, and 9/9 contract
  names/descriptions are present.
- Decision/event/Parliament localisation: 233 decision IDs across the three
  Ireland decision files have names and descriptions; 1,075 decision
  requirement-tooltip references resolve; 511 country-event IDs and their
  title/description/option references resolve; and all 90 Parliament, Northern
  ledger, and concealed-evidence GUI text/tooltip references resolve.
- Company assets: 9/9 company sprite definitions and 9/9 texture files
  resolve; all nine company focus icon references resolve.
- Focus/AI crosswalk: all 215 gameplay focus IDs have title, description, and
  reward localisation; all 215 Ireland focus references in plans resolve; the
  two `available_mio_tt` reward references resolve through vanilla English
  localisation; all five family gateway locks and family programme enables
  are present.
- Vanilla precedent: industrial concern syntax was compared with vanilla
  country concern files; MIO includes/traits/parent syntax was compared with
  vanilla generic MIO organizations.

## Remaining risks and blockers

- No live HOI4 start, advisor hire/retire, MIO UI, focus AI queue, or save/load
  test was run in this audit; runtime UI behavior remains for parent review.
- No focus-count discrepancy remains: the checked-out source has 215 gameplay
  focuses, matching the task wording. The wrapper `ireland_focus_tree` is not
  counted as a focus block.
- Territorial event/decision behavior and focus coordinate/layout review were
  explicitly excluded. They are not claimed as part of this country-package
  handoff.
- No country-package simplification was introduced. The only deliberate scope
  exclusions are the parent-directed coordinate and territorial surfaces.
