# Foreign-Channel Exposure Burden Tranche

Feature slug: `ireland_focus_tree`

Status: source-level implementation tranche; HOI4 was not launched.

## Canonical gap

The Part 5 decision map treats foreign-channel work as a bargain with named external leverage and exposure, not as a free diplomatic button. `Formalise Plan W Liaison`, `Mobilise Diaspora Relief`, `Receive a German Emissary`, `Seek Vatican Humanitarian Mediation`, and `Convene a Neutral States Consultation` already had their route, partner, law, mission, or material gates, but their completion effects did not consistently record the external burden described by the map.

## Implemented contract

- `Formalise Plan W Liaison` now records `+5 Foreign Exposure` beside its existing British-Leverage bargain.
- `Mobilise Diaspora Relief` now records `+3 American Leverage` and `+5 Foreign Exposure` after its convoy commitment.
- `Receive a German Emissary` now records `+5 Foreign Exposure` beside its existing German-Leverage bargain.
- `Seek Vatican Humanitarian Mediation` now records `+3 Vatican Leverage` and `+5 Foreign Exposure` before opening its mediation mission.
- `Convene a Neutral States Consultation` now records `+5 Foreign Exposure` without inventing sponsor leverage for a neutral forum.
- The deltas are centralized in `common/script_constants/slopx_ireland_constants.txt`, and the action descriptions/requirement tooltips name the burden and source-specific result.

## Boundary and cleanup

This tranche does not grant aid, equipment, units, fuel, shipping, territory, cores, recognition, alignment, offices, administration, or passive Political Power. It does not merge source channels or turn the neutral forum into a sponsor. Existing foreign-reaction windows, mission deadlines, failure/escalation records, and cleanup remain the owning lifecycle's responsibility.

## Evidence

- `common/decisions/slopx_ireland_decisions.txt`
- `common/script_constants/slopx_ireland_constants.txt`
- `localisation/english/slopx_ireland_l_english.yml`

Live partner invalidation, reaction ordering, mission completion, AI queue behavior, engine-reference checks, and cleanup scenarios remain not-run.
