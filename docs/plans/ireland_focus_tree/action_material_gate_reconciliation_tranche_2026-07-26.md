# Ireland action-material gate reconciliation tranche — 2026-07-26

Feature slug: `ireland_focus_tree`

Status: implemented source tranche; the Ireland overhaul remains incomplete because source clearance, live engine checks, and required runtime scenarios are still open.

## Scope

This tranche closes three per-action admission mismatches in the canonical 140-action map. Each action already had a concrete completion charge; the missing piece was a matching stockpile gate in the same decision admission path. The changes do not alter the 13-category, 140-action, or 54-mission inventory.

## Implemented gates

| Action | Named work | Admission now required | Completion charge |
| --- | --- | --- | --- |
| `Expand Folklore Collection` | Connacht collectors, travel, and archive custody | 250 manpower and 5 Trucks | 250 manpower and 5 Trucks |
| `Negotiate British Flexibility` | Dublin-to-Belfast negotiating and transport staff | 250 manpower and 5 Trucks, plus a valid British partner | 250 manpower and 5 Trucks, plus the existing exposure and British-Leverage burden |
| `Merge Tax and Debt Administration` | Lower Lagan and Lisburn customs/debt transfer | control of state 119, a valid external-creditor channel, and 5 Convoys | 5 Convoys |

The tax/debt convoy values use dedicated local macros rather than borrowing the diaspora-relief names. The charges remain immediate action commitments; no action creates a passive stockpile, free shipping, free equipment, or a refund on success.

## Localisation

The three requirement strings remain player-facing and now state the staff, truck, or convoy commitment alongside the existing route, partner, ledger, and dynamic Political Power/Command Power requirements.

## Static evidence

- `common/decisions/ireland_decisions.txt` contains the three new admission gates and the dedicated tax/debt convoy macros.
- A source sweep of all 140 action blocks finds no completion-time equipment, manpower, fuel, or factory charge without a corresponding same-action stockpile/capacity gate. Existing scripted authority helpers remain responsible for gates that intentionally span an action and its map objective.
- The three requirement localisation keys are present in `localisation/english/ireland_l_english.yml`.
- No focus, event, mission result, or conclusion was changed by this tranche.

## Remaining gates

This closes only three material-admission rows. Action-specific leverage, tied-unit, aircraft, ship, local-support, and foreign-channel evidence still requires broader per-ID reconciliation; source clearance, engine/reference checks, live AI/GUI behavior, and the fresh-save scenario programme remain open.
