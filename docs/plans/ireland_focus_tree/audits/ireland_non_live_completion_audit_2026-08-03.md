# Ireland non-live completion audit — 2026-08-03

## Scope and authority

This is the current source-level audit for `ireland_focus_tree` / `ireland`.
The canonical index and its listed specifications, maps, matrices, research
notes, and coding prompt remain authoritative. The offline Paradox wiki pages,
local vanilla documentation, vanilla precedents, and existing Ireland Total Overhaul
patterns were consulted for the touched systems. Hearts of Iron IV was not
launched, and live in-game testing is outside the completion gate by explicit
user direction.

## Current implementation inventory

| Surface | Current source result |
| --- | --- |
| National focus tree | 216 Ireland focus nodes, 197 authored connectors, Ireland-local MCP layout diagnostics: 0 |
| Route spirits | 3 persistent families |
| Decisions | 13 categories, 140 actions |
| Missions | 54 mission families; normal cap 8, emergency cap 10, emergency plus Northern occupation cap 12; command-cost ceiling 60 |
| Events | 256 historical-chain blocks plus 236 flavour blocks; all 495 event blocks have title, description, trigger, option, localisation, and cleanup/after handling |
| AI | 30 durable profiles and 10 temporary overlays, with concealed-route zero-weight policy and route-gated focus queues |
| Achievements | 32 canonical IDs; 96 runtime state sprites; static `hidden = yes` retained for A-22, A-27, A-28, and A-29 through A-32 |
| GUI | Exactly three decision-category surfaces: Conditions, Northern Settlement, and Concealed Evidence; the accepted public-achievement dossier is an extension of the third surface |
| Runtime gfx | Active texture references resolve under `gfx/`; `assets/` remains staging/source/processed evidence only |
| Icon audit | Runtime icon surface audit reports all required goal, law, spirit, category, action, mission, ledger, overlay, emblem, flag, and achievement surfaces complete |

The source-level gameplay audits also confirm zero focus grants for cores,
state transfer, or controller changes. The single Northern focus claim is a
claim-only contact effect; no focus grants Northern territory or cores. The
stage-five Northern integration review remains separate from claims, control,
occupation, settlement, and final core review.

## Accepted staged achievement disclosure

The local custom-achievement schema provides no supported trigger-valued menu
visibility field. The accepted A2 interpretation therefore keeps A-22, A-27,
and A-28 engine-compatible with fixed `hidden = yes` declarations and uses the
existing Concealed Evidence Ledger as the public reveal surface.

The third GUI now opens when the hidden-evidence gate is active or when one of
the three public reveal flags is present. Public-only mode hides the unrelated
evidence rows, shows only the individually revealed achievement entries, and
reuses each achievement's normal, grey, and not-eligible sprite state. Criteria
text and tooltips expose current German Leverage or Northern integration stage,
completion state, and the named permanent disqualifiers. A-29 through A-32
remain concealed and are not added to the dossier. No unsupported achievement
field, fourth GUI, or route-spoiler title was introduced.

## Source and asset boundary

The source manifest currently contains 169 entries: 166 complete and 3
blocked. Clearance counts are C1: 3, C2: 0, C3: 135, and C4: 31. The preserved
portrait archive contains 57 complete canonical portrait packages. Three exact
source portrait rows remain blocked and are not substituted or promoted:

- P-26 Patrick Cogan;
- P-45 Mick Fitzpatrick;
- P-55 Liam D. Walsh.

The runtime leader directory contains only wired objects with available source
evidence. The 57 complete portrait manifest rows now source their unmodified
originals directly from the flat `docs/portraits/` root; the old `assets/`
locations are recorded only as staging evidence, and processed 156x210 crops
remain derivatives. The latest
resolved portrait package is P-15 John Leydon, sourced from the exact captioned
30 April 1940 Catholic Archives delegation image and registered as a conditional
local-mod source package. P-31 Michael Browne remains complete from the captioned UCD
Digital Library image surfaced by RTÉ and wired as a post-1939 vocational-route
advisor. The Fairymount Schools' Collection evidence line is now surfaced in
the Otherworld flavour record with its CC BY 4.0 source and an explicit
testimony-is-not-proof caveat.

Round 16 added one exact-name NLI Poole lead for "Mr. Liam Walsh" (POOLEWP
3272), a 1925 Waterford uilleann-pipe portrait. It remains research-only: the
catalogue does not connect that sitter to canonical P-55 Captain Liam D. Walsh,
whose documented political work was Dublin-based. The lead is therefore an
identity-conflict rejection, not a sixth runtime portrait and not a substitute.
The dated decision record is
`assets/source_research_handoffs/portrait_exact_object_search_round16_2026-08-03.md`.

