# Final mechanics-hub localisation audit — 2026-08-15

## Scope

Audited the National Situation Ledger and focus-tree inlay localisation in:

- `localisation/english/ireland_l_english.yml`
- `common/scripted_localisation/ireland_localisation.txt`

References reviewed: `AGENTS.md`, the mechanics-hub specification and value-purpose matrix, the National Situation Ledger documentation, the corrective addendum, existing mechanics-hub handoffs, the required offline wiki localisation/scripted-GUI pages, and the relevant vanilla localisation/focus-inlay documentation.

No gameplay, GUI source, focus-tree, asset, or thumbnail files were edited. No commit was created.

## Localisation patch

### `localisation/english/ireland_l_english.yml`

Changed or added these mechanics-hub keys:

- `ireland_mechanics_hub_summary_northern_archived`
- `ireland_mechanics_hub_refresh_available`
- `ireland_focus_inlay_instruction`
- `ireland_focus_inlay_northern_archived`
- `ireland_focus_inlay_northern_failure`
- `ireland_focus_inlay_northern_critical`
- `ireland_focus_inlay_northern_ready`
- `ireland_focus_inlay_northern_warning`
- `ireland_focus_inlay_northern_open`
- `ireland_focus_inlay_culture_archived`
- `ireland_focus_inlay_culture_locked`
- `ireland_focus_inlay_culture_public`
- `ireland_focus_inlay_culture_critical_sealed`
- `ireland_focus_inlay_culture_critical_revealed`
- `ireland_focus_inlay_culture_critical_evidence`
- `ireland_focus_inlay_culture_ready`
- `ireland_focus_inlay_culture_ready_evidence`
- `ireland_focus_inlay_culture_warning`
- `ireland_focus_inlay_culture_warning_evidence`
- `ireland_focus_inlay_culture_revealed`

Before, the inlay exposed North as a lone integration stage and Culture as a lone capacity/evidence number. After the patch, each uses a short primary state phrase, with the North stage or public Culture/evidence marker secondary. The branch wording is now truthful for locked, archived, failure, critical, ready, warning, sealed, revealed-disqualifier, and revealed-evidence states. The Northern summary explicitly says the record is archived, closed, and read-only after `ireland_route_archived`. Refresh text now promises only the displayed report and public bottleneck/route-status summaries. The inlay instruction uses the exact “National Situation Ledger” category name.

### `common/scripted_localisation/ireland_localisation.txt`

Changed these defined-text blocks:

- `GetIrelandMechanicsHubSummary`: added an archive-first Northern summary branch for `ireland_route_archived`.
- `GetIrelandMechanicsHubInlayNorthern`: archive, locked, failure, critical, ready, and warning priority branches using the existing hub predicates.
- `GetIrelandMechanicsHubInlayCulture`: archive, locked, critical/disqualifier, critical/revealed, critical/sealed, ready, warning, and evidence-reveal branches using the existing hub predicates. Concealed evidence counts are not selected before `ireland_concealed_evidence_revealed`.

## Required audit output

### Missing keys

None found for the scripted-localisation references in the file. The new inlay and archived-summary keys all resolve.

### Duplicate keys

None found: exact localisation-key scan returned zero duplicates; defined-text `name` scan returned zero duplicates.

### Scripted-localisation issues

`GetIrelandMechanicsHubPurpose` still has unreachable `ireland_mechanics_hub_purpose_*` fallback branches. The earlier consequence branches match first for every valid tab, and `interface/ireland_national_situation.gui` has only one post-detail text slot (`[GetIrelandMechanicsHubPurpose]`). That slot currently displays the consequence contract, not a separate family-purpose line. Do not reorder those branches without adding or repurposing a GUI slot; doing so would hide the current consequence/gate/next-action text.

`GetIrelandMechanicsHubSelection` intentionally reuses the existing `ireland_conditions_selection_*` and `ireland_northern_selection_*` descriptions. They provide the row purpose, consumers, and improvement wording, but are not mechanics-hub-prefixed keys.

### Dynamic-text opportunities

- The North/Culture inlay was the confirmed P1 proxy problem and is patched.
- Foreign leverage detail keys (`ireland_mechanics_hub_detail_foreign_british`, `..._american`, `..._german`, `..._vatican`, and `..._dependence`) explain use and risk but do not name explicit positive/reduction sources as strongly as the State, Provision, Readiness, Northern, and most Culture descriptions. If the strict value-purpose requirement is retained, add named focus/action sources in a later bounded wording pass.
- `ireland_mechanics_hub_detail_culture_capacity` explains purpose and consumers but does not name its authored capacity-improvement actions. This was left unchanged to avoid broad text churn in the concurrent localisation addition.

