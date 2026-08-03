# Ireland localisation handoff

Historical handoff note (reconciled 2026-07-22): this worker snapshot reports 3,015 expected keys and no scripted-localisation dependency. The current audit reports 3,193 YML keys and the source contains scripted-localisation definitions and GUI projections, so this handoff is not the current runtime status. Retain it as coverage-worker evidence; use `docs/plans/ireland_focus_tree/audits/ireland_localisation_audit_2026-07-18.md`, `common/scripted_localisation/slopx_ireland_localisation.txt`, and `docs/plans/ireland_focus_tree/source_of_truth_map.md` for reconciliation.

## Status

The Ireland localisation file now covers every source-derived player-facing key in the audited focus, decision, mission, event, spirit, achievement, GUI, and National Settlement BOP surfaces. The key audit is exact: 3,015 expected Ireland keys, 3,015 definitions, zero missing keys, zero extra `slopx_ireland` keys, and zero duplicate definitions.

This is a localisation coverage completion, not a claim that the whole Ireland package is runtime-complete. The Northern Settlement Ledger still has a source-side scripted-localisation dependency described below.

## Files changed

- `localisation/english/slopx_ireland_l_english.yml`
- `docs/plans/ireland_focus_tree/localisation/localisation_handoff.md`

No gameplay, interface, GFX, asset, or other localisation file was edited.

## Exact coverage

| Surface | Source objects | Localisation definitions or references |
| --- | ---: | ---: |
| National focuses | 216 focus IDs | 432 name and description keys |
| Decision categories | 13 categories | 26 name and description keys |
| Decision actions | 140 actions | 280 name and description keys |
| Decision missions | 54 mission families | 108 name and description keys |
| Decision result and burden tooltips | 4 custom effect tooltips | 4 keys |
| Main events | 249 event IDs | 996 unique title, description, and option keys |
| Flavour events | 236 event IDs | 944 unique title, description, and option keys |
| Persistent spirits | 3 spirits | 6 name and description keys |
| Achievements | 32 achievements | 64 `NAME` and `DESC` keys |
| GUI surfaces | 3 surfaces | 137 unique referenced localisation keys |
| National Settlement BOP | 9 side and range IDs | 18 name and description keys |
| **Total** |  | **3,015 unique localisation definitions** |

The main-event suffix audit is 218 standard four-key blocks (`.t`, `.d`, `.a`, `.b`) plus 31 foreign/reaction blocks using `.title` and `.desc`, with 30 `.refuse` and one `.defer` option. The flavour-event audit is 236 titles, 236 descriptions, and 472 source-defined choices. The GUI reference counts by file are 57 for the Conditions Panel, 44 for the Northern Settlement Ledger, and 38 for the Concealed Evidence Ledger. Shared close-button references make the three-file total 137 unique keys.

## Duplicate and missing-key audit

- Focus source IDs: 216 raw, 216 unique.
- Category IDs: 13 raw, 13 unique.
- Action IDs: 140 raw, 140 unique.
- Mission IDs: 54 raw, 54 unique.
- Main event IDs: 249 raw, 249 unique.
- Flavour event IDs: 236 raw, 236 unique.
- Spirit IDs: 3 raw, 3 unique.
- Achievement IDs: 32 raw, 32 unique.
- BOP side and range IDs: 9 raw, 9 unique.
- Localisation definitions: 3,015 parsed, zero duplicate keys.
- Expected source-derived keys missing from localisation: none.
- Extra `slopx_ireland` localisation keys: none.
- Malformed single-line localisation entries: none.

The BOP's `slopx_ireland_national_settlement` key is intentionally shared with the national focus of the same ID. It is defined once and counted once in the focus coverage, while the two BOP sides and seven BOP ranges receive their own labels and descriptions.

## Dynamic localisation and route wording

Dynamic values were retained or added where the source exposes a live state value, including:

