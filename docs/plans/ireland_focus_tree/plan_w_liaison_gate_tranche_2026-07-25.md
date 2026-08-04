# Plan W Liaison Gate Tranche (2026-07-25)

Feature slug: `ireland_focus_tree`

## Scope

This tranche closes the canonical admission gate for `Formalise Plan W Liaison`. It keeps the action as a bounded Border Belt contingency measure: it does not grant territory, cores, equipment, units, fuel, shipping, administration, alignment, or recognition.

## Canonical requirements

The Part 5 decision map requires invasion danger, Readiness, and a legal-cooperation gate. The canonical Plan W row also identifies Command, Intelligence, Supply, Provision, Irish command safeguards, and the British bargain as the operative conditions. The action must define contacts, maps, command, entry conditions, withdrawal, and secrecy, with exposure and British leverage as risks.

## Current implementation

`common/decisions/ireland_decisions.txt` now requires all of the following before the existing dynamic Political Power and Command Power scarcity gate can pass:

- invasion danger or an active war;
- the British channel and a valid British partner, with Border Belt state 113 controlled;
- live Provision of at least 40;
- live Readiness of at least 35;
- live Command Readiness of at least 30;
- live Intelligence Readiness of at least 30;
- live Supply Readiness of at least 25;
- the foreign-access law and sovereignty safeguards.

The completion effect preserves the existing 25 Command Power charge, records the action, adds the authored British-leverage exposure, and opens the foreign-reaction window. No political-victory shortcut is introduced.

`localisation/english/ireland_l_english.yml` exposes the same conditions in the action description and requirements tooltip, including the distinct command, intelligence, supply, law, safeguard, and Border Belt checks.

## Validation boundary

Static source and localisation checks are required after this tranche. HOI4 was not launched, so live decision visibility, partner validity, law transitions, foreign reactions, and cleanup scenarios remain open evidence gates.