### Cross-surface mismatch notes

- The inlay status text now follows the same `ireland_mechanics_hub_*_{locked,critical,ready,warning}` predicates used by `common/focus_inlay_windows/ireland_national_situation_inlay.txt`.
- Archive text is now explicit for the selected Northern summary and both North/Culture inlay text helpers. The status sprite remains the existing locked fallback; action/refresh availability remains owned by the GUI/scripted-GUI agent.
- The full hub's selected-row explanation carries purpose/consumer/source prose; its dynamic line is consequence/gate/next-action prose despite the helper name `GetIrelandMechanicsHubPurpose`.

### Encoding concerns

`localisation/english/ireland_l_english.yml` retains a UTF-8 BOM (`EF BB BF`). `common/scripted_localisation/ireland_localisation.txt` remains a plain Clausewitz script without a BOM; no encoding conversion was made.

### Long-text/clipping risk

The new inlay phrases were shortened to keep the primary state ahead of the secondary marker. Full-hub detail, consequence, requirements, and tooltip strings still need the GUI owner's deterministic long-text review at both target resolutions. The renderer scenarios supplied unresolved dynamic values, so this handoff does not claim final pixel-level clipping proof.

## Validation

- Static localisation scan: 6,209 YAML keys; 0 duplicate keys; 55 defined-text names; 0 duplicate names; 0 missing `localization_key` references; YAML BOM present.
- Read-only GUI inspection succeeded for `ireland_focus_inlay_operational` and `ireland_mechanics_hub_long_text`; source graphs parsed without blocking diagnostics.
- Useful artifact URIs:
  - `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/ce67499b28cbf1f614d527ae149ac3377dcae0bb0675668e3c2a61d99bc6245a/08f722349651c6f2c15104d04ee335a381ed5d3b33682a759b8fa5fcf8c5ad97/gui-inspect.b51c8ed78fdfaf14.json`
  - `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4ddccc0a5653afcd15e3d30140a90f4a41d81bbdc6ae9e3ac911c9f209264d12/5195c35fbf5833c92fdcf4bf2ffca3886a8826cccbd69d4d11538cd95f2882d1/ireland_national_situation_inlay_window-full.svg`
  - `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/4aeb144a075f125fb39802ca9d5c2ea45b69f269f013bcf5f6b336d1556c22fd/b6ba23b9c4fa614042827417a3a55de8ea4dc67eb88c3d81235c540b2c0d5fa7/gui-inspect.d4ac6db8082b16d2.json`
  - `hoi4-agent://workspace/mod_ireland_total_overhaul_aaca88216c92/artifact/9ac5699ae35950a24ca5327f2e0e0838a3bfd2c3a7ad27e3363f718a28aa6554/32a9f8161bbb3248c721278fb84b77aace3bb5e1da9cda797a6ad7b071b381a4/ireland_national_situation_window-full.svg`
- GUI inspection reported unresolved scenario dynamic values and existing layout overlap/partial-sprite diagnostics; those are GUI/scenario evidence limits, not localisation-key failures. No GUI source was changed in this localisation handoff.

## Blockers and simplifications

- Family-purpose localisation remains unreachable in `GetIrelandMechanicsHubPurpose` until the GUI owner provides a separate purpose slot or deliberately merges purpose and consequence text.
- Foreign-detail and Cultural Capacity source wording remains an audit recommendation, not a patch; no mechanics were invented or changed.
- No aggregate, concealed value, route gate, or gameplay meaning was added or altered. `thumbnail.png` was not touched.

## Parent closure after the final GUI reflow

The blocker recorded above is closed in the frozen source. `GetIrelandMechanicsHubPurpose` was split into `GetIrelandMechanicsHubFamilyPurpose` and `GetIrelandMechanicsHubConsequence`; `interface/ireland_national_situation.gui` now has separate family-purpose and current-consequence slots in addition to the selected-row explanation, state-dependent selected-status line, and next-action line. All six `ireland_mechanics_hub_purpose_*` branches are reachable, the consequence helper has 34 row-specific branches plus archive/lock overrides, and the selected-status helper identifies the active bottleneck, greater autonomy risk, Northern stage, or Evidence proof state. Final dashboard inspection revision `f8fc5fbe5ea0d72c` reports no blockers or unintended text/control overlap. The remaining overlap notices are the intentionally co-located mutually exclusive status sprites and click-transparent selected-tab overlays.
