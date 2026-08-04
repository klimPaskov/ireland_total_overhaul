# Occupation and regional authority gate tranche

Feature slug: `ireland_focus_tree`  
Namespace: `ireland`  
Date: 2026-07-25

## Purpose

This tranche closes three canonical admission gaps in the Northern occupation and regional-external decision surfaces. The actions now require an operational unit or authority appropriate to the named objective instead of treating a broad route or occupation flag as sufficient.

## Canonical requirements covered

- `Disarm Paramilitary Organizations` — Derry and Foyle: a Northern unit, intelligence basis, lawful security authority, manpower, and reviewable security burden.
- `Integrate or Devolve Military Command` — Belfast Urban and Harbour: a Northern unit, controlled state 119, support equipment, Army Experience, command readiness, and dynamic command cost.
- `Offer Protectorate Treaty` — Dublin Metropolitan Region: a recognised authority or proven Northern war/conquest/bargain record, a committed regional route, state-113 ownership, British-Flexibility ceiling, and a foreign-reaction window.

## Implementation

`common/scripted_triggers/ireland_triggers.txt` now provides:

- `ireland_paramilitary_disarm_authority`, requiring a division in state 119, Intelligence Readiness above the investigation floor, and Public Order, Security Under Law, or Vet and Rebuild Policing authority.
- `ireland_protectorate_authority_valid`, requiring a recognised liberated authority, Northern war plan, completed coercive campaign, or Northern wartime bargain.

The decision consumers remain in `common/decisions/ireland_decisions.txt` and retain their existing capacity, route, ledger, map, political-power, command-power, cooldown, AI, and cleanup logic. Military command additionally charges the authored Army Experience cost on completion. The protectorate action calls `ireland_open_foreign_reaction_window = yes` and does not grant a subject, territory, core, industry, equipment, unit, fuel, shipping, administration, alignment, office, or recognition.

The player-facing requirements in `localisation/english/ireland_l_english.yml` name the current unit, intelligence, law, material, authority, and foreign-reaction gates. The reusable trigger contracts are documented in `docs/ireland_dynamic_effects.md`.

## Static evidence

- The disarm, military-command, and protectorate consumers each reference their intended authority trigger exactly once.
- State 119 unit presence is checked with `num_divisions_in_states`; no action effect creates or moves a division.
- Support equipment and Army Experience are checked and charged by the military-command action; the charge is negative and cannot exceed the project command-power ceiling.
- Protectorate authority is distinct from route access, Northern control, occupation, settlement, integration, and core review. No new core or territorial effect was added.
- Runtime icon work remains separate: final goal DDS files live under `gfx/`, while direct-source generation and audit intermediates stay under temporary `assets/` staging.

## Remaining validation and live checks

The local static checks still need to be rerun after this tranche for brace balance, unsupported operators, trigger definition/consumer counts, localisation BOM/key uniqueness, and source-map alignment. The offline HOI4 MCP focus workspace is not registered for this repository, so MCP focus rendering remains an environment blocker; HOI4 itself is intentionally not launched.

## Follow-up

Continue the action-material review for aircraft, ships, local-support records, and foreign-channel safeguards. Then run the full decision/mission, country-package, localisation, asset, AI, and feature-completion audit programme before any overall completion claim.
