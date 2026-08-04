# Northern local-partner gate tranche

Feature slug: `ireland_focus_tree`  
Namespace: `ireland`  
Date: 2026-07-25

## Purpose

The canonical Northern map requires Cross-Border Confidence Measures to have at least one local partner. Inviting Northern Delegations also needs an authored local contact before travel, security, and representation work can begin. The shared Northern route flags alone did not distinguish a claim or war plan from local participation.

## Implementation

`common/scripted_triggers/ireland_triggers.txt` now defines `ireland_northern_local_partner_valid`, accepting only named local-contact or mandate records: opened Northern contacts, local authority, union local mandate, IRA local mandates, trade corridor, or open Northern negotiation.

The trigger is consumed by:

- `ireland_action_open_cross_border_confidence_measures`;
- `ireland_action_invite_northern_delegations`.

Both decisions retain their existing named map-state, control, staff/material, consent, mission, dynamic-cost, AI, and cleanup gates. No claim, control, occupation, settlement, integration, core, unit, or diplomatic recognition is created by the trigger.

## Validation status

Static trigger/consumer, source-brace, operator, localisation, and cross-surface checks remain to be rerun after this tranche. Live local-partner, travel, mission, failure, and cleanup scenarios remain not-run; HOI4 is intentionally not launched.
