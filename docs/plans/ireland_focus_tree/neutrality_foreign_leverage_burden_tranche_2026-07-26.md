# Neutrality and foreign-leverage burden tranche

Feature slug: `ireland_focus_tree`

Date: 2026-07-26

Status: source-level implementation complete for this tranche; live partner, reaction, AI, engine-reference, and cleanup scenarios remain not-run.

## Canonical gap

The decision and mission map requires five action families to treat external dealings as a real cost: `Release or Exchange Internees`, `Share a Controlled Weather Report`, `Answer a Foreign Access Request`, `Negotiate British Flexibility`, and `Recognise a Liberated Authority`. Before this tranche, the first, second, third, and fifth actions changed only their local ledger or aid/recognition result, while the British negotiation changed only Northern British Flexibility. None recorded the required Foreign Exposure and source-specific leverage burden.

## Implementation

- Added shared constants for the neutrality channel burden (`5` Foreign Exposure and `3` sponsor leverage) and the explicitly British Northern negotiation (`3` Foreign Exposure and `4` British Leverage).
- Added `slopx_ireland_record_diplomatic_channel_burden` in `common/scripted_effects/slopx_ireland_effects.txt`. It checks current named partner validity, gives leverage only to one live named channel, treats the neutral-states forum as exposure-only, and clamps every external ledger.
- Wired the reusable effect into internment release, controlled weather, foreign-access response, and liberated-authority recognition after their existing legal, incident, route, map, material, and dynamic-cost work.
- Wired the Northern negotiation directly to its valid British-partner gate and records its British Exposure/Leverage burden beside the existing +5 Northern British Flexibility movement. It does not move Unionist Consent.
- Updated action names, descriptions, requirements, dynamic-effect documentation, project status, and the source-of-truth map in the same change.

## Boundary and cleanup

The effect creates no foreign access, alignment, recognition, territory, core, industry, equipment, unit, fuel, shipping, administration, office, or political-power reward. Existing incident closure, mission activation, cancellation refunds, foreign-reaction windows, category capacity, and route cleanup remain owned by the five decisions and their existing helpers. Live channel invalidation, simultaneous-channel priority, reaction outcomes, AI queue behavior, engine parsing, and cleanup scenarios remain not-run.