Round 17 checked an exact-name Third Tipperary Brigade group-photograph lead
for P-45 against the associated BMH witness statement. The witness is a
Tipperary-born 1898 local figure, not the canonical Dublin-based 1893 national
IRA leader, and the group image is too soft for a responsible leader render.
The lead remains research-only and does not alter the four-row blocked set.
The dated decision record is
`assets/source_research_handoffs/portrait_exact_object_search_round17_2026-08-03.md`.

Round 18 independently rechecked every remaining exact-person row. It found no
promotable object: P-15 remains outside the portrait window with no compatible
reuse basis; P-26 has no face-mapped or rights-cleared portrait; P-45 has only
unresolved commercial group-photo leads and no portrait object in the UCD
papers catalogue; and P-55 has no NLI Walsh portrait while the Waterford Poole
lead is a different person. The dated decision record is
`assets/source_research_handoffs/portrait_exact_object_search_round18_2026-08-03.md`.

Round 19 found a stronger period-fitting P-15 lead: the Catholic Archives
catalogue names John Leydon in a 30 April 1940 Irish delegation photograph
outside the Savoy Hotel. The record credits Keystone Press Agency, but the
public route returned a JavaScript challenge and exposed no exact image bytes,
crop locator, or image-level reuse permission. The lead was subsequently
resolved in round 24 after the exact master bytes and caption-mapped crop were
recovered; this metadata-only statement is retained as historical evidence.
The dated decision record is
`assets/source_research_handoffs/portrait_exact_object_search_round19_2026-08-03.md`.

Round 22 rechecked the same four rows and added a stronger identity lead for
P-45: the searchable illustration captions in Brian Hanley's copyrighted
*The IRA, 1926–1936* place Mick Fitzpatrick in an April 1932 Glasnevin group
photograph. The book and its restricted scan expose no reusable plate bytes or
image-level permission. P-26 still has no face mapping in the History Ireland
group photograph; at that round P-15 still had only the metadata-only Catholic
Archives / Keystone lead; and P-55 still had no Walsh face mapping in the
ArchivUL or NLI records. No portrait was promoted in round 22; round 24
subsequently promoted P-15 and left P-26, P-45, and P-55 blocked.
The dated decision record is
`assets/source_research_handoffs/portrait_exact_object_search_round22_2026-08-03.md`.

Round 24 promotes P-15 John Leydon from the exact Catholic Archives master
`CA_CP-3-16-5-51.jpg`. The printed caption maps Leydon as the leftmost sitter;
the exact source, processed crop, preserved source, runtime DDS, conditional
local-mod boundary, and hashes are recorded in
`assets/source_research_handoffs/portrait_exact_object_search_round24_2026-08-03.md`.
P-26, P-45, and P-55 remain the three unresolved exact-person portrait rows.

Round 25 rechecks P-26 Patrick Cogan against the direct image object used by
the *History Ireland* Clann na Talmhan article. The Athenry group photograph
has no face-level Cogan mapping, image-level licence, or exposed original
holding record, so it remains research-only. No crop, processed PNG, source
preservation file, DDS, or runtime registration was created. The handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round25_2026-08-03.md`.

Round 26 rechecks P-45 Mick Fitzpatrick and P-55 Liam D. Walsh. The FMA and
Hanley Fitzpatrick leads expose identity/context evidence but no face-mapped
reusable image object or image-level permission. The NLI and ArchivUL Walsh
records expose finding aids, correspondence, and unmapped group photographs;
the Waterford Poole Liam Walsh image is a different sitter. Both rows remain
C1/blocked. No source promotion, processed derivative, runtime DDS, or new
`docs/portraits` file was created; the negative findings are recorded in
`assets/source_research_handoffs/portrait_exact_object_search_round26_p45_2026-08-03.md`
and
`assets/source_research_handoffs/portrait_exact_object_search_round26_p55_2026-08-03.md`.

Round 27 checks a History Ireland image accompanying its account of the 1930
anti-Poppy Day platform, where Fitzpatrick is named as a speaker. The image is
instead a 1935 *Republican Congress* newspaper-cover illustration and contains
no Fitzpatrick portrait or face mapping. It remains research-only; no crop,
processed PNG, DDS, runtime registration, or `docs/portraits` file was created.
The dated handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round27_p45_2026-08-03.md`.

