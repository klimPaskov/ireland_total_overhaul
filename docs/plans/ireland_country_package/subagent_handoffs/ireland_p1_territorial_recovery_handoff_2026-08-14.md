# P1 Territorial Recovery Handoff

Status: implemented within the decision, territorial-event, scripted-system,
constant, localisation, and narrow runtime-capacity surfaces on 2026-08-14.
No focus-tree, Parliament GUI, AI-plan, conclusion-event, asset, GFX, spec, or
thumbnail file was edited by this tranche.

## Changed files and identifiers

| File | Identifiers / responsibility |
|---|---|
| `common/decisions/ireland_expansion_decisions.txt` | `ireland_territorial_reopen_supervised_plebiscite` (306); converted `ireland_territorial_workers_border_campaign` into the launcher; `ireland_mission_sustain_the_workers_border_campaign` (343); `ireland_territorial_rebuild_workers_border_campaign` (421); event-led `ireland_territorial_convene_provincial_assent` (575); `ireland_territorial_reconvene_provincial_assent` (593); `ireland_territorial_withdraw_border_enforcement` (671); and the Atlantic-basing exit visibility. |
| `events/ireland_territorial_diplomacy_events.txt` | `ireland_territorial_diplomacy.25` Provincial Assent convention (801), `.26` assent record (863), `.27` adjournment record (883). |
| `common/scripted_triggers/ireland_triggers.txt` | Workers' full/partial result thresholds (4681), Provincial Assent reconvene readiness, safe fascist-withdrawal eligibility (4733), mission capacity alias, and critical-mission recognition. |
| `common/script_constants/ireland_constants.txt` | P1 mission/recovery durations, reservation, consent floors, rebuild deltas, and reconvene floors. Decision-only timer and reservation macros mirror those shared constants. |
| `common/scripted_effects/ireland_effects.txt` | `ireland_cleanup_mission_objectives` clears Congress-mission transient flags (4160–4162); `ireland_cleanup_route_state` clears Provincial Assent pending response flags (4255–4257). |
| `common/scripted_effects/ireland_runtime.txt` | `ireland_rebuild_mission_counters` now counts `ireland_mission_sustain_the_workers_border_campaign_active` in both the global active count (561) and the Northern category count (827). These are the only runtime edits. |
| `common/scripted_localisation/ireland_localisation.txt` and `localisation/english/ireland_l_english.yml` | The Territorial Policy category status starts at `GetIrelandTerritorialMethod` (667) and includes `GetIrelandTerritorialNextAction` (765), with all P1 cards, mission, event, tooltip, record, and obligation text. |

No new scripted effect was introduced, so `docs/ireland_dynamic_effects.md` did not need an entry.

## Lifecycle and balance notes

- Democratic recovery appears only after the established supervised-plebiscite mission records a failure or cancellation, no plebiscite is active, and no territorial response window is open. It preserves the original result record, clears only the existing launcher lock, applies the existing one-time non-refund guard, restarts the existing mission through its established capacity gate, and sets the route-specific 180-day cooldown. Partial plebiscite history is untouched and still meets the existing `ireland_settlement_under_law` focus requirement.
- The Congress launcher remains a 25 Political Power, 35-day committee action, but it now starts `ireland_mission_sustain_the_workers_border_campaign`. The 180-day mission records full success at Social Consent 60 and Northern Nationalist Consent 60; a 45/50 partial result sets `ireland_territorial_workers_campaign_complete`, preserving the existing `ireland_all_island_workers_republic` focus requirement while adding `ireland_territorial_workers_campaign_partial`. A timeout records failure and opens the repeatable, 120-day, one-civilian-factory rebuild. Rebuild restores only civilian-organising ledgers, retains failure history, and restarts the mission; it has no Political Power or equipment reward.
- Fascist withdrawal only appears after the original Ulster refusal or rejected counteroffer, while the enforcement file is open but no war goal has been issued, and then only when enforcement readiness fails, Northern Ireland is Irish-controlled/owned, or the foreign controller becomes invalid, a subject, or a faction partner. It clears all pending demand/target state without a refund, leaves the consumed reserve consumed, records the partial conclusion, and opens the non-annexation Atlantic-security exit.
- Provincial Assent now sends its result through `.25` rather than guaranteeing it on decision completion. The AI weighs Northern unionist consent, Northern nationalist consent, royal legitimacy, and administrative reach. The assent option is zero-weighted for historical AI; historic AI cannot force assent. `.26` records the outcome and unlocks the existing restoration settlement requirement. `.27` records the adjournment and preserves the first-adjournment flag. The reconvene card is repeatable, costs one civilian factory for 120 days, requires improved consent or legitimacy, and never erases that record.
- `ireland_territorial_reopen_belfast_compact` remains unchanged and the new status surface still exposes its refusal/reopening state.

