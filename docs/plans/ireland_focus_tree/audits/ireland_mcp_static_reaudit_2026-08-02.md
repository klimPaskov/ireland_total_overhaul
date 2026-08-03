# Ireland offline MCP static re-audit — 2026-08-02

## Scope

This is a fresh read-only MCP inspection of the authored Ireland focus,
event, and GUI surfaces. Hearts of Iron IV was not launched. Live engine
play, fresh saves, and scenario playthroughs remain excluded by the user's
completion-gate direction.

Workspace: `mod_ireland_total_overhaul_65a6b5f140a7`.

## Focus tree

The national-focus inspection of
`common/national_focus/slopx_ireland_focus_tree.txt` returned
`FOCUS_INSPECTED` with status `ok` for tree
`slopx_ireland_focus_tree`:

| metric | result |
|---|---:|
| focus nodes | 216 |
| resolved titles | 216 |
| connectors | 197 |
| connector crossings | 0 |
| node intersections | 0 |
| long connectors | 0 |
| maximum horizontal span | 8 |
| maximum Manhattan span | 10 |
| minimum same-row spacing | 3 |
| Ireland-tree diagnostics | 0 |

Latest focus artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/ac4c08115c9295a567410cd45e3fd888fcdff79515dd15ca2751f214d6b142e5/722d22cef2a21461e97246ec9a12d710c701f01ae90007afa6c226c03a504ae9/focus-inspect.c7b5d17b3be731b5.json` (revision `c7b5d17b3be731b5407e9df5714c9e7201022de1a40ff1d5661526186af4f70`; layout hash unchanged).

The follow-up focus readback after wiring the rejection recovery handoff and
isolating the route-specific reveal flags also returned `FOCUS_INSPECTED` with
zero Ireland-local diagnostics. Its artifact is
`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/6fbbb487dfc300f99a3ae4eca7d554a80e76225806fe4fd117278843a0c04a99/893913ba45558141a608688de2d040fb612a4fda1a7a0ae292b560c4fabe1ffb/focus-inspect.b30c56a235564e37.json` (revision `b30c56a235564e37eacbb0de88a31da58fe85184577695ecab134aac6f3200c9`).

The global response also lists fourteen unrelated vanilla continuous-focus
sprite-reference errors from the installed generic tree. They are outside
the authored Ireland source and were not changed.

## Event namespace

The bounded namespace lint for `slopx_ireland_events` returned
`EVENT_INSPECTED_PARTIAL` with status `ok` and `blockingDiagnostics: 0`.
The partial result is the MCP large-workspace boundary: helper and lifecycle
projections are deferred in the global inventory, not reported as Ireland-local
blocking diagnostics. The filtered source contains the current standard and
flavour event families documented by the final non-live audit.

Latest event scan artifact: `hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/48c2d9ad12e37f2bb0b186e45c09493e1fb2a86c9b5b1568bafbe736d61322e6/ac82e97b5f276b6950a0bb2b8256687ddd1879a4c8a3b883f897bba4b3284067/event-scan-6e096b930451.json` (graph hash `984a16...`; blocking diagnostics 0; workspace projection remains partial by design).

The focused event lint and options render were rerun for the repaired
`slopx_ireland_events.437` node. Both returned `status: ok` with
`blockingDiagnostics: 0`. The render manifest is
`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/59266970286f4d7453198686570cd0dbe0e7fbba4990eb2284fcfb9a2475bd74/47b3414aa7338331911bc47bfce656efae3838c8bb814224aae4ef0beb9ba985/event-options-6e096b930451-manifest.json`;
the bounded options JSON is
`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/59266970286f4d7453198686570cd0dbe0e7fbba4990eb2284fcfb9a2475bd74/639d082e39d81bff400ce0ee043751f28566b319e7029762626eea2f272d8e68/e545d892d7a08e98918a2c6c4a0afb42adc74a7418159fd60fa173cdcdf19d70/event-options-6e096b930451.json`.

After the human-restoration handoff and route-specific reveal isolation were
added, the focused event lint/render returned `status: ok` with zero blocking
diagnostics again. The refreshed lint artifact is
`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/9117b4dd7a4626cb5dc8a1b0bb29b39644494a8281992cbdc3bfcf7ea3ef9703/6acebd56108957e16890c8e6b0a708c5c8c4d5d6962aa62438e4ee56cbf773f9/event-lint-71e332deae14.json`; the refreshed options render is
`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/77a2a2de68ea0be3d85f42875f8ebd6acc372add657080d62d84188eb9aabb19/207091be55372547cabc26bbd7a6822be48687fe1bb51f409fe9b6704291fe82/event-options-71e332deae14-manifest.json`.

The event compare call was also attempted against the prior scan revision and
the current graph artifact. The prior scan is a bounded report projection, not
an importable event-graph snapshot, and the game-backed workspace does not
retain a full comparable revision. The MCP service therefore returned
`EVENT_GRAPH_ARTIFACT_INVALID`, `EVENT_REVISION_NOT_CACHED`, and
`EVENT_BASELINE_MISSING` for those compare forms. This is recorded as a tool
boundary; it does not add an Ireland source blocker. The source review below
is the authoritative repair evidence.

## GUI graph

The fresh GUI inspection returned `GUI_INSPECTED` with `complete: true` and
`validation.passed: true`:

| graph metric | result |
|---|---:|
| nodes | 45,018 |
| edges | 101,982 |
| elements | 23,370 |
| sprites | 17,457 |
| fonts | 183 |
| scripted GUIs | 20 |

The diagnostic list includes the intentional 140 named action sprites over 70
textures. `ireland_gui_texture_reuse_engine_reference_2026-08-02.md` records
the direct source counts and the vanilla precedent for repeated
`texturefile` paths. It is not a duplicate sprite-name or missing-runtime-file
defect.

## Final readback after source-clearance round 11

The authored surfaces were read again after the round-11 source-clearance
documentation pass. The focus result again reports 216 Ireland nodes,
197 connectors, zero Ireland-local layout diagnostics, zero crossings, zero
intersections, and zero long connectors. Its current artifact is
`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/acacac5c3ae51fd7e8b5c1a5b8baefdab21afb17270f962dede7d3d63af6006d/802e5c93f6a1585776d818a19822e30083ca8d4f23a5a017817cc714794d8aec/focus-inspect.cd726b73c0ef5456.json`.

The GUI result again reports a complete connected graph with 45,018 nodes,
101,982 edges, 23,370 elements, 17,457 sprites, 183 fonts, and 20 scripted
GUIs. Its current artifact is
`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/43769184f3efd033380580e523d0e9c74b9f1532d6d0538faca0ca14dcf14c10/2c8cd295eaf4c8cddbb3cd8f4efb31af6929d0b0095a8dd6ef17c5f8b896b5b6/gui-inspect.8f9e40269f2ebf8c.json`.

The focused Otherworld event lint again returned `status: ok` with zero
blocking diagnostics. The current bounded lint artifact is
`hoi4-agent://workspace/mod_ireland_total_overhaul_65a6b5f140a7/artifact/9117b4dd7a4626cb5dc8a1b0bb29b39644494a8281992cbdc3bfcf7ea3ef9703/95321fd72807afce82d537dbb6a25fd7cfde02316ce87645e3acee7fb0a7149d/event-lint-71e332deae14.json`.

