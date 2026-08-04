# Ireland mission description objective review — 2026-07-26

Feature slug: `ireland_focus_tree`

## Result

The 54 localized mission descriptions in `localisation/english/ireland_l_english.yml` were reviewed against the mission architecture in `docs/specs/ireland_focus_tree/ireland_focus_tree_spec_part_5_decisions_events_and_lifecycles.md`.

The descriptions now identify the concrete work the player must perform instead of describing a generic ledger or repeating a category template. Each row names the relevant place, institution, route, cargo, force, service, or settlement where the canonical row provides one; every row states a concrete deadline or operating period; and every row distinguishes full success, partial success, and failure. Escalation and cleanup remain implemented in the corresponding mission source blocks rather than being hidden in prose.

## Static evidence

- 54 mission description keys are present, matching the 54 mission blocks in `common/decisions/ireland_decisions.txt` one-for-one.
- 54/54 descriptions are unique exact strings.
- 54/54 descriptions include a machine-readable `within N days` or `for N days` duration.
- 54/54 descriptions include `Full success`, `partial success`, and `failure` outcome wording.
- 54/54 source mission blocks contain a named map-objective tooltip, `days_mission_timeout`, full-result handling, partial-result handling, failure handling, escalation telemetry, and route-cleanup handling.
- The previous generic phrases (`stated parliamentary objective`, `stated material objective`, `stated readiness objective`, `stated diplomatic objective`, and the repeated National Settlement boilerplate) occur zero times in the mission description rows.
- The localization file retains its UTF-8 BOM.

## Reviewed mission families

The review covers every canonical family, grouped by the source table:

- Settlement and government: Cabinet Discipline; Seventy Routine Votes; Six-Month Settlement Review.
- Electoral and civic administration: Free General Election; Government After the Poll; By-Election.
- Education and services: Education Settlement; Essential Services; Parish Service Contracts.
- Serious culture: National Folklore Cycle; Five-Region Cultural Congress; Restoration Evidence.
- Food, industry, energy, and transport: County Tillage; Harvest to Market; Protected Workshop Network; Developmental Plant; Capital Through Winter; Turf; Dublin–Cork Corridor; Essential Cargo Route; Lost Merchant Vessel; Western Regional Portfolio.
- Defence and command: Command District; Reserve Brigade; Dublin–Belfast Corridor; Coastwatch Sector; Treaty Port; Neutral Approaches; Plan W; Demobilised Cadre.
- Active neutrality: Aircrew Internment; Merchant Sinking; Equal Belligerent Rules; Blacksod Reporting.
- Foreign channels: British Supply Agreement; American Procurement; German Arms Promise; Vatican Relief Mediation.
- Northern transition and integration: Cross-Border Health; Representative Northern Convention; Supervised Plebiscite; Federal Settlement; Take and Hold Belfast; Ordinary Policing; Belfast Industry; Stage Five Integration Review.
- Regional and supernatural conclusions: Regional Charter; Member Contribution Schedule; Five-Site Compact.
- Postwar conclusions: End Wartime Rationing; Demobilised Forces; Republic Settlement; United Nations Admission; National Reconstruction.

## Boundaries

This tranche changes player-facing mission prose and its evidence only. It does not claim that the mission system has passed live engine parsing, AI queue tests, map-control scenarios, timer scenarios, foreign-reaction scenarios, Northern transition scenarios, neutrality cleanup scenarios, or the full 22-scenario programme. The broader overhaul remains incomplete while those checks, source clearance, the 140-row action/material safeguard mapping, and the staged-achievement visibility engine reference remain open.