## Mission quality

| Owner / category / region | Requirement and duration | Success / failure | Duplicate and exploit control |
|---|---|---|---|
| Congress / Territorial Policy, Northern | Existing mission capacity plus Northern category capacity; Social and Nationalist consent; 180 days | Full or partial is explicitly recorded; failure opens rebuilding | One active flag is counted by the global and Northern capacity counters; launcher is once-only, rebuild is paid and repeatable after a later failure. |
| Democratic / existing Northern plebiscite | Existing capacity and mission rules; relaunch card has 180-day cooldown | Existing mission full/partial/failure records are preserved | Recovery never refunds the launcher material or recreates it; it only reactivates the existing mission. |
| Restoration / Territorial Policy, Northern | One available civilian factory, 120 days, improved consent or legitimacy | `.26` records assent; `.27` records adjournment | No territorial or resource reward; first adjournment is durable, pending response flags are cleaned on route cleanup. |

## Localisation and category status

`ireland_territorial_policy_desc` now composes live scripted-localisation lines for:

- selected method;
- current target or holding;
- active response and the applicable cooldown;
- Ulster refusal, Belfast reopening, plebiscite, Congress, Provincial Assent, withdrawal, and recovery records;
- separate unresolved Highlands, Wales, Cornwall, Scottish-protectorate, and Welsh-protectorate obligations; and
- the next recovery or territorial action when one is currently valid.

## Cost, AI, and cleanup audit

- The Congress launch retains its existing Political Power entry cost; the new rebuild instead reserves one civilian factory for 120 days. It creates no unit, equipment, Political Power, territorial transfer, or core reward.
- Plebiscite recovery has a visible 15 Political Power and 35-day entry cost, takes the existing Northern critical-mission admission test, and sets the established material-refund guard before reactivation. Its failure/cancellation record is not cleared.
- Provincial reconvening uses a live available-civilian-factory test plus a custom tooltip for the improved Northern-consent-or-legitimacy requirement. No Political Power refund path exists.
- Border withdrawal is available only after the first ultimatum's refusal/rejected counteroffer and without a resulting war goal. It rejects unsafe targets before it can create a second ultimatum, clears global event targets, and leaves the enforcement reserve spent.
- Congress uses normal territorial AI weight only after the same capacity and category checks available to the player. Provincial Assent's AI result is weighted from the named current ledgers, and the assent option has zero historical-AI weight. The protected Belfast reopening remains independent and unchanged.

## Audit findings and remaining risks

Severity: no P1 implementation blocker remains in the owned surfaces.

- **Medium — live engine validation remains pending.** Static source checks cannot prove Clausewitz mission activation order under a full mission queue, timed decision behaviour, or event-option AI selection. The implementation follows the existing Northern critical-mission structure and the existing territorial target/cleanup structure.
- **Low — no new UI asset is required.** P1 reuses existing territorial decision art and adds no GFX reference.
- **Low — no new effect helper was needed.** The existing `ireland_clear_territorial_diplomacy_targets`, mission-result accounting, and capacity update helpers cover the cleanup and accounting work.

## Validation evidence

- Consulted the offline Paradox wiki data-structure, trigger, effect, modifier, localisation, scope, on-action, event, decision, idea, and AI pages; and the vanilla script-concept/script-constant, trigger, effect, decision-mission, and Italian decision precedents before implementation.
- Every touched script has a zero brace balance. The targeted syntax scan found no unsupported `<=` or `>=` operator in P1 surfaces.
- The territorial event namespace now contains 27 unique numeric event IDs, including unique `.25`, `.26`, and `.27`.
- All new decision, mission, and Provincial Assent event localisation keys resolve in the English file; the file retains its UTF-8 BOM.
- All ten scripted-localisation calls from `ireland_territorial_policy_desc` resolve to a `defined_text` block.
- `hoi4.event_inspect` was not callable in this session, so no MCP event artifact exists. Source-to-source event and localisation checks were performed instead.

## Simplifications, omissions, and blockers

None. No fallback was used. No cores, free units, free equipment, free Political Power, or reserve refunds were added.