## Disposition

The fresh inspections close the local static MCP check for the authored Ireland
surfaces. The focus tree has no Ireland-local layout diagnostic, the Ireland
event namespace has no blocking diagnostic in its bounded lint, and the GUI
graph is complete and connected. Global-tool limitations and unrelated vanilla
diagnostics remain explicitly scoped rather than silently treated as Ireland
failures.

The following source-level repairs are included in this re-audit:

- The Otherworld route now remains plausible through folklore, archive,
  investigation, and pre-verification containment. It enters the absurd family
  only after the explicit archive-reveal event writes the impossible-evidence
  flags, or at the authored final convergence. The historical-event dispatcher
  uses the same absurd-route boundary.
- Before any route commitment, the serious-culture AI opening and the completed
  Tier-1 folklore/archive lane retain the historical `H` profile. The
  Otherworld AI opening is also `H`; the Otherworld investigation focus is the
  explicit transition to plausible `P`, and only
  `slopx_ireland_events.437` can move the route into `A`. An AI preference alone
  cannot reveal the hidden route.
- The canonical four-choice event `The Archive Records What Has Not Yet
  Happened` requires the independent witness ledger, rare-condition threshold,
  council authority, and concealed-transition authority. Its four options own
  the contact, containment, exploitation, and human-restoration outcomes. The
  rejection option opens the existing `Recovery Bridge`, which hands into
  `Restore Constitutional Calendar`; its review flags are transient, its
  completion record is durable, and the route remains classified A throughout.
  Cleanup clears the transient event and restoration-review flags after the
  durable choice is stored.
- The shared `slopx_ireland_verified_impossible_reveal` flag remains a
  High-King/Five-Provinces and convergence result. It is not an Otherworld
  admission gate: the Otherworld profile, guardian readiness, focus gates, and
  `.437` dispatch use the route-specific
  `slopx_ireland_otherworld_impossible_confirmed` or
  `slopx_ireland_otherworld_archive_reveal_complete` flags. A different hidden
  route therefore cannot suppress or bypass the canonical Otherworld event.
- The Dillon named-vote gate is supplied by
  `common/scripted_triggers/slopx_ireland_dillon_gate_repair.txt` and is used
  by both the named decision gate and the final event war-entry gate. The
  invasion-danger exception is not allowed to synthesize the named vote.
- The 140 decision actions now call two documented shared scarcity helpers for
  their severe/watch surcharges. Their authored base Political Power,
  Command Power, burden, physical inputs, mission outcomes, and AI hints
  remain action-specific.
- A2 is closed by the explicit project-owner ruling in
  `authority_rulings_m2_a2_c3_2026-08-01.md`: A-22, A-27, and A-28 retain
  scalar `hidden = yes` and canonical reveal conditions in `happened`.
  Offline achievement documentation and the installed vanilla achievement
  file expose no supported trigger-valued `hidden` or dynamic `visible`
  schema, so no undocumented syntax is introduced. The completion-auditor
  suggestion to replace this with dynamic visibility is superseded by that
  ruling, not an open Ireland-local defect.
