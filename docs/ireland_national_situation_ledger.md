# Ireland Cabinet Briefing

Feature slug: `ireland_mechanics_hub`.

## Purpose

The Cabinet Briefing gives the player a concise strategic reading of Government, National Supply, Defence, and the National Question. It is available in the decision view after Ireland initializes and appears as a compact inlay in the national-focus view.

It does not duplicate the detailed ledgers. Provision components remain in the Provision system, service preparation remains in Readiness, Northern settlement records remain in the Northern system, and cultural, evidence, diplomatic, and exceptional-route state remains with their existing content.

## Reading the briefing

- Government is a cabinet judgement of parliamentary authority.
- National Supply is the existing Provision aggregate.
- Defence is the existing Readiness aggregate.
- National Question reports whether the question is unopened, in recovery, settled, or at an active integration stage.

Green indicates a sound condition, amber a matter under pressure, red an active obstruction, and grey a record not yet opened. Hovering a card explains the policy consequence and points to the existing focus or decision family that governs it.

The assessment line names the cabinet's immediate concern. A single `Advance Programme` action appears only when the next ordinary Parliament step is valid. The same guarded executor and cost are used by the Parliament surface. The briefing grants no independent progress and AI does not use it.

## Focus inlay

The focus-view inlay uses the same four cards as an informational summary, not a second control dashboard. The guarded action remains on the decision-category briefing because focus-inlay buttons cannot be conditionally hidden; this avoids a permanently grey control. There are no tabs, selectable rows, refresh controls, or hidden route changes.

## Implementation ownership

- Category: `common/decisions/categories/ireland_categories.txt`
- Scripted GUI: `common/scripted_guis/ireland_scripted_guis.txt`
- Focus inlay declaration: `common/focus_inlay_windows/ireland_national_situation_inlay.txt`
- Status triggers and action helper: `common/scripted_triggers/ireland_mechanics_hub.txt` and `common/scripted_effects/ireland_mechanics_hub.txt`
- Dynamic cabinet text: `common/scripted_localisation/ireland_localisation.txt`
- Layouts: `interface/ireland_national_situation.gui` and `interface/ireland_national_situation_inlay.gui`
- English text: `localisation/english/ireland_l_english.yml`

## Future direction

Keep this surface small. New mechanics should normally appear in the focus, decision, event, or dedicated ledger where the player acts on them. A new briefing card requires a separate accepted design proving that it is both strategically distinct and directly governable.
