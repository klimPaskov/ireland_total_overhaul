# Ireland event clarity and option-effects localisation handoff

Owner: `event_clarity_localisation`
Scope: English localisation only. Gameplay files remain owned by the parent agent.

## Completed

- Audited four Ireland-owned event files: `events/ireland_flavour_events.txt`, `events/ireland_route_events.txt`, `events/ireland_member_contribution_events.txt`, and `events/ireland_public_conclusion_events.txt`.
- Inventory found 495 visible event blocks, 1,988 title, description, and option references, and 998 unique player-facing options.
- Added a nonempty `<option key>.effects` key for every one of the 998 options in `localisation/english/ireland_l_english.yml`.
- Each effects string states the visible ledger direction with consistent green, red, or yellow colour markup. It also names direct visible outcomes such as plebiscite records, route commitments, review openings, conclusion reviews, archive/site decisions, neutral observations, and member-contribution costs.
- Rewrote generic Northern, postwar, and foreign-reaction descriptions so they describe the immediate in-world situation and show the relevant live ledger value. Existing titles and option key names were preserved.
- Replaced the regional member-contribution option labels with readable sentences that state their exact immediate costs.
- Removed semicolons and em dashes from the Ireland event and flavour localisation section.

## Validation evidence

- Option references: 998 unique.
- `.effects` keys: 998, all nonempty, missing 0.
- Localisation duplicate keys: 0.
- File encoding starts with UTF-8 BOM bytes `EF BB BF`.
- Event-section semicolon count: 0. Event-section em dash and en dash count: 0.
- Foreign reaction window wording uses `May open a paced foreign response window when the 120-day cooldown is clear.` No unconditional `Opens a foreign response window` wording remains in `.effects` keys.

## Parent wiring and recommended call sites

The parent should keep `custom_effect_tooltip = <option key>.effects` in every `option` block in the four audited event files. The exact call-site inventory is the 998 `name =` option lines listed above. The localisation file is ready for those calls, including `ireland_events.airspace_escalation.a.effects`.

Special non-ledger outcomes represented by the new keys include:

- `ireland_events.unity_final_cabinet_decision.*`: federal, unitary, postwar pledge, defence cooperation, or refusal records.
- `ireland_events.five_provinces_stone_review.*` and `ireland_events.five_provinces_standards_sites.*`: evidence verification, site security, sealed interpretation, or rejection.
- `ireland_events.dillon_named_dail_vote.*`: carried or deferred Dáil vote and mandate recovery.
- `ireland_events.high_king_public_conclusion.accept` and `ireland_events.northern_unity_public_settlement.accept`: public conclusion records.
- `ireland_events.member_contribution_selection.*`: exact stockpile or power charges and the 180-day schedule commitment.
- `ireland_events.foreign_neutral_shipping_observation.*`: neutral observation record and review period without a leverage claim.
- Plebiscite, Irish Shipping, archive-reveal, and Frank Ryan lifecycle options: visible record wording without raw implementation flag names.

## Parent completion update - 2026-08-13

The parent implementation replaced direction-only numeric wording with exact
signed, post-clamp previews. All 998 choices retain matching custom effect
tooltips. Numeric ledger choices print their exact applied changes; the five
member-contribution choices state fixed costs; the neutral observation and High
King conclusion state their 14-day and 180-day review periods; flag-only choices
state the durable policy or route consequence. The earlier direction-only note
below records this subagent's localisation baseline and is superseded by this
parent completion update.

## Dynamic and scripted-effect notes (historical subagent baseline)

- Superseded baseline note: the subagent originally used direction-only wording. The parent completion update above replaces it with event-opening, exact signed post-clamp previews.
- The paced foreign-window wording reflects the current helper cadence. Do not change it back to unconditional opening language unless the helper contract changes.
- Helper calls that need player-facing custom tooltips are represented in the option effects text: `ireland_open_foreign_reaction_window`, `ireland_close_neutrality_incident`, `ireland_begin_conclusion_review`, Dillon mandate advance or setback, integration cleanup, route commit or cleanup, Otherworld archive reveal, neutral shipping observation, foreign digest consolidation, and member-contribution helpers.
- No raw country flag names are exposed in the new text. If a future helper adds a player-visible state, add a named effects sentence to the corresponding option key rather than exposing the flag.

## Remaining review notes

- The existing project-wide localisation file contains non-event em dashes in older focus, decision, and idea text. Those were outside this ownership boundary and were not changed.
- Some older event descriptions still use the project’s existing `ireland_settlement_bop_value` display alias. This is the established player-facing projection of the National Settlement ledger and was retained for cross-surface consistency.
- No gameplay or event script changes were made by this subagent. The parent owns final review of tooltip placement and runtime semantics.
