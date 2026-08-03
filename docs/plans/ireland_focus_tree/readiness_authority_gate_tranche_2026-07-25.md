# Ireland readiness authority gate tranche — 2026-07-25

## Scope

This tranche closes four canonical admission gaps in the National Readiness and Neutrality Incident action surfaces. It does not add passive political power, transfer territory, grant buildings, create cores, or replace the linked missions.

## Canonical rows addressed

| Action | Canonical proof | Implemented admission |
| --- | --- | --- |
| Build a Coastwatch Sector Network | Marine and Coast Watching Service active | `slopx_ireland_coastwatch_service_active`; full control of state 134 with infrastructure-connected post site |
| Install Harbour Defences | valid port authority and transferred or controlled harbour | `slopx_ireland_harbour_defence_authority`; full control of state 135 plus port authority/transfer/project proof |
| Organise Marine Patrols | Marine Service or route equivalent | `slopx_ireland_marine_patrol_authority`; Marine Service or named shipping route, full controlled Cork port, industrial capacity |
| Intercept an Airspace Violation | detected aircraft and available warning or Air Corps response | `slopx_ireland_air_intercept_response_authority`; Air Warning route or command authority with state-113 air base |

## Source and engine basis

- The local decision map and canonical Part 5 table identify the four service/authority proofs and named operating regions.
- The existing focus and runtime flags are the route records: Coastwatch, Air Warning, Treaty Port transfer, port defence, Maritime Protection, Maritime Reserve, and shipping-route completion flags.
- The existing scripted map helpers establish full-control and infrastructure/industrial checks for states 134, 135, and 113.
- Vanilla state 113 provides the reference air base and naval base used by the air-response and maritime precedents; no new building is granted by these admission triggers.

## Files changed

- `common/scripted_triggers/slopx_ireland_triggers.txt`
- `common/decisions/slopx_ireland_decisions.txt`
- `localisation/english/slopx_ireland_l_english.yml`
- `docs/slopx_dynamic_effects.md`

## Validation evidence

- Each new scripted trigger has one definition and is consumed by the intended decision.
- The Coastwatch action now uses state 134 and an infrastructure-connected site, matching its western-sector label instead of its former Dublin-only check.
- Harbour and Marine actions now require full control instead of mere ownership; the Marine action also requires a controlled port industrial complex.
- The air action still requires the active airspace incident, fighters, and fuel, and now also requires the warning/response authority proof.
- Localization was restored and verified as UTF-8 with BOM after the edit.

## Remaining gates

- Engine-side trigger parsing, live decision availability, mission outcomes, foreign reaction, and the complete scenario matrix remain unrun because this task does not launch HOI4.
- Source-clearance, asset, and full canonical completion ledgers remain open in the project status documents.
