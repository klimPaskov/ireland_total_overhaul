# Ireland action safeguard admission tranche — 2026-07-26

Feature slug: `ireland_focus_tree`

## Scope

This source tranche closes three per-action safeguard rows identified by the canonical 140-action map. It does not change the action or mission inventory, category caps, political-power model, Northern boundary, or material reward rules.

## Implemented gates

| Action | Canonical burden | Admission now required | Ownership |
| --- | --- | --- | --- |
| `Share a Controlled Weather Report` | exposure, aviation safety, leverage, Integrity | a live weather incident, a completed G2 cooperation record, or a valid diplomatic channel, plus Coastal and Air Warning at the shared warning bottleneck threshold | `slopx_ireland_weather_cooperation_depth_valid` |
| `Release or Exchange Internees` | leverage, public trust, security review | the internment law and active incident, plus a live British, American, German, Vatican, or neutral-states diplomatic channel with a valid route | `slopx_ireland_internment_diplomatic_channel_valid` |
| `Merge Tax and Debt Administration` | finance staff, budget, external creditors | controlled state 119 plus a live British, American, or neutral-states creditor route | `slopx_ireland_external_creditor_channel_valid` |

The shared `slopx_ireland_any_valid_diplomatic_channel` trigger validates named state actors for the British, American, German, and Vatican channels and retains the neutral-states forum as its own channel. A stale route flag or generic foreign-reaction window is not sufficient.

## Boundaries and cleanup

The triggers have no side effects. The owning actions retain their existing dynamic Political Power/Command Power costs, physical inputs, incident or mission lifecycle, foreign-reaction window, and route cleanup. No gate grants recognition, alignment, territory, cores, industry, equipment, units, fuel, shipping, administration, offices, or passive Political Power.

## Static checks

- All three new trigger identifiers are defined once and referenced by their intended action.
- The weather action still consumes 250 manpower and 10 Support Equipment, with the existing capped cancellation recovery.
- Internee release still closes the named neutrality incident and does not create a release or diplomatic result without the channel gate.
- Tax/debt administration still charges its existing bounded burden and does not erase debt or create an external agreement.
- No new command-power cost exceeds 60.
- No live HOI4 process was launched. Engine parsing, action visibility, AI admission, foreign-channel invalidation, incident cleanup, and occupation scenarios remain not-run.

