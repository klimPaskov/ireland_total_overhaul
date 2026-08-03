# Ireland static engine-reference audit

Date: 2026-07-29  
Feature: `ireland_focus_tree`  
Namespace: `slopx`

## Scope

This audit covers the current authored source, localisation, GFX registrations,
runtime textures, and the local engine references required by `AGENTS.md`.
Hearts of Iron IV was not launched. Live play, fresh-save, and in-game scenario
testing are outside the user-authorized completion gate.

## 2026-08-01 authority update

The pending authority items in this historical audit are superseded for the
approved M2, A2, and C3 decisions by
`docs/plans/ireland_focus_tree/authority_rulings_m2_a2_c3_2026-08-01.md`.

- M2 resolves the Radical/Underground wording conflict without changing the
  exact inventory: the election and essential-service modes are merged into
  their base missions and ordinals 006 and 009 are the two new Radical
  mission families.
- A2 accepts the documented static `hidden = yes` treatment for A-22, A-27,
  and A-28 with canonical earned/reveal conditions. No trigger-valued
  achievement visibility key is claimed.
- All 60 C3 review approvals are accepted. The current manifest has 83 C3-
  complete entries, including the later EV-SRC-055 Oireachtas and EV-SRC-059
  Admiralty-chart promotions, with final runtime DDS files, hashes, and GFX
  registrations. C1/C2 blocked and C2 review rows remain unchanged.

The post-ruling localisation recheck removed pre-reveal cultural wording that
named hidden routes or extraordinary leads, aligned the two merged mission
titles with the authority ruling, changed the by-election and parish-audit
requirement text to name the merged base missions and modes, and exposed the
current radical-mode ledger values in both objective tooltips. The localisation
auditor found no missing or duplicate keys after this correction.

The source checks were made against the required offline Paradox wiki snapshot,
the local vanilla documentation under the Hearts of Iron IV installation, and
vanilla precedents for focuses, decisions, missions, events, ideas, AI,
achievements, characters, scripted GUI, sprites, and scripted effects.

## Authored inventories

The current source contains:

- 216 unique Ireland focus blocks;
- 140 unique decision-action blocks;
- 54 unique mission-family blocks;
- 194 unique action and mission identifiers in total;
- 32 unique custom-achievement identifiers;
- 30 durable AI strategy profiles and 10 temporary overlays;
- 31 focus-selection plans;
- 493 unique top-level event definitions: 257 package, contribution, and public
  conclusion events plus 236 consequential flavour events.

No duplicate focus, action, mission, achievement, or event identifier was found.
All 216 focus identifiers referenced by the AI focus plans resolve to authored
focuses. All 740 prerequisite, mutual-exclusion, and related focus references
resolve inside the same 216-focus inventory.

## Opening values and shared tuning

The initializer and shared tuning sources preserve the canonical opening:

- National Settlement 25 with momentum -1;
- Social Consent 55;
- Neutrality Integrity 72;
- Dáil formal threshold 153 and routine threshold 152;
- National Provision components 55, 25, 40, and 30, displayed as 38;
- Readiness components 25, 8, 20, 12, 5, 5, and 30, displayed as 15;
- Northern opening values U5, N40, L30, B10, S45, and I10;
- leverage values British 45, Vatican 25, American 5, and German 5.

The action command-power ceiling is centralized at 60. No authored Ireland
action exceeds that ceiling.

## Focus reward boundary

The national-focus source contains no direct use of:

- equipment, manpower, fuel, resources, units, supply, or technology grants;
- building or off-map building construction;
- political-power or command-power grants;
- state ownership transfers;
- state cores;
- faction entry or autonomy grants.

Political victories therefore do not bypass their attached implementation
systems through direct focus rewards.

Northern claims, control, occupation, settlement, integration, and cores remain
separate. The only Ireland `add_core_of` writer is the final Northern core-review
effect. Its trigger requires stage-five/core eligibility, settlement and
integration completion, control and resistance checks for state 119, the final
review and proof record, every review component, and the absence of recorded
review failures.

## Decision and mission lifecycle

All 54 missions define a deadline, selectable-mission state, positive-progress
polarity, completion effect, timeout effect, and AI weight. All 140 decision
actions define visibility, availability, completion effects, and AI weight.
Shared scripted helpers provide the partial-success, failure, escalation,
costing, and cleanup surfaces used by the authored families.

The approved M2 ruling resolves the historical Radical/Underground inventory
wording. The current source physically nests
`slopx_ireland_mission_consolidate_the_movement_network` and
`slopx_ireland_mission_secure_constituent_authority` under
`slopx_ireland_radical_underground`. The by-election and parish-audit modes
remain mode-specific paths of the two merged base missions. The source still
contains exactly 54 mission families, 140 actions, and 13 categories.

## Localisation and event references

The Ireland localisation inventory contains 3,574 unique keys with no duplicate
keys in the package files. Every Ireland localisation file retains a UTF-8 BOM.

Coverage includes:

- both name and description keys for all 216 focuses;
- both name and description keys for all 194 actions and missions;
- both `_NAME` and `_DESC` keys for all 32 achievements;
- all 1,978 event localisation references used by the 493 top-level event
  definitions.

No unresolved Ireland event-definition or event-reference identifier was found.

## Runtime GFX

Nine Ireland GFX definition files contain 346 unique sprite names and 1,106
texture references. Every referenced runtime texture exists under `gfx/`; no
sprite points into temporary `assets/` staging.

All 877 inspected runtime DDS files decoded successfully. The repaired icon
families have the following exact inventories:

- 216 focus-goal icons;
- 13 decision-category icons;
- 70 decision-action textures;
- 54 mission textures;
- 63 route-spirit textures;
- 27 overlay textures;
- 51 law textures;
- 45 mechanic-ledger textures;
- 96 achievement textures: 32 complete, 32 grey, and 32 not eligible.

The staging and runtime icon pixels match. The focus, law, decision, mission,
spirit, overlay, and ledger families have no outer-edge alpha contact, opaque
corners, or strong green-key chroma. The achievement family intentionally uses
full square frames and has no strong green-key chroma. Enlarged contact-sheet
review found no neighbouring atlas tile or sheet fragment crossing an icon
edge.

## Script hygiene

Forty-two Ireland script files were checked for balanced braces. Forty Ireland
gameplay files were checked for unsupported `<=` and `>=` operators. No
structural or unsupported-operator finding was recorded.

## Open authority and source gates

Static source validation does not close the remaining portrait, symbol, and
event/news source rows that remain C1, C2, or user-review C3 in the
authoritative source manifest. The M2 inventory question and the A2
achievement-visibility question are settled by the dated authority ruling.
A2 uses the documented static `hidden = yes` form and does not claim an
unsupported trigger-valued visibility field.

The feature remains incomplete while those gates are unresolved. No fallback
or silent reinterpretation is authorized by this audit.