Round 28 checks the official Oireachtas image endpoints for P-26 Patrick Cogan
and P-45 Mick Fitzpatrick. Both return the generic 80x80 `Avatar` SVG rather
than a person-specific portrait. The new History Ireland Blueshirt rally image
checked for P-55 Liam D. Walsh is a group scene whose caption and visible
identity map O'Duffy, not Walsh; the article's surrounding mention of Walsh is
not a face-level mapping. All three objects remain research-only, with no
promotion, derivative, runtime registration, or new `docs/portraits` file. The
dated handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round28_2026-08-03.md`.

Round 29 rechecks P-26 and P-45 through the Carlow bibliographic lead, official
Oireachtas identity records, NLI catalogue leads, and the Brian Hanley/Maurice
Twomey caption trail. It finds no exact original image bytes with person-level
mapping and a defensible local-mod reuse boundary. No portrait source,
derivative, runtime DDS, GFX registration, or new `docs/portraits` file was
created. P-26, P-45, and P-55 remain the three explicit source blockers. The
dated handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round29_p26_p45_2026-08-03.md`.

Round 20 found an exact-period ArchivUL photograph of Irish Brigade officers
outside the Cáceres barracks, dated January 1937. The item names no individual
officers, exposes no image bytes, and leaves reproduction conditions blank;
its unrestricted-access statement is not a reuse grant. It therefore does not
establish Liam D. Walsh as a sitter or change the four blocked rows. The dated
decision record is
`assets/source_research_handoffs/portrait_exact_object_search_round20_2026-08-03.md`.

Round 21 found a second exact-period ArchivUL officer-corps photograph, dated
May 1937, whose reverse note identifies O'Duffy seated in the centre. The item
does not identify Walsh or map any other face to a name, exposes no image
bytes, and leaves reproduction conditions blank. It therefore does not
establish Liam D. Walsh as a sitter or change the four blocked rows. The dated
decision record is
`assets/source_research_handoffs/portrait_exact_object_search_round21_2026-08-03.md`.

## Runtime consumer reconciliation

The current crosswalk and direct source scan now agree on the live image
consumers. All 51 generated event/news images have an exact `picture =` use in
an Ireland event, and all 69 canonical `EV-SRC-*` event/news rows resolve to
their intended Ireland-owned event sprite. 56 of the 57 complete canonical
portrait rows have semantic non-`.gfx` character or campaign-initialisation
consumers. P-15 is registered as a conditional local-mod source package
without an invented gameplay consumer; P-26, P-45, and P-55 remain
unregistered exact-source blockers. The stale line references that had
made valid consumers appear absent were refreshed in
`assets/asset_coverage_crosswalk.md`; no unrelated event or portrait consumer
was invented.

## Non-live validation evidence

- Fresh engine-reference checks on 2026-08-03: `hoi4.focus_inspect` reports
  216 Ireland focus nodes, 197 authored connectors, zero Ireland-local layout
  diagnostics, zero crossings, zero node intersections, zero long connectors,
  and a minimum same-row spacing of 3. Its 14 blocking icon diagnostics belong
  to the unrelated vanilla continuous-focus palette and are not part of the
  Ireland tree.
- A fresh `hoi4.focus_render` returned `FOCUS_RENDERED` for
  `ireland_focus_tree` from the Ireland source. The retained artifact is
  the expected Ireland tree render; the 14 reported blocking messages are the
  same unrelated vanilla continuous-focus sprite references, not Ireland-tree
  diagnostics. This is offline reference evidence, not live game validation.
- `hoi4.map_inspect` reports a valid shared map revision: province definitions,
  bitmap geometry, state/strategic-region membership, adjacencies, supply and
  railway networks, ports, and locators all pass. It reports no unknown or
  missing-geometry province IDs. `hoi4.event_inspect` returns zero blocking
  diagnostics for the Ireland event namespace with no skipped Ireland source;
  its workspace-wide helper/lifecycle projection remains explicitly partial.
- The weighted mission adapter reads the Ireland decision source with 70
  mission candidates, 13 required inputs, and zero unresolved inputs. The
  adapter reports the pool as incomplete because the source contains only the
  Ireland file under inspection; this is an analyzer scope result, not a
  gameplay omission. Focus, decision, and event probability adapters returned
  MCP internal errors for this large custom source and therefore are not used
  as positive evidence; the existing source-level AI audits remain authoritative.