- National Settlement BOP value.
- Provision, Readiness, and Neutrality Integrity displays.
- Northern Unionist Consent, Nationalist Consent, Labour Cooperation, British Flexibility, Security Stability, Integration Capacity, and integration stage.
- Concealed Evidence credibility, category, region, public-knowledge, disqualifier, and obligation counts.
- Action burden, political cost, and command cost in the action confirmation tooltip.
- Active mission count in full, partial, and failure result tooltips.

Focus, decision, main-event, and flavour-event wording was reviewed against the route registry. De Valera, Lemass, Fine Gael and Cosgrave, Mulcahy, Costello, Dillon, Norton, Clann, vocational, IRA, Congress, O'Duffy, clerical and producer, Ailtirí, High Kingship, Five Provinces, Otherworld, and convergence language uses distinct institutional or ideological framing. The concealed routes use evidence, testimony, obligations, sites, or public consequences as the reveal language rather than advertising a locked route in generic UI text. The achievement description for the sponsorless hidden movement is deliberately generic until that route is public.

## Scripted-localisation issue list

The Northern GUI source contract states that `slopx_ireland_northern_model`, `slopx_ireland_northern_region`, and `slopx_ireland_northern_failure_state` should be scripted-localisation projections from route flags, integration stage, and active review/failure state. The repository currently has an empty `common/scripted_localisation/` directory and no Ireland definitions for those projections.

The YML file therefore supplies non-spoiler, stable labels and tooltips for all three referenced keys, but cannot make their displayed model, region, or failure value dynamic inside the localisation-only ownership boundary. This remains unresolved and should be implemented by the parent in a source-owned scripted-localisation file, then checked with the Northern GUI render or an engine parse.

## Cross-surface notes

- Main events use both `.t`/`.d`/`.a`/`.b` and `.title`/`.desc`/`.accept`/`.refuse`/`.defer` naming forms. Both forms are covered.
- Event follow-up text is represented by every source-defined title, description, and option reference. No additional follow-up key family exists in the audited event files.
- GUI element `name` fields and dirty flags were not treated as localisation references. Only text, context-aware text, context-aware tooltips, and `pdx_tooltip` values were included in the 137-key audit.
- Character names are inline in the source files, and no Ireland cosmetic-country localisation references were found. No speculative country-name keys were added.
- Source comments use ASCII `Ailtiri` in places, while the canonical route name is `Ailtirí na hAiséirghe`; player-facing route text follows the canonical accented spelling.

## Encoding and wording checks

- `slopx_ireland_l_english.yml` starts with the UTF-8 BOM bytes `EF BB BF`.
- No `:0` localisation keys were introduced.
- No em dash or semicolon appears in the player-facing YML text.
- No update-history or implementation/meta wording was found in the player-facing values.
- Manual review corrected repetitive wording in the National Settlement and Republican Veterans focus descriptions and concealed the hidden-route name in the sponsorless-movement achievement description.

## Recommended parent fixes

1. Add the three Northern scripted-localisation projections in the parent-owned `common/scripted_localisation/` surface for `slopx_ireland_northern_model`, `slopx_ireland_northern_region`, and `slopx_ireland_northern_failure_state`.
2. Re-run a read-only Northern GUI inspection/render after those definitions are wired, checking that locked states remain non-spoiler and that the live model, region, and failure state change with the active route and review state.
3. Keep the localisation file as the single definition site for the 3,015 audited keys. Do not duplicate the shared GUI close-button key or the BOP/focus shared National Settlement key.

## Validation not run

No live HOI4 launch, GUI render, or engine localisation parse was run in this worker because the task ownership is limited to the localisation file and handoff report. The source/reference audit, duplicate scan, malformed-line scan, BOM check, and player-facing punctuation/meta-word scan were run locally. Runtime validation should be performed by the parent after the Northern scripted-localisation projections are supplied.

## Unresolved wording decisions

- Focus, decision, and event text is source-derived implementation prose rather than a sourced quotation package. Historical quotation wording was not invented.
- Hidden-route descriptions remain intentionally indirect until the source gates expose those routes.
- Northern model, region, and failure labels are stable non-spoiler text pending the missing scripted-localisation definitions.
