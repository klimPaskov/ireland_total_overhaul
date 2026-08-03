# Ireland cultural capacity and concealed-evidence ledger

Feature slug: `ireland_focus_tree`; namespace: `slopx`.

This document records the runtime contract for the serious-culture lane and its concealed evidence projection. It is deliberately separate from the focus-tree layout: public cultural work is useful to every route, while the hidden High Kingship, Five Provinces, and Otherworld permissions require the named evidence, political, regional, and unusual-campaign gates in the canonical specifications.

## State surfaces

`slopx_ireland_cultural_capacity` is the shared institutional summary. The four player-facing components are recomputed by `slopx_ireland_sync_cultural_evidence`:

- `slopx_ireland_cultural_language_service`
- `slopx_ireland_cultural_archival_record`
- `slopx_ireland_cultural_regional_participation`
- `slopx_ireland_cultural_site_stewardship`

The campaign opens with Cultural Capacity `30`, and the four displayed components open at `30/27/25/22`. Completed H/P institutions, named actions, and full mission records add to the appropriate component. All four values are clamped to the shared `0..100` range; they are not political-power stores and do not create equipment, factories, units, fuel, shipping, territory, cores, offices, recognition, or alignment.

The concealed ledger projects independent work into these displayed counters:

- credible records, capped at `12`;
- evidence categories, capped at `7`;
- participating regions, capped at `6`;
- disqualifiers, capped at `100` but normally `0` or `1`;
- accepted obligations, capped at `12`;
- public knowledge, mirrored from `slopx_ireland_public_knowledge` and capped at `100`.

Only completed named work or a recorded full mission can advance a credible record. Starting an action or receiving a partial/failure result does not create a full record. Disqualifiers are durable route history and are never silently removed by recovery.

## Stepwise flow

1. The shared opening initializes the capacity, four components, public knowledge, and the six GUI evidence counters.
2. The daily/monthly Ireland hooks recompute the public components from the capacity ledger and completed institutional work.
3. The same sync projects archival, regional, site, witness, diaspora, and mission records into the concealed counters.
4. The serious-culture public flags open the H/P lane and its readable focus requirements. The hidden permission itself remains concealed until the canonical cultural permission is present.
5. `slopx_ireland_independent_evidence_ready` requires the cultural service and diaspora exchange, the royal evidence thresholds, regional participation, and either a full restoration-evidence mission or the provenance achievement. It is not set by a focus description or by an action merely being selected.
6. `slopx_ireland_sync_hidden_permissions` consumes the live counters and disqualifier state. It derives the separate readiness flags for High Kingship, Five Provinces, and Otherworld, then requires the corresponding political opening and unusual campaign condition.
7. The route-specific focus gates expose the concealed branch only after the permission flags are earned. Route conclusions still require their own institutions, offices, obligations, review, and cleanup.
8. A concealed-evidence inspection request is consumed on the next Ireland daily tick, refreshing the ledger and permissions and incrementing the evidence GUI dirty counter.

The H/P/A boundary is preserved throughout: documented language, archive, regional, site, folklore, and exchange work is H; antiquarian political reinterpretation is P; impossible confirmation and the final concealed routes are A. Serious cultural work remains valuable when an A route is never revealed.

## Route thresholds

The route permissions use centralized constants in `common/script_constants/slopx_ireland_constants.txt`:

| Route | Public component thresholds | Evidence thresholds | Additional condition |
| --- | --- | --- | --- |
| High Kingship | Language `45`, archival `60`, regional `55`, site `65` | Credible `4`, categories `3`, regions `3`, no disqualifier | A constitutional opening plus a rare war, incident, foreign-reaction, Northern-failure, or emergency-review state |
| Five Provinces | Archival `45`, regional `65`, site `55` | Northern settlement ledger and regional preparation | Federal powers preparation/conference followed by a rare campaign condition |
| Otherworld | Language `45`, archival `75`, regional `60`, site `70` | Credible `6`, categories `4`, regions `4`, no disqualifier | Investigation, evidence verification, and a rare campaign condition |

High Kingship, Five Provinces, and Otherworld use different readiness flags and different later completion flags. One route's evidence is not treated as another route's completion.

## Plebiscite and GUI lifecycle

`slopx_ireland_sync_plebiscite_state` maps the campaign-open flag to both the generic `slopx_ireland_plebiscite_open` and the Northern `slopx_ireland_northern_plebiscite_open` flag. A passed, rejected, or recovered result closes both open flags and the campaign-open flag. The authored Northern result event also records the separate passed/rejected outcome before cleanup.

The three scripted GUI surfaces remain exactly:

- National Conditions Panel: requests a conditions review and refreshes Provision, Readiness, operational, and law projections;
- Northern Settlement Ledger: requests a Northern review, runs the ledger/core-review/achievement helpers, and exposes dynamic model, region, and failure text;
- Concealed Evidence Ledger: requests an evidence inspection, refreshes cultural counters and hidden permissions, and preserves hidden content until the route gate is actually earned.

Row clicks set request flags rather than mutating gameplay directly. The Ireland daily hook consumes those flags so the GUI and the authoritative ledgers cannot drift from one another.

## Implementation and asset wiring

The runtime implementation is in `common/scripted_effects/slopx_ireland_culture.txt`, with calls from `common/on_actions/slopx_ireland_on_actions.txt`. Shared thresholds are in `common/script_constants/slopx_ireland_constants.txt`; route gates remain in `common/scripted_effects/slopx_ireland_runtime.txt`; focus requirements are in `common/national_focus/slopx_ireland_focus_tree.txt`.

Evidence display variables are projected to `interface/slopx_ireland_evidence_ledger.gui` using the existing `GFX_slopx_ireland_gui_evidence_*` rows and status assets. They must remain dynamic and must not reveal concealed focus names before permission. If a row needs a new icon, register it in `interface/slopx_ireland_gui_assets.gfx`, place the final sprite under the matching `gfx/` root, and record the source/processed item in the feature asset manifest; no generated likeness is valid for a historical person.

## Interactions and cleanup

- Cultural components feed the focus gates, evidence display, AI hidden-route permission, and route-specific spirit progression.
- Northern contacts and regional participation feed the regional evidence projection but never grant Northern control, occupation, settlement, integration, or cores.
- Evidence disqualifiers feed High Kingship and Otherworld failure gates and achievement history; recovery may clear live emergency state but not a witnessed disqualifier.
- Plebiscite cleanup closes both generic and Northern open states after passed, rejected, or recovered results.
- Route conclusion cleanup remains owned by the route conclusion effects; the culture sync only derives evidence/readiness state and does not remove leaders, offices, laws, identities, or route spirits.

## Future plans

Future extensions may deepen regional service delivery, archival provenance, and postwar cultural reconstruction without adding a fourth persistent spirit family or a fourth GUI. Any new evidence class must have a named source flag, a full/partial/failure interpretation, an explicit disqualifier policy, a localized display value, and a documented H/P/A classification before it is wired into a route gate.