- `hoi4.gui_inspect` completed against workspace `mod_ireland_total_overhaul_65a6b5f140a7`; the updated evidence GUI produced no Ireland-local unresolved references. The remaining MCP index diagnostics are unrelated global/controlled-reuse texture diagnostics.
- `hoi4.gui_render` completed the updated evidence window for the offline `ireland_audit` scenario at 1280×720 across normal, locked, warning, and long-text states. This is deterministic layout/reference evidence, not a live game claim.
- A fresh `hoi4.gui_render` pass also returned `GUI_RENDERED` for all three authored windows—Conditions, Northern Settlement, and Concealed Evidence—at 1280×720 across normal, locked, warning, and long-text states. The MCP response truncation notices are wire-budget notices only; linked render artifacts were retained. This is deterministic layout/reference evidence, not a live game claim.
- The 2026-08-03 GUI re-audit inspected all three authored windows with the
  current `ireland_audit` scenario: 58, 40, and 57 elements respectively. The
  aggregate MCP projection reports 97 diagnostics and intentional overlap
  counts of 10, 9, and 29; the complete disposition is recorded in
  `audits/ireland_gui_engine_reference_reaudit_2026-08-03.md`. These are
  mutually exclusive animation/fallback, status, dossier, and button-label
  layers, plus the documented 140-name/70-texture controlled-reuse index
  warnings, not unresolved runtime GUI defects.
- `audit_runtime_icon_surfaces.py` reports `all_complete: true` for all ten required runtime icon surfaces.
- The direct event/portrait consumer audit reports 51/51 generated event images,
  69/69 canonical sourced event rows, and 56/57 complete canonical portraits
  with live consumers; P-15 is the explicitly registration-only package, and
  the three blocked portrait rows remain outside that set.
- Targeted source checks report no missing new dossier localisation keys, no missing dossier GUI elements or visibility triggers, the required localisation BOM, balanced touched script blocks, and no active consumer path under `assets/`.
- Mission, action, event, achievement, focus, route-gate, Northern-core, and source-consumer audits remain reconciled to the canonical counts listed above.

## Simplifications, omissions, and blockers

The current source is not marked complete because three exact historical portrait
objects remain blocked by the source/rights/identity requirements above. No
generated likeness, wrong-person image, generic avatar, or fallback portrait was
used to hide those rows. Live HOI4 testing is intentionally omitted rather than
treated as a blocker, per user direction. No other simplification was made in
the 2026-08-03 implementation tranche; rounds 16, 17, 18, 19, 20, 21, 22,
and 23 documented
rejected identity-conflict or unresolved-source leads and did not change the
manifest.

## Round 23 portrait-source addendum (superseded for P-15 by round 24)

The direct official object checks did not close the four source blockers. The
Oireachtas Patrick Cogan image endpoint returns the site's generic 80-by-80
SVG Avatar placeholder rather than a Cogan portrait. The public Google Books
page image for the Hanley P-45 lead returns an image-not-available placeholder.
The Catholic Archives P-15 record still exposed metadata only during that
round, while the NLI and ArchivUL P-55 records still exposed no mapped Walsh
portrait. Round 24 subsequently recovered the exact P-15 master and promoted
it; P-26, P-45, and P-55 remain blocked.
The dated decision record is
docs/plans/ireland_focus_tree/assets/source_research_handoffs/portrait_exact_object_search_round23_2026-08-03.md.

## Independent completion-auditor follow-up

The read-only completion auditor found no additional gameplay, localisation,
AI, achievement, asset-wiring, or runtime-path omission. Its earlier
pre-round-24 snapshot confirmed the 216-focus, 13/140/54 decision-mission,
495-event, 30-profile/10-overlay, 32-achievement, and 165-complete/4-blocked
manifest reconciliations. That portrait count was superseded by the round-24
P-15 promotion; the current manifest is 166 complete / 3 blocked. It found two
documentation-only discrepancies: stale GUI cardinalities, corrected in this
tranche to 58/40/57 elements and 10/9/29 reported visible overlaps, and the
A-20 source comment's stale P/A class, corrected to canonical P. The
route-extension RC-PORTRAIT-02 remains outside the canonical 169-row budget.

## Round 31 exact-source closure

The final bounded source pass did not change the blocked set. P-26 Patrick
Cogan remains blocked after distinct National Library of Ireland, UCD,
Oireachtas, and Wikimedia Commons identity/object checks; no exact portrait
object or face-mapped, rights-cleared group was found. The evidence is recorded
in `assets/source_research_handoffs/portrait_exact_object_search_round31_p26_2026-08-03.md`.

P-45 Mick Fitzpatrick remains blocked after review of the official Military
Archives MSPC records `MSP34REF63535` and `34D2519`. Those files establish the
canonical identity and service history but contain no photographic portrait or
face-mapped group, so neither PDF was extracted or placed in `docs/portraits`.
The evidence is recorded in
`assets/source_research_handoffs/portrait_exact_object_search_round31_p45_2026-08-03.md`.

The 57 complete flat originals remain the only canonical portrait source inputs;
the round-31 research PDFs and all other research packages remain staging or
provenance evidence. No new `docs/portraits` subfolder was created, and no
156x210 derivative is used as a source input.
