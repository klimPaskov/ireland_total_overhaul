# Ireland Naval Service and Atlantic Defence

## Player-facing concept

Ireland's naval game is a small-state maritime service, not a late-game battleship ladder. The country begins with an exposed coastline, a fragile merchant lifeline, scattered harbour administration, and a defence establishment that can count men more easily than it can keep a vessel at sea. The branch turns those weaknesses into a sequence of choices: coastal observation, harbour control, patrol craft, marine infantry, convoy protection, and eventually a lawful Atlantic service.

The presentation should be practical and period-specific. Use the viewpoint of harbourmasters, coastwatch crews, Army officers, merchant captains, and cabinet ministers. Keep the public record visible—ships, fuel, crews, dockyard time, and port capacity—while leaving the most sensitive intelligence implications to the agency and event surfaces. Avoid generic “build a navy” language and avoid presenting Ireland as a hidden great power.

## Architecture map

```text
State Still Defined -> Defence Estimates -> Command Audit -> Port and Coast Audit
                                      |
                                      +-> Rebuild the Marine Service
                                      |      |
                                      |      +-> Requisition Trawler Hulls -> Coastal Patrol Flotilla
                                      |      |                                  |
                                      |      |                                  +-> Marine Service Reserve
                                      |      |                                  +-> Atlantic Convoy Office
                                      |      |
                                      |      +-> Establish a Naval Staff -> Harbour Defence Board
                                      |                                             |
                                      |                                             +-> Cobh Dockyard Programme
                                      |                                             +-> Lough Swilly Watch
                                      |
                                      +-> Coastwatch (shared readiness lane)
                                             |
                                             +-> Neutral Approaches Patrol
                                             +-> Atlantic Defence League
```

The common maritime trunk is compatible with political, industry, neutrality, and Northern-settlement routes. The two internal naval lanes are a choice of emphasis, not mutually exclusive ideologies:

| Lane | Role | First payoff | Late payoff |
| --- | --- | --- | --- |
| Marine Service | cheap patrol craft, rescue, fisheries protection, marine infantry, convoy discipline | patrol-craft production and a deployable coastal template | a repeatable merchant-protection and emergency-escort decision family |
| Naval Staff | port administration, repair, signals, harbour defence, foreign naval liaison | dockyard and naval-base improvements with a named staff | a coastal defence doctrine, agency access, and a regional maritime pact |

## Focus groups and route logic

Working focus labels are implementation anchors, not final localization.

1. `rebuild_the_marine_service` is the branch opener. It requires the existing port-and-coast audit and records a maritime institution flag. It unlocks the naval filter, the first maritime decision group, and the basic naval unit names.
2. `requisition_trawler_hulls` and `coastal_patrol_flotilla` trade civilian capacity and convoy stock for a small surface-screen/patrol programme. They should grant a production route or equipment stockpile only once, then expose a repeatable patrol decision with fuel and convoy costs.
3. `marine_service_reserve` creates a named coastal/marine division template and a reserve mobilisation decision. It should use manpower, infantry equipment, support equipment, and training time; it must not become a free repeated-division loop.
4. `establish_a_naval_staff` opens the staff lane. It improves a named port, creates a repair/signal institution, unlocks naval intelligence agency availability, and grants a research bonus for naval doctrine or electronics instead of a flat stack of small modifiers.
5. `harbour_defence_board`, `cobh_dockyard_programme`, and `lough_swilly_watch` tie geography to the existing map. The rewards should be naval-base/coastal-fort/radar or infrastructure changes in the relevant controlled state, with a decision to prioritize repairs under threat.
6. `atlantic_convoy_office` and `neutral_approaches_patrol` connect to the existing Provision/Readiness/neutrality values. Their visible costs are convoys, fuel, manpower, and a bounded amount of dockyard time; their visible outputs are maritime provision, warning, rescue, and shipping protection.
7. `regional_maritime_defence_pact` is the late convergence point. It can cooperate with a regional defence league or Atlantic diplomacy route, but it must check that Ireland has a live port, a functioning maritime institution, and a real contribution to offer.

Historical AI mode should prefer the common maritime trunk and defensive/coastwatch lane when Ireland has the branch available. It must not enter the mod's alternate ideological or Otherworld paths while historical focuses are enabled; the existing historical-AI guard remains authoritative for those route-entry focuses.

## Military package

