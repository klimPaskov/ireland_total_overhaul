# Foreign guarantee active-law gate tranche

Feature slug: `ireland_focus_tree`

## Change

`Review Foreign Guarantees` now requires the live `slopx_ireland_law_guarantee_active` flag in addition to the existing occupation/integration review context, Dublin-to-Belfast map scope, Northern flexibility headroom, and valid British partner.

The flag is maintained by the existing guarantee-law refresh lifecycle. A stale review flag, a Northern route alone, or a named British actor without an active guarantee can no longer create the review action. The action still changes only the Northern flexibility ledger and creates no territory, cores, recognition, equipment, units, shipping, fuel, administration, offices, alignment, or passive Political Power.

## Evidence and remaining work

- Source: `common/decisions/slopx_ireland_decisions.txt` (`slopx_ireland_action_review_foreign_guarantees`).
- Law owner: `common/scripted_effects/slopx_ireland_laws.txt` (`slopx_ireland_law_guarantee_active`).
- Localisation: `localisation/english/slopx_ireland_l_english.yml`.
- This closes the canonical active-guarantee admission row for this action only. Live law transition, partner invalidation, reaction, mission, AI, and cleanup scenarios remain not-run.
