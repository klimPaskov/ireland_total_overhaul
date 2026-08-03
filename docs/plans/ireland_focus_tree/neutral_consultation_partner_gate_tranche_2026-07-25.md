# Neutral consultation partner gate tranche — 2026-07-25

Feature slug: `ireland_focus_tree`  
Namespace: `slopx`

## Canonical requirement

The Part 5 decision lifecycle and the decision/mission map define `Convene a Neutral States Consultation` as a political action that requires two or more valid neutral or small-state partners. A single foreign-safeguards flag is not sufficient evidence of two participants.

## Implementation

The action now consumes `slopx_ireland_neutral_consultation_partners_valid`. The composite trigger requires both:

1. an open Vatican channel whose named Italian/Vatican partner still exists and has not capitulated; and
2. the separate neutral-states forum channel opened by `Foreign Safeguards`.

The Holy See is the authored small-state mediator and the neutral-state forum is the second neutral partner. Their channel flags remain separate, so the action cannot count one focus or one generic foreign capability twice.

The action still requires Dublin Metropolitan Region, the foreign category capacity and dynamic scarcity costs. Completion only records the consultation and opens the foreign-reaction window; it grants no alignment, recognition, territory, core, industry, equipment, unit, fuel, shipping, administration, office, or free-supply outcome.

## Evidence

- Trigger: `common/scripted_triggers/slopx_ireland_triggers.txt`
- Action admission: `common/decisions/slopx_ireland_decisions.txt`
- Player-facing requirements: `localisation/english/slopx_ireland_l_english.yml`
- Reusable-helper contract: `docs/slopx_dynamic_effects.md`
- Canonical row: `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md` and `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md`

## Remaining proof

Static script and localisation audits are required after the edit. A live engine scenario still needs to prove that the action is hidden with only one channel, appears with both channels and a live Vatican partner, handles Vatican invalidation, records the reaction window, and cleans up its active state.