Add the following historical/plausible 1936–1940 templates in the Ireland OOB and name groups:

- `Coastal Defence Battalion`: infantry with engineers and a small artillery/anti-air support identity; intended for ports and fixed defence.
- `Marine Service Company`: marines with engineers and recon; a scarce, expensive amphibious/security formation rather than a normal infantry replacement.
- `Coastal Watch Brigade`: infantry with engineers, recon, and signal support; used by the coastwatch and harbour-defence decisions.
- `Emergency Reserve Division`: a restrained infantry template for the national reserve route, created once and improved through later focuses/decisions.

The starting OOB should preserve the vanilla Irish army, then add only the historical coastal service/patrol elements that the selected date and available equipment support. Naval units must be gated by the relevant technology, dockyard, and production rules. Do not spawn a full battle fleet at game start.

## Ship and formation names

Create country-specific name groups for light craft, destroyers, submarines, and merchant/convoy vessels. Use attested Irish maritime names where possible: `Muirchú`, `Fort Rannoch`, `Fortbaugh`, `Irish Poplar`, `Irish Plane`, `Irish Elm`, `Irish Beech`, `Irish Larch`, `Irish Ash`, `Irish Willow`, `Irish Hawthorn`, `Irish Rose`, `Irish Cedar`, and `Irish Hazel`. Add geographic and civic fallback names based on Irish ports, rivers, provinces, and coastal landmarks. Keep the prefix `LÉ` for a naval-service identity only if the route has actually created that service; use `MV`/`SS`-style merchant naming for the commercial list.

Division name groups should cover Irish brigades, marine service formations, coastal watch formations, and reserve divisions, with ordered names for the first historical formations and fallbacks for expansion.

## Intelligence agency

Add an Ireland-specific agency definition under `common/intelligence_agencies/` with a two-frame 234x119 logo. It becomes the default for IRE and is available for original-tag Ireland. The name pool should support three route-appropriate institutional names: Army intelligence (`G2`), a coastwatch/harbour service, and a neutral shipping intelligence office. The logo should reuse a sourced Irish harp/official-state emblem in a restrained two-frame agency presentation; do not use a decision icon or a focus icon.

The agency should connect to the naval branch through one meaningful unlock: naval intelligence, coastal reconnaissance, or convoy-risk operations. It should not grant a broad intelligence-power windfall or bypass the existing evidence/neutrality gates.

## Decisions and gradual disclosure

The decision category should reveal maritime actions in phases:

- Early: inspect ports, assign coastwatch sectors, and record a maritime baseline.
- Middle: commission patrol craft, train the Marine Service Reserve, repair a port, and protect a named route.
- Late: run emergency escort, form a regional maritime pact, or settle postwar merchant-service obligations.

Each action must state its direct cost using texticons (`£pol_power`, `£command_power`, `£navy_experience`, `£convoys`, `£fuel`, `£manpower`) and a short named material cost. Tooltips explain what Provision, Readiness, Maritime Protection, and Neutrality Integrity measure. Do not expose every late action in the opening category.

## AI and balance

The naval branch uses route-specific strategy weights:

- historical AI: maritime trunk, coastwatch, port defence, and convoy protection; no alternate route entry while historical focus mode is on;
- democratic/neutral AI: Naval Staff and Atlantic Convoy Office, avoiding offensive war goals;
- military-route AI: Marine Service Reserve and Harbour Defence Board first, accepting higher command costs;
- foreign-dependent AI: staff/lender route only after a valid sponsor channel exists, with a dependency penalty and no free ships.

Exploit checks cover repeated reserve division creation, repeated convoy refunds, free dockyard loops, agency stacking, and a patrol decision that can be clicked without fuel/convoy or active port capacity. Focus rewards should be rounded to the repository's established tuning cadence unless an engine requirement makes a different value necessary.

## Assets and documentation

Register all focus, decision, category, BoP, national-spirit, agency, and report-art sprites before using them. The naval branch needs a distinct navy/coast palette, proper BoP side icons, an agency logo, and report images for patrol/rescue/harbour review. Reuse existing Irish sourced symbols only when their dimensions and role match the surface; otherwise create a dedicated asset and record source, dimensions, path, GFX name, and fallback.

Update the route coverage table, icon manifest, localization handoff, and this spec's implementation handoff with changed identifiers and validation evidence. The implementation report must list any historical detail that remains an alternate-history interpretation rather than an attested 1936 institution.
