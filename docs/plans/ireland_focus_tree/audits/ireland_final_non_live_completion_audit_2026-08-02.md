# Ireland final non-live completion audit — 2026-08-02

Status: historical 2026-08-02 snapshot. The 2026-08-03 round-15 promotion and
non-live audit supersede its numeric asset counts; consult
`ireland_non_live_completion_audit_2026-08-03.md` and
`source_of_truth_map.md` for current authority. Hearts of Iron IV was not
launched, in accordance with the user's instruction that live in-game testing
is outside this completion gate.

## Verified implementation surface

The current source and crosswalk reconcile to 216 focus nodes, 13 decision
categories, 140 actions, 54 mission families, 106 spirit rows, 32
achievements, and 169 canonical asset-manifest rows. The 236 flavour-event
minimum is present as 236 distinct flavour events, alongside the historical,
crisis, foreign-reaction, GUI, AI, Northern, neutrality, and postwar source
surfaces described by the canonical package.

The fresh offline MCP re-audit in
`ireland_mcp_static_reaudit_2026-08-02.md` resolves all 216 Ireland focus titles,
197 connectors, zero Ireland-local layout diagnostics, zero connector
 crossings, zero node intersections, and zero long connectors. Its 14 reported
 errors are unrelated vanilla continuous-focus sprite references in the global
 workspace. The focused Ireland event inspection reports zero blocking
diagnostics; its validation remains partial because the large workspace defers
global helper and lifecycle projections.

The three GUI windows have current source-graph evidence for 58, 40, and 36
elements. Their reported overlap set is limited to mutually exclusive
animation/static-fallback layers, mutually exclusive status layers, and text
drawn over its own button plate. The action texture reuse is intentional and is
documented against the vanilla shared-texture pattern in
`ireland_gui_texture_reuse_engine_reference_2026-08-02.md`. The current
connected GUI graph inspection is complete with `passed: true`; the remaining
texture-reuse, font-metric, and unsupported-render-field messages are
classified offline-tool/reference limitations rather than Ireland-local sprite
or layout defects.

## Runtime asset placement

Final runtime assets are under `gfx/`. The `assets/ireland_focus_tree/` tree is
staging-only for source originals, processed previews, manifests, contact
sheets, and review evidence. A runtime path scan found no active `assets/`
texture path.

Current runtime counts include 216 goal DDS files, 51 law-stage DDS files, 63
route-spirit DDS files, 72 leader portraits, 121 event/news DDS files, 11 GUI
textures, and seven independent animation families with static fallbacks. The
fresh goal, law, and spirit packages were regenerated as separate assets,
read back successfully, and checked for alignment, neighboring atlas bleed,
opaque boxes, and chroma-key residue. The full 216-goal and 51-law packages are
installed under `gfx/interface/`.

The regenerated asset crosswalk now finds a non-.gfx consumer for all 69
complete sourced event/news rows and all 55 complete portrait rows. The two
period-blocked portrait rows P-15 and P-31 remain registered only for source
review and have no character or gameplay consumer; the three identity blockers
P-26, P-45, and P-55 remain unregistered in runtime.

## Source-clearance blocker

`docs/plans/ireland_focus_tree/assets/source_manifest.json` currently contains:

| family | complete | blocked | total |
| --- | ---: | ---: | ---: |
| real-person portraits | 55 | 5 | 60 |
| historical symbols/documents | 40 | 0 | 40 |
| sourced event/news slots | 69 | 0 | 69 |
| total | 164 | 5 | 169 |

The five blocked rows are P-15, P-26, P-31, P-45, and P-55. P-15 and P-31
retain source-only review bytes but are blocked from final use because their
only exact images are non-free and outside the 1936-1945 portrait window; no
later image is used as a placeholder. P-50 is complete from the
exact, face-mapped 1921 Tom Barry wedding source documented in the round-13
handoff, and P-54 is complete from the exact, caption-mapped 1936 Irish Brigade
group photograph documented in the round-14 handoff. All symbol/document and
event/news rows now have complete staged and runtime packages under their
recorded conditional or unrestricted source boundaries.

No cleared final DDS is accepted for the five remaining blocked rows. S-06 and S-08
are complete C3 exact-period poster alternates promoted under their recorded
alternate-object conditions; S-33 is a complete C3 source package with an
exact NLI source, processed crop, staging DDS, and promoted runtime DDS. The
30-row round-12 C3 package and the two source-only period blockers are
recorded in the dated handoff. Attribution,
controlled-reuse conditions, and remaining identity uncertainty remain visible
in the manifest and source-clearance handoffs. The earlier bounded clearance
search rechecked the then-37-row queue before round 12; see
`assets/source_research_handoffs/final_clearance_remaining_ireland_rows_2026-08-02.md`.
The round-10 follow-up is historical evidence for the queue before the
round-12 conditional promotion. No generated likeness, generic substitute, or
fallback was introduced. The event/news surface is now 120/120.

The latest research confirms that the DIFP online edition does not provide a
blanket reuse licence, and Military Archives material requires object-level
permission for reproduction beyond research or personal use. The relevant
policies are [DIFP editorial policy](https://www.difp.ie/editorial-policy/),
[Military Archives deposit terms](https://www.militaryarchives.ie/uploads/documents/Archive_deposit_agreement_updated_version_December_2016.pdf),
and [Military Archives researcher rules](https://www.militaryarchives.ie/fileadmin/user_upload/documents/Researcher_Administration/Rules_and_information_for_researchers_in_the_Military_Archives_updated_18_August_2016.pdf).
The UCC Alfred O'Rahilly portrait is an exact identity source but remains
marked controlled by UCC rather than promoted without permission; see the
[UCC collection record](https://www.ucc.ie/en/heritage/collections/portrait-james-sinton-sleator-prha-1885-1950-alfred-orahilly.html).

## Completion disposition

The gameplay package, icon regeneration and runtime placement, localisation,
AI routing, GUI wiring, source crosswalk, and non-live audits are reconciled.
The goal must remain open until the five blocked portrait rows receive exact
person-labelled source objects or the missing identity objects are supplied.
Live in-game testing is intentionally omitted and is not counted as a blocker.

The latest static repair tranche also reconciles the Otherworld H/P/A
boundary, including the historical `H` serious-culture/archive opening, the
historical Otherworld AI opening, the investigation focus committing `P`, and
the explicit four-choice `slopx_ireland_events.437` archive-reveal event that
commits `A`. Its rejection branch opens the existing recovery bridge and
constitutional-calendar restoration sequence without returning the campaign
to H; the verified impossible occurrence remains an A-state historical fact.
The same tranche retains the Dillon named-vote helper, shared decision
scarcity charges, and user-approved A2 static-hidden achievement contract.
The event source now contains 256 authored standard event definitions,
including the canonical archive-reveal node and all four durable choice
branches; its targeted offline MCP lint/render returned zero blocking
diagnostics. The route-specific reveal flags cannot be synthesized by the
High-King/Five-Provinces shared reveal writer, so a different hidden route
cannot suppress this event. These repairs do not reduce the source-clearance
gate: the five blocked portrait rows remain the outstanding canonical asset
blockers recorded by this audit.
