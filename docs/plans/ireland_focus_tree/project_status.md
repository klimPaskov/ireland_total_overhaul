# Ireland Focus Tree Project Status

Feature slug: `ireland_focus_tree`

Feature: Ireland gameplay overhaul and national focus tree (completion audit in progress)

## Full-mod audit refresh: 2026-08-05

The current live source contains 211 focuses with one root, 14 decision
categories, 144 primary actions plus 4 Marine Service actions, and 54 mission
families. The improvement loop removed ordinary repeated focus reward bundles,
restored the convergence AI focus chain, closed stale election/lifecycle flag
aliases, made Atlantic route protection one-time, added parliamentary outcome
tooltips, and made composite AI plans relinquish ownership to precise profiles.
MCP focus inspection reports 234 connectors with zero crossings, node
intersections, long connectors, or same-row overlap. The parliament GUI source
graph has no overlap or budget blockers across the rendered state matrix. A
direct `hoi4.exe -debug` launch after these repairs produced an empty
`logs/error.log`. The three blocked portrait rows P-26, P-45, and P-55 remain
blocked because exact cleared source was not supplied; no substitute was used.

The 2026-08-03 snapshot below is retained as historical provenance.

## Historical authority snapshot: 2026-08-03

The 2026-08-03 round-15 and round-24 source promotions, round-16 through
round-18 and round-25 through round-31 exact-object rejections,
public-achievement dossier tranche, fresh focus/event/map/GUI engine-reference checks,
and non-live completion audit supersede the older numeric snapshot in this
checkpoint. The normalized authority ledger is
`docs/plans/ireland_focus_tree/source_of_truth_map.md`.

The latest non-live engine pass reports zero Ireland-local focus layout
diagnostics, valid shared map definitions and networks, zero blocking
diagnostics in the Ireland event namespace, and no skipped Ireland event
sources. The mission probability adapter resolves its inspected source inputs;
global vanilla diagnostics and analyzer-scope errors remain explicitly
separated from Ireland implementation evidence.

The portrait-source boundary is now flat: all 57 complete portrait manifest
rows point to unmodified originals directly under `docs/portraits/`. Temporary
`assets/` paths are retained as staging evidence only; processed 156x210 crops
are derivatives and final runtime DDS files remain under `gfx/`.

The user-approved M2 and A2 decisions are implemented. M2 preserves exactly
13 decision categories, 140 action definitions, and 54 mission definitions by
merging the by-election and parish-audit modes into their base missions and
using mission ordinals 006 and 009 for the two new Radical/Underground
families. A2 keeps A-22, A-27, and A-28 statically hidden with their canonical
earned/reveal conditions; no unsupported dynamic achievement-visibility syntax
is used. The two M2 replacement mission declarations are physically nested
under Radical/Underground, not merely activated by its actions.

The 2026-08-01 Dillon/O'Duffy route-gate repair is recorded in
`audits/ireland_dillon_oduffy_gate_repair_2026-08-01.md`. Dillon now has live
mandate progression, a separately earned named-vote transition whose gate
cannot use the invasion exception, explicit safeguard derivation, and the
native dual-authority crisis boundary; O'Duffy has a dated bypass and matching
AI expiry. The ten approved C3 event/news packages now have concrete consumers;
the later EV-SRC-055 and EV-SRC-059 conditional C3 promotions add two more
source-derived consumers, and the five cleared FRUS packages EV-SRC-004,
EV-SRC-022, EV-SRC-040, EV-SRC-041, and EV-SRC-058 now consume the four H04
emergency-news nodes and the F15 neutral-markings node. The evidence is in
`audits/ireland_event_source_consumer_repair_2026-08-01.md`. These static
repairs do not close the separate source-clearance and visual-budget blockers.

The 2026-08-01 route-advisor tranche is recorded in
`ireland_route_advisor_package_tranche_2026-08-01.md`. Ireland now has 34
custom advisor blocks: the two earlier paid Lemass/Mulcahy roles, three
source-backed constitutional starting replacements, and 29 route-gated
historical portfolios across Fianna Fáil, Fine Gael and coalition politics,
Labour, Clann, Church/vocational politics, IRA civil and command routes,
Congress, O'Duffy, and Ailtirí. Recruitment is route-scoped; normal hiring
costs, office/date gates, dismissal, and cleanup remain active. The custom
Traynor, Hyde, and O'Kelly tokens replace duplicate vanilla starting tokens.

The user-approved C3 source conditions are recorded in
`docs/plans/ireland_focus_tree/authority_rulings_m2_a2_c3_2026-08-01.md` and
the round-12 handoff at
`assets/source_research_handoffs/user_approved_conditional_round12_2026-08-02.md`.
The current 169-row manifest has 166 `complete` entries, 0
`needs_user_review` entries, and 3 blocked entries. Its clearance breakdown is
135 C3-complete, 0 C2-review, 3 C1-blocked, 0 C2-blocked, and
31 C4-complete entries. The round-12 conditional source rows
(S-06, S-08, S-15, S-20, S-23, S-26, and S-33) are installed under the
standard runtime `gfx/` roots with their alternate-object boundaries intact;
S-06/S-08 placement is recorded in
`assets/source_research_handoffs/runtime_promotion_s06_s08_2026-08-02.md`, and
the full source audit records their runtime DDS hashes and attribution limits.
EV-SRC-041 is the promoted C4 official FRUS 1940
Vol. III Document 161 package; its source and runtime evidence are recorded in
`assets/source_research_handoffs/EV041_FRUS_clearance_2026-08-01.md`.
EV-SRC-055 is the promoted conditional C3 Houses of the Oireachtas
Constitution (Consequential Provisions) Bill package; its source, runtime, and
H01 consumer are recorded in
`assets/source_research_handoffs/EV055_Oireachtas_clearance_2026-08-01.md`.
EV-SRC-059 is the promoted conditional C3 UWM/AGSL Admiralty Chart 1765
package; its source, runtime, and F17 Cork ports consumer are recorded in
`assets/source_research_handoffs/EV059_UKHO_chart_clearance_2026-08-01.md`.
Promoted C3 DDS files are under the standard runtime
`gfx/` roots and all have matching manifest hashes and registered texture
paths. The runtime currently contains 121 final event-picture DDS files: 69
cleared or user-approved conditional event/news manifest packages, the
separately manifested cleared S-03 presidential-seal report crop, and 51
generated images. The canonical 120-image event/news budget is complete; the
remaining source gap is three exact person-labelled portraits. No blocked row
has been replaced by generated, duplicated, or fallback art. The round-12
conditional promotion handoff is
`assets/source_research_handoffs/user_approved_conditional_round12_2026-08-02.md`.
Round 13 also promotes P-50 Michael Price from an exact face-mapped 1921 group
photograph, round 14 promotes P-54 P. J. Coughlan from an exact
caption-mapped 1936 Irish Brigade group photograph, and round 15 promotes P-31
Michael Browne from an exact caption-mapped Commission on Vocational
Organisation photograph. Their source, crop locators, preserved portraits, and
runtime sprites are recorded in
`assets/source_research_handoffs/portrait_exact_object_search_round13_2026-08-02.md`
`assets/source_research_handoffs/portrait_exact_object_search_round14_2026-08-02.md`,
and `assets/source_research_handoffs/portrait_exact_object_search_round15_2026-08-03.md`.
The round-16 rejection handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round16_2026-08-03.md`.
Round 17 rejects the exact-name Third Tipperary Michael Fitzpatrick lead after
the associated BMH witness statement identifies a different 1898-born local
figure; its handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round17_2026-08-03.md`.
Round 18 independently rechecks all four remaining exact-person rows. It finds
no promotable source: the P-15 1977 lead is outside the portrait window, P-26
has no face-mapped or rights-cleared object, P-45 has only unresolved commercial
group-photo leads plus a separate UCD papers catalogue, and P-55 has no NLI
Walsh portrait while the Waterford Poole sitter is a different person. Its
handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round18_2026-08-03.md`.
Round 19 finds a stronger period-fitting P-15 lead in the Catholic Archives:
the 30 April 1940 Irish Mission to London record names Leydon in a delegation
photograph outside the Savoy Hotel. The record credits Keystone Press Agency,
but the accessible catalogue route exposes metadata only and no image-level
reuse permission. The lead remains research-only and does not change the four
blocked rows. Its handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round19_2026-08-03.md`.
Round 20 independently checks a January 1937 ArchivUL photograph of Irish
Brigade officers outside the Cáceres barracks. The item names no Walsh sitter,
exposes no image bytes, and leaves reproduction conditions blank, so its
unrestricted-access statement is not a reuse grant. P-55 remains C1 blocked;
the handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round20_2026-08-03.md`.
Round 21 checks a second exact-period ArchivUL officer-corps photograph from
May 1937. Its reverse note identifies O'Duffy seated in the centre, but the
item names no Walsh sitter, exposes no image bytes, and leaves reproduction
conditions blank. It does not change the four blocked rows; its handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round21_2026-08-03.md`.
Round 22 rechecks all four remaining rows and adds a stronger P-45 identity
lead: searchable illustration captions in Brian Hanley's copyrighted *The IRA,
1926–1936* place Mick Fitzpatrick in an April 1932 Glasnevin group photograph.
Google Books is not browsable, the Internet Archive scan is restricted, and no
image bytes or image-level reuse permission are available. P-26 remains an
unmapped History Ireland group photograph, P-15 remains a metadata-only
Catholic Archives/Keystone lead, and P-55 remains an unmapped ArchivUL/NLI
record. No portrait row or runtime consumer changed; the handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round22_2026-08-03.md`.
Leader source packages remain preserved under `docs/portraits`.

Round 24 promotes P-15 John Leydon from the exact 30 April 1940 Catholic
Archives “Irish Mission to London” object. The archive caption maps Leydon as
the leftmost sitter, and the source master, crop, preserved source, runtime
DDS, and conditional local-mod boundary are recorded in
`assets/source_research_handoffs/portrait_exact_object_search_round24_2026-08-03.md`.
P-26 Patrick Cogan, P-45 Mick Fitzpatrick, and P-55 Liam D. Walsh remain the
three exact-person source blockers.

Round 25 rechecks P-26 Patrick Cogan against the direct image object used by
the *History Ireland* Clann na Talmhan article. The Athenry group photograph
does not map Cogan's face and exposes no image-level licence or original
holding record, so it remains research-only. No crop, processed PNG, source
preservation file, DDS, or runtime registration was created. The handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round25_2026-08-03.md`.

Round 26 rechecks the remaining P-45 Mick Fitzpatrick and P-55 Liam D. Walsh
rows. The FMA wedding catalogue and Hanley caption trail provide identity or
context only for Fitzpatrick, without reusable plate bytes or image-level
permission. The NLI and ArchivUL Walsh records likewise provide finding aids,
letters, or unmapped group photographs, not an exact portrait object. The
Waterford Poole Liam Walsh image remains a confirmed wrong-person lead. Both
rows remain C1/blocked, with no crop, processed PNG, DDS, runtime registration,
or new `docs/portraits` file. The dated handoffs are
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
and P-45 Mick Fitzpatrick; both return the generic 80x80 `Avatar` SVG rather
than person-specific source portraits. Its new History Ireland Blueshirt image
lead for P-55 Liam D. Walsh is a group rally scene with O'Duffy identified and
no face-level Walsh mapping. All three objects remain C1/blocked research
evidence only; no derivative, runtime registration, or new `docs/portraits`
file was created. The dated handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round28_2026-08-03.md`.

Round 29 rechecks P-26 and P-45 through the Carlow bibliography, official
Oireachtas identity records, NLI catalogue leads, and the Brian Hanley/Maurice
Twomey caption trail. No exact original image bytes with person-level mapping
and a defensible local-mod reuse boundary were found. No portrait source,
derivative, runtime DDS, GFX registration, or new `docs/portraits` file was
created; P-26, P-45, and P-55 remain the three blocked canonical rows. The
handoff is
`assets/source_research_handoffs/portrait_exact_object_search_round29_p26_p45_2026-08-03.md`.

Rounds 30 and 31 add the final bounded P-55, P-26, and P-45 checks; the
official MSPC records for Fitzpatrick provide identity evidence but no portrait
object, and no new source, derivative, runtime DDS, GFX registration, or
portrait subfolder was created. Their handoffs are
`assets/source_research_handoffs/portrait_exact_object_search_round30_p55_2026-08-03.md`,
`assets/source_research_handoffs/portrait_exact_object_search_round31_p26_2026-08-03.md`,
and
`assets/source_research_handoffs/portrait_exact_object_search_round31_p45_2026-08-03.md`.

The round-10 bounded source-clearance pass rechecked all 37 remaining rows
without promoting any C1/C2 material at that time. It found an exact dated 12
October 1944
Catholic Archives Ailtirí flier lead for S-18, but the record does not grant
reproduction or digital-object rights, so S-18 was then C2 blocked. The
subsequent round-12 project-owner instruction conditionally promoted the 32
rows with exact source bytes and reviewed crops; S-18 and the other six symbol
rows are now complete C3 packages. The current evidence is
`assets/source_research_handoffs/user_approved_conditional_round12_2026-08-02.md`.

The round-11 public-domain check repeated exact-name Commons, library, archive,
and official-source searches for the remaining portrait and historical-object
rows. It found no new exact image-level reuse grant before the project-owner
instruction. Round 13 clears P-50 from the exact mapped Tom Barry wedding
photograph, round 14 clears P-54 from the exact caption-mapped Irish Brigade
group photograph, and round 15 clears P-31 from the exact caption-mapped
Commission on Vocational Organisation photograph; rounds 16 and 17 document
rejected identity-conflict leads, leaving the same four person-labelled
portrait gaps. The current evidence is
`assets/source_research_handoffs/public_domain_check_round11_2026-08-02.md`.

The 2026-08-01 review-row audit is recorded in
`audits/ireland_review_row_route_portrait_reaudit_2026-08-01.md`. S-24 and S-27
are now complete C3 conditional packages under the explicit user approval
handoff; Daniel Morrissey's separate route extension is complete under
conditional C3 local-mod scope; EV-SRC-055, EV-SRC-059, and EV-SRC-041 are
complete under their dated source clearance handoffs. Father Edward Cahill
remains blocked without an exact
portrait. No substitute or fallback was introduced.

The matching static MCP re-audit is
`audits/ireland_mcp_static_reaudit_2026-08-02.md`: current focus, event, and
GUI surfaces were inspected read-only, and the global or intentional
shared-texture diagnostics are classified there rather than silently counted
as Ireland-local failures. The preceding 2026-08-01 record remains historical
evidence for the same boundary.
The EV-SRC-055 follow-up source/GFX/event check is recorded in
`audits/ireland_ev055_static_reaudit_2026-08-01.md`; its bounded MCP event lint
returned zero blocking diagnostics.
The EV-SRC-059 follow-up source/GFX/event check is recorded in
`audits/ireland_ev059_static_reaudit_2026-08-01.md`; its post-wiring bounded
MCP event lint returned `status: ok` with zero blocking diagnostics. The
workspace-wide helper/lifecycle projection remains deferred by the MCP
large-workspace limit and is not an Ireland-local blocker.

Live HOI4 launch, in-game testing, fresh saves, and scenario playthroughs are
excluded from the completion gate by explicit user direction. Static audits,
local engine-reference checks, canonical source reconciliation, asset
clearance, and non-live audit evidence remain required until the final audit
reports no blocker.

The 2026-08-02 decision-cost contract repair is complete: all 140 custom-cost
actions omit regular cost fields, manually deduct their fixed base Political
Power in complete_effect, retain the named-ledger surcharge branches, expose
action-specific dynamic cost localisation, and provide worst-case
ai_hint_pp_cost values. The focused static audit reports 140/140 hints,
deductions, and cost keys with zero regular cost lines.

The 2026-08-02 AI route-selection repair is recorded in
`audits/ireland_ai_route_selection_repair_2026-08-02.md`. Historical AI remains
fixed to de Valera; non-historical AI now receives a permission-aware,
pre-commit opening intent for the radical, serious-culture, High King, Five
Provinces, Otherworld, and Ailtirí families. Existing route plans consume the
intent only through generic profile flags and still require every authored
focus, date, evidence, material, hidden-permission, and mutual-exclusion gate.
No route flag or political/material grant is written by the selector.

The 2026-08-02 H/P/A boundary repair keeps the uncommitted serious-cultural
and archive lane in `H`; the Otherworld AI opening is also `H`. After the
Otherworld investigation focus commits the route, archive work, investigation,
and pre-verification containment are `P`. `A` begins only when
`ireland_events.437` resolves the canonical archive reveal and its
four-choice outcome writes the durable route-specific impossible-result and
archive-reveal flags; final convergence remains `A`. The historical flavour dispatcher is
suppressed only by the `A` route flag. The exact three persistent spirit
families remain unchanged. The Dillon strict named-vote helper is retained at
`common/scripted_triggers/ireland_dillon_gate_repair.txt` and is used by
both named-vote entry points.

The same 2026-08-02 tranche adds the canonical Otherworld boundary event
`ireland_events.437`, `The Archive Records What Has Not Yet Happened`.
Its admission requires the independent witness ledger, unusual campaign
condition, Hidden Evidence Council completion, and concealed-transition
authority; its four options record contact/compact, containment, exploitation,
or human-restoration outcomes with live settlement, consent, public-knowledge,
neutrality, and exposure consequences. The rejection choice opens the shared
`Recovery Bridge` and `Restore Constitutional Calendar` sequence; its
transient review flags are cleaned on route closure and its completion record
is durable, while the impossible event keeps the route in A. The event owns
the route-specific Otherworld writers for
`ireland_otherworld_archive_reveal_complete` and
`ireland_otherworld_impossible_confirmed`; the shared
`ireland_verified_impossible_reveal` flag remains reserved for the other
hidden families and final convergence. Compact, containment, and dominion
focuses require the route-specific reveal. Targeted offline MCP event lint/render
returned zero blocking diagnostics, while the large workspace’s focused scan
and unavailable full-graph compare remain documented as tooling limits.

The 2026-08-01 mission-capacity transition audit is recorded in
`mission_capacity_transition_and_activation_refresh_tranche_2026-08-01.md`.
The runtime ladder is 8 active missions in ordinary peace, 10 during war or a
national emergency, and 12 only when both the emergency and Northern
occupation conditions are present; returning from the 12-slot state steps down
to 10 immediately and to 8 after 30 stable days. All 54 mission families retain
named objectives, deadlines, full/partial/failure/escalation/cancellation
paths, AI utility, and route cleanup. The bounded static event/mission/GUI/
achievement cross-check is recorded in
`audits/ireland_static_source_reaudit_2026-08-01.md`.

Latest route-conclusion and achievement-gate repair (2026-07-28): route-specific
`*_concluded` flags now wait for the shared 180-day full/partial review instead
of being written by capstones. Conclusion achievement writers require the full
review result. A-20 uses the four durable source-leverage maxima, A-21 checks
live emergency recovery state without rejecting its own recovery history, and
A-26 counts only the four named sovereign diplomatic channels with non-subject
partner gates. Static source checks are recorded in
`docs/plans/ireland_focus_tree/route_conclusion_and_achievement_gate_repair_2026-07-28.md`;
HOI4 was not launched and live route/achievement scenarios remain open.

Completion authority note (user direction, 2026-07-28): live in-game testing,
fresh saves, and live scenario playthroughs are intentionally excluded from the
completion gate. They may remain recorded as unrun evidence, but they do not
block this goal. Local static engine-reference checks, canonical design
decisions, source clearance, worktree integration, and non-live audits remain
completion requirements.

## Superseded historical snapshots

The dated records below preserve earlier evidence for traceability. The
2026-08-01 authority snapshot at the top of this file is the current source for
M2, A2, C3, manifest status, and runtime placement. Older counts or pending
authority language below must not reopen those settled decisions.

Round-seven source reconciliation (2026-07-29): the historical 169-row
manifest is currently 48 complete, 64 `needs_user_review`, and 57 blocked.
Family status is portraits 11/34/15, symbols 8/17/15, and event/news 29/13/27
(complete/review/blocked). Clearance-state totals are C1 35, C2 26, C3 82,
and C4 26. The manifest tier distribution is T1 45, T2 18, T3 27, T4 19,
T5 8, T6 9, T7 25, T8 9, T9 7, T10 0, and T11 2. The twenty-three
round-3 review candidates remain review-only and are not promoted to runtime. Ten
exact NLI/UCD leads advanced from C1 to C2 while staying blocked. Current
event-source consumption maps EV-SRC-003 to .109, EV-SRC-021 to .110,
EV-SRC-039 to .111, and EV-SRC-057 to .254. Runtime consumed budget assets are
80/80 complete, while the overall 120-image budget is 80/120 complete. Exactly
three GUI windows inspect as 58/40/57 elements, with reported visible overlap
counts of 10/9/29. The 2026-08-03 re-audit classifies the animation/fallback,
status, dossier, and state-row layers as intentional. Local validation remains `false` because the source
graph also treats canonical action-texture reuse and offline renderer
limitations as blocking diagnostics. The runtime
inventory is 857 DDS files total, 856 Ireland-owned; the Ireland GFX audit
records 1,085 texture references and 325 unique sprite names. FG-001 through
FG-007 are all implemented.

This is the settled machine-manifest baseline after the round-3A and round-3B
source packages were reconciled.

The same audit found seven live review-gated portrait references still wired in
current route-character/GFX sources: P-05, P-06, P-27, P-43, P-46, P-56, and
RC-PORTRAIT-01 Daniel Morrissey. Current source evidence does not prove a fix,
so this remains unresolved. The NR07 early-admission defect is fixed: all four
NR07 event blocks and their four dispatcher limits directly require
`ireland_northern_core_review_open`, whose sole writer requires final
review proof, integration stage five, control of state 119, and clean
occupation/settlement state.

The v12 goal-icon package and v1 law-state package are the current runtime
asset packages. v11, v10, v9, v8, v7, v5, v4, and older static notes are
historical review evidence only.

Latest focus-AI reconciliation (2026-07-28): the historical “no focus AI”
finding is superseded by the current source. Ireland has 216 authored focus
blocks, 31 `IRE_ireland_*` focus plans with no unresolved focus references, route
plan coverage for all 17 visible gateways, and exactly 40 strategy blocks
(30 durable profiles plus 10 temporary overlays). Ordinary route priority is
kept in vanilla-style `focus_factors` plans; only the concealed Ailtirí
gateway needs a node-level `ai_will_do` permission guard. This is static source
evidence only; live focus selection, probability balance, MCP engine loading,
and required scenarios remain open. See
`docs/plans/ireland_focus_tree/focus_ai_reconciliation_2026-07-28.md`.

Latest focus-layout inspection (2026-07-28): the final offline MCP inspection
resolved all 216 Ireland focus titles with 197 connectors, zero Ireland-local
crossings, zero node intersections, zero long connectors, and zero
Ireland-tree diagnostics. The matching render is recorded in
`docs/plans/ireland_focus_tree/focus_layout_inspection_2026-07-28.md`. The
global MCP response still reports fourteen unrelated vanilla continuous-focus
diagnostics, so this is authored-tree evidence rather than a global validation
pass; engine loading and live scenarios remain open.

Latest event source state (2026-08-01 reconciliation): the four
`events/ireland*.txt` sources contain 495 unique event IDs, including the
exact 236-event flavour floor. The engine-reference reaudit records the clean
namespace-filtered baseline and the zero-helper catalogue
limitation; the later Frank Ryan handoff adds three P11 nodes with shared
scripted-trigger definitions and complete localisation. This closes the local
event helper-reference gate without a live-engine claim. Evidence:
`docs/plans/ireland_focus_tree/audits/ireland_event_engine_reference_reaudit_2026-07-29.md`
and `docs/plans/ireland_focus_tree/ireland_frank_ryan_return_lifecycle_2026-07-29.md`.

Current GUI engine-reference re-audit (2026-08-03): the three exact windows
inspect as 58/40/57 elements with reported visible overlap counts of 10/9/29.
The current disposition classifies the animation/fallback, mutually exclusive
status, dossier title/state, and A-22/A-27/A-28 row layers as intentional. All three windows rerendered
at 1920x1080 and 1280x720 in normal, warning, locked, and long-text states with
`GUI_RENDERED` and no blocker. The aggregate local result remains `false`
because the source graph also reports the canonical 140-sprite/70-texture reuse
contract, offline font limitations, static-fallback inference, and unsupported
render fields. See
`docs/plans/ireland_focus_tree/audits/ireland_gui_surface_reaudit_2026-07-29.md`.

Latest goal-icon regeneration (2026-07-28): the user-rejected v7 goal package
was replaced by fourteen newly generated 4×4 source atlases with all 216
subjects regenerated from fresh built-in image-generation sources in
`assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v12/`.
The v12 package contains 216 fresh source rows, transparent alpha previews, 216
optically centered 100×88 processed PNGs, and 216 DDS files. Its strict audit
reports zero missing or unexpected rows, duplicate hashes, opaque corners,
empty icons, off-center icons, edge contact, DDS readback failures, or source
or processed hash overlap with v7. The exact 216 audited DDS files are
promoted in `gfx/interface/goals/ireland/`, with stable registrations
unchanged in `interface/ireland_icons.gfx`. The generation brief uses
restrained vanilla HOI4 focus-emblem language: one large readable painted
object or compact scene per icon, dark contour, matte shading, controlled
period palette, and route-specific symbols; it prohibits readable text,
portraits, UI boxes, square tiles, glossy rendering, and a full-field green
matte. The v12 manifest and contact sheet, plus the runtime handoff and
all-icon audit, are retained beside the fresh sources. This is asset/source
evidence only; live engine loading and focus readability remain open.

Latest all-icon/law regeneration audit (2026-07-28): the full Ireland icon
surface review found no alignment, edge-bleed, opaque-corner, or visible
chroma-key defect in the categories, actions, missions, spirits, mechanic
ledger, temporary overlays, route emblems, sourced symbols, achievement
variants, or animation fallbacks when judged against each asset type's
intended framing. The one concrete defect was inconsistent horizontal
placement in the old law family. Seventeen fresh law triptychs were generated
and cropped into the 51 canonical entry/reviewed/failure rows, then normalized
around a shared visible center of (29.5, 33.5) in the 60x68 canvas, with no
more than 0.5 pixels of raster-quantization drift. The v1 package
has 51/51 matching processed and DDS rows, with no edge contact, opaque
corners, fuchsia or greenscreen pixels, or center outliers beyond that
half-pixel allowance. Runtime files are
under `gfx/interface/ideas/ireland/laws/`; the complete visual record is
`docs/plans/ireland_focus_tree/assets/icon_surface_audit_2026-07-28.md`.
Live in-game testing is intentionally outside this asset completion pass.

Latest focus-raster inspection (2026-07-28): the offline national-focus raster
loaded all 216 Ireland goal references from `gfx/interface/goals/ireland/`
with zero Ireland-local missing-icon or texture-path diagnostics. The 9046x1009
review raster and the fourteen unrelated vanilla continuous-focus diagnostics
are recorded in `docs/plans/ireland_focus_tree/focus_raster_goal_icon_inspection_2026-07-28.md`;
this remains authored-tree evidence, not live engine proof.

Latest decision/mission lifecycle and cost tranche (2026-07-28): all 54
canonical objective missions now use automatic completion semantics. All 140
actions now display the named ledger that actually drives their dynamic
Political Power, Command Power, and burden surcharge, and all 140 requirement
tooltips no longer show the unrelated global maximum preview. A-22 now checks
current German leverage rather than the historical high-water variable. The
member-contribution class design is now implemented as a five-way paid
troops/ships/finance/intelligence/infrastructure selection with class-specific
mission evaluation and cleanup. M2 closes the former Radical/Underground
two-slot wording question: the exact 54-family inventory uses the two freed
ordinals 006 and 009 for physically nested Radical/Underground mission
families. Source clearance and live scenarios remain open; the local GUI
engine-reference classification is recorded in
`audits/ireland_gui_texture_reuse_engine_reference_2026-08-02.md`. Evidence:
`docs/plans/ireland_focus_tree/decision_mission_lifecycle_cost_tranche_2026-07-28.md`;
`docs/plans/ireland_focus_tree/member_contribution_choice_tranche_2026-07-28.md`.

Latest radical-action gate and mission-deadline repair (2026-07-28): the ten
Radical and Underground actions now use their existing IRA, Congress, O'Duffy,
Ailtirí, and failure/recovery readiness flags instead of the broad shared
transition gate. All 54 mission descriptions now state the exact day value
used by their `days_mission_timeout` blocks. The M2 authority ruling assigns
the two replacement mission families to ordinals 006 and 009 under the
Radical/Underground categories; the total remains exactly 54.
Evidence: `docs/plans/ireland_focus_tree/radical_action_gate_and_mission_deadline_repair_2026-07-28.md`.

Detailed current asset evidence: `docs/plans/ireland_focus_tree/assets/icon_surface_audit_2026-07-28.md`.

Latest High Kingship branch-lifecycle tranche (2026-07-27): the existing High Kingship focus surfaces now distinguish lawful household, sacral-crown, and captured-crown states. The captured-crown outcome is a source-specific failure with consent/exposure/settlement shocks, a foreign-reaction handoff, and an authored recovery bridge; the charter, capstone, AI, and achievement-history surfaces consume the branch markers. This preserves the exact 216-focus and 216-goal-icon budgets. Evidence: `docs/plans/ireland_focus_tree/high_kingship_branch_lifecycle_tranche_2026-07-27.md`. This is source-level evidence only; live event timing, hidden visibility, AI, engine-reference, source-clearance, and scenario proof remain open.

Historical asset-budget runtime audit (2026-07-27, refreshed 2026-07-29): this record preserves the earlier v12 goal/law package and 80/120 budget snapshot. It is superseded by the 2026-08-02 fresh goal/law/spirit package audit, the current 165/0/4 source manifest, and the current 120/120 event-picture inventory at the top of this file.

Historical sourced-portrait preservation (2026-08-01): the 38 canonical manifest-backed portrait packages with local source images, plus the review-gated Daniel Morrissey route extension, were preserved under `docs/portraits/source_originals/` and `docs/portraits/processed_png/`. The recovered P-37 Seán Russell, P-59 J. J. Walsh, and P-60 Oliver J. Flanagan originals were preserved under `docs/portraits/research_2026-07-29/blocked_queue/`. The round-12 conditional promotion supersedes this count; its ten exact portrait originals are preserved under the dated `docs/portraits/research_2026-08-02/user_approved_conditional/source_originals/` package. Evidence: `docs/portraits/README.md`, `docs/plans/ireland_focus_tree/assets/source_manifest.json`, and `docs/plans/ireland_focus_tree/assets/source_research_handoffs/user_approved_conditional_round12_2026-08-02.md`.

Round-six portrait preservation adds the exact 1934 Library of Congress Seán
Murray page and metadata plus two direct Military Archives Harry White objects.
The archive now contains 208 files. P-51 is conditional C3 review, not a
runtime promotion; P-41 remains blocked C2.

Historical source-clearance re-audit (2026-07-29): this record preserves the earlier 48/64/57 manifest snapshot and is superseded by the 2026-08-02 165/0/4 authority snapshot. Current event consumers, source rows, and runtime placement are recorded at the top of this file and in `source_of_truth_map.md`.

Latest mission-presentation and runtime-clearance repair (2026-07-29): all 54
non-selectable objective missions now use `is_good = no`, so the engine labels
their `available`/`complete_effect` path as success and their timeout path as
failure. Twenty-two unconsumed C3 review portraits were removed from runtime
registration and `gfx/leaders/ireland/`; their exact source bytes remain under
`docs/portraits/` and their review derivatives remain in temporary staging.
The seven consumed review-gated portraits remain unresolved. Evidence:
`docs/plans/ireland_focus_tree/mission_polarity_and_review_portrait_runtime_repair_2026-07-29.md`.

Latest focus-localisation route-voice tranche (2026-07-26): the 216 focus descriptions were manually rewritten into route-specific prose covering the shared opening, constitutional and named-leader routes, serious culture, Provision, Readiness, neutrality, Northern policy, radical transitions, clerical and producer states, Ailtirí, High Kingship, Five Provinces, Otherworld, and convergence. The targeted sweep finds zero remaining route-wide generic focus-description templates. Evidence: `docs/plans/ireland_focus_tree/focus_localisation_route_voice_tranche_2026-07-26.md`. This improves player-facing text only; parser, focus-render, source-clearance, hidden-achievement, and runtime scenario gates remain open.

Latest decision-category archive cleanup (2026-07-26): all thirteen category headers now hide on `ireland_route_archived`, matching the 140 action-level archive gates and preventing empty post-transition panels. Evidence: `docs/plans/ireland_focus_tree/subagent_handoffs/decision_category_route_archive_cleanup_2026-07-26.md`. The M2 authority ruling subsequently closed the Radical/Underground wording issue by physically nesting the ordinal 006 and 009 replacement mission families while preserving the exact 54-row inventory.

Latest regional-defence component-gate tranche (2026-07-26): `Propose a Regional Defence League` now requires the canonical aggregate Readiness `75` and Provision `65` floors plus Warning, Maritime Protection, Command, and Intelligence each at least `45`, alongside its existing charter, member, safeguards, named-force, common-threat, capacity, and dynamic-cost gates. Evidence: `docs/plans/ireland_focus_tree/regional_defence_league_component_gate_tranche_2026-07-26.md`. This closes one source-level operational component gate only; the full action/material map, source clearance, live engine/reference checks, AI behavior, GUI rendering, and required scenarios remain open.

Latest Atlantic-route threshold reconciliation tranche (2026-07-26): the durable Atlantic route writer no longer records formation at the obsolete Provision/Readiness `35/35` point. It now requires the authored charter and proposal, valid partners, a full contribution schedule, a common threat, Provision `65`, Readiness `75`, Maritime Access and Transport Serviceability `50`, and Warning/Maritime Protection/Command/Intelligence `45` floors. Evidence: `docs/plans/ireland_focus_tree/atlantic_route_threshold_reconciliation_tranche_2026-07-26.md`. This closes one route-writer threshold mismatch only; British/American settlement proof, source clearance, live engine/reference checks, AI behavior, GUI rendering, and required scenarios remain open.

Latest action-material gate reconciliation tranche (2026-07-26): `Expand Folklore Collection`, `Negotiate British Flexibility`, and `Merge Tax and Debt Administration` now enforce the manpower/truck/convoy commitments they already charge, with dedicated tax/debt convoy macros and synchronized requirement text. A static sweep finds no completion-time physical charge without a matching same-action stockpile or capacity gate. Evidence: `docs/plans/ireland_focus_tree/action_material_gate_reconciliation_tranche_2026-07-26.md`. This closes three admission rows only; the full per-ID material/safeguard map, source clearance, live engine/reference checks, AI behavior, and required scenarios remain open.

Latest concealed-transition authority tranche (2026-07-26): `Convene a Hidden Evidence Council` now requires the completed restoration review, independent evidence, hidden-content permission and game rule, and a clean failure/closure state; completion reveals the concealed transition without adding evidence. High Kingship, Five Provinces impossibility, Otherworld dominion/impossible confirmation, and the derived impossible reveal additionally require the durable council authorization, while the constitutional and federal P-route gates remain separate. Evidence: `docs/plans/ireland_focus_tree/concealed_transition_authority_tranche_2026-07-26.md`; helper contract is in `docs/ireland_dynamic_effects.md`. This closes one source-level concealed-route authorization gap only; source clearance, live engine/reference checks, AI behavior, GUI/focus rendering, and required scenarios remain open.

Latest restoration-outcome lifecycle tranche (2026-07-26): restoration mission timeout now records false-lead, fraud/disqualification, public-panic, or route-closure classifications from the live evidence, disqualifier, and public-knowledge state; panic containment and failed-restoration archiving consume those classifications and clear the transient flags while retaining durable mission history. Evidence: `common/script_constants/ireland_constants.txt`, `common/decisions/ireland_decisions.txt`, `localisation/english/ireland_l_english.yml`, and `docs/plans/ireland_focus_tree/restoration_evidence_independent_review_tranche_2026-07-26.md`. This closes the source-wired restoration outcome-classification/cleanup gap only; live outcomes, hidden reveal, source clearance, engine/reference checks, AI behavior, and required scenarios remain open.

Latest foreign-channel burden tranche (2026-07-26): Plan W, diaspora relief, the German emissary, Vatican mediation, and neutral consultation now record the external-exposure burdens named by their channel work; source-specific American/Vatican leverage is explicit while the neutral forum remains exposure-only. Evidence: `docs/plans/ireland_focus_tree/foreign_channel_burden_tranche_2026-07-26.md`. This closes five source-level burden rows only; partner invalidation, reaction ordering, mission outcomes, source clearance, engine/reference checks, AI behavior, and required scenarios remain open.

Latest restoration-evidence independent-review tranche (2026-07-26): `Test a Restoration Claim` and `Verify the Restoration Evidence` now require a named authority combining archive provenance, independent Cultural Service/Diaspora review, historic-site custody, royal evidence thresholds `4/3/3`, an unusual campaign condition, and no evidence disqualifier. The Leinster map objective also rechecks the active action and mission, full control, industry, and naval-base platform. Evidence: `docs/plans/ireland_focus_tree/restoration_evidence_independent_review_tranche_2026-07-26.md`; helper contract is in `docs/ireland_dynamic_effects.md`. This closes one source-level restoration admission/objective gap only; mission outcomes, hidden-route reveal, source clearance, live engine/reference checks, AI behavior, and required scenarios remain open.

Latest cultural congress regional-rights tranche (2026-07-26): `Hold a Provincial Cultural Congress` now requires regional participation plus a rights-bearing constituency through Minority Confidence, Labour Organisation, or Church influence; its mission map objective rechecks those values, the active action and mission, the three authored state/building platforms, and the multi-region evidence count. Evidence: `docs/plans/ireland_focus_tree/cultural_congress_regional_rights_tranche_2026-07-26.md`; trigger contract is in `docs/ireland_dynamic_effects.md`. This closes one source-level cultural mission gap only; restoration evidence, the broader material/safeguard map, source clearance, live engine/reference checks, AI behavior, and required scenarios remain open.

Latest folklore collection objective/material tranche (2026-07-26): `Expand Folklore Collection` now requires the serious-culture/archive lane, school or language-service network, archival groundwork, historic-site custody, Connacht control, 250 manpower, and 5 Trucks; its dated mission map objective rechecks those institutional proofs and records only capped cancellation recovery. Evidence: `docs/plans/ireland_focus_tree/folklore_collection_objective_and_material_tranche_2026-07-26.md`; trigger contract is in `docs/ireland_dynamic_effects.md`. This closes one source-level cultural action/objective gap only; the other cultural missions, broader material/safeguard map, source clearance, live engine/reference checks, AI behavior, and required scenarios remain open.

Latest Treaty Port and neutral-approaches objective tranche (2026-07-26): `Defend A Treaty Port` now requires a live harbour-defence action and mission, Munster port platform, Treaty Port/port-defence project, connected warning service, and command/warning readiness; `Patrol The Neutral Approaches` now requires its live action and mission, Munster/Leinster port platforms, a named Irish or chartered shipping route, warning/rescue authority, Neutrality Integrity, and maritime-protection readiness. Evidence: `docs/plans/ireland_focus_tree/treaty_port_neutral_approaches_objective_tranche_2026-07-26.md`; reusable proof contracts are in `docs/ireland_dynamic_effects.md`. This closes two source-level map-objective gaps only; the broader 140-action material/safeguard map, source clearance, live engine/reference checks, AI behavior, and required scenarios remain open.

Latest foreign-procurement authority tranche (2026-07-26): British supply now requires a named Provision shortage, finance/rural-credit support, and sovereignty/access safeguards; American procurement requires an external-creditor route plus finance/manufacturing and legal authority; German delivery proof requires a prior emissary promise and independence safeguards; Vatican mediation requires a named war, incident, Church-network, diaspora, or postwar-isolation cause. The same proofs apply to the foreign source selector and are rechecked by all four delivery objectives; Vatican records its humanitarian case separately from mission success. Evidence: `docs/plans/ireland_focus_tree/foreign_procurement_authority_tranche_2026-07-26.md`; helper contracts are in `docs/ireland_dynamic_effects.md`. This closes four source-level foreign admission/objective gaps only; Treaty Port/neutral approaches, the broader 140-action material/safeguard map, source clearance, live engine/reference checks, AI behavior, and required scenarios remain open.

Latest readiness objective-truth tranche (2026-07-26): the four readiness rows for `Protect an Operational Plan`, `Demobilise a Force Tier`, `Secure the Dublin-To-Belfast Corridor`, and `Take and Hold Belfast` now require authored plan/authority records, real deployed formations, the Strategic Depot, command or supply floors, rail and civilian-passage records, and the Northern Security Stability floor where applicable. The demobilisation mission also records preserved-cadre, archived-record, partial-demobilisation, and veteran-settlement-pending outcomes without conflating readiness release with postwar settlement. Evidence: `docs/plans/ireland_focus_tree/readiness_objective_truth_tranche_2026-07-26.md`; reusable proof contracts are in `docs/ireland_dynamic_effects.md`. This closes four source-level objective/admission gaps only; source clearance, foreign and neutral depth, the broader action safeguard map, live engine/reference checks, AI behavior, and required scenarios remain open.

Latest foreign-guarantee active-law tranche (2026-07-26): `Review Foreign Guarantees` now requires the live `ireland_law_guarantee_active` law state in addition to its existing Northern occupation/integration review, Dublin-to-Belfast scope, Northern flexibility, and valid British-partner gates. Evidence: `docs/plans/ireland_focus_tree/foreign_guarantee_active_law_gate_tranche_2026-07-26.md`. This closes one canonical admission row only; live law transition, partner invalidation, reaction, AI, engine-reference, mission, and cleanup scenarios remain not-run.

Latest mission-description review (2026-07-26): all 54 canonical mission descriptions now use distinct route-specific prose with concrete objectives, named places or institutions where applicable, explicit durations, and separate full, partial, and failure outcomes. The corresponding source blocks retain named map-objective gates, escalation telemetry, and cleanup handling. Evidence: `docs/plans/ireland_focus_tree/mission_description_objective_review_tranche_2026-07-26.md`. This closes the mission-prose review finding only; source clearance, the 140-row action/material safeguard mapping, engine-reference checks, live scenarios, and worktree integration remain open.

Latest action-safeguard admission tranche (2026-07-26): `Share a Controlled Weather Report`, `Release or Exchange Internees`, and `Merge Tax and Debt Administration` now require the concrete weather/cooperation, diplomatic-channel, and external-creditor proofs named by their canonical cost rows. Evidence: `docs/plans/ireland_focus_tree/action_safeguard_admission_tranche_2026-07-26.md`; shared trigger contracts are documented in `docs/ireland_dynamic_effects.md`. This closes three per-ID admission rows only; the broader 140-row mapping, source clearance, engine-reference checks, live scenarios, and worktree integration remain open.

Latest veteran-settlement and UN-authority tranche (2026-07-26): `Demobilise and Settle Veterans` now requires Administrative Reach 60, Labour Organisation 35, a named housing/reconstruction/veteran-employer capacity, two available civilian factories, 100 Infantry Equipment, and 1,000 manpower; it reserves two civilian factories for 300 days and returns only the capped recoverable share on cancellation. This brings the current named native factory-reservation total to eight projects / thirteen reservations. `Apply for United Nations Membership` and its admission map objective now require a completed postwar foreign review, a resolved FR11 admission position or closed H17 United Nations chain, and Diplomatic Recognition 50. Evidence: `docs/plans/ireland_focus_tree/veteran_settlement_un_authority_tranche_2026-07-26.md`; trigger contracts are documented in `docs/ireland_dynamic_effects.md`. This closes two source-level admission gaps only; live mission, foreign-reaction, AI, engine-reference, and cleanup scenarios remain not-run.
Latest action-resource safeguard tranche (2026-07-26): the four existing logistics pairs now use twelve shared trigger contracts for admission, AI safety, mission availability, live full/partial evaluation, and map-objective projection. Rail requires states 113/135, endpoint infrastructure, 5 Trains, 250 manpower, 200 Fuel, one factory for 180 days, and returns 3/175/140 capped cancellation materials; cargo requires the state-135 port, route, railway, tiered naval capacity, and 5/2/200 materials; command requires the state-113 arms/infrastructure platform, Supply 20, one division for admission and two for full success; Belfast requires state-119 platform, Labour 30/45 and Industrial Capacity 40/55 bands, and two factories for 300 days. The named native reservation total is now nine projects / fifteen reservations. Evidence: `docs/plans/ireland_focus_tree/action_resource_safeguard_implementation_tranche_2026-07-26.md`; live engine parsing, AI behavior, mission ticking, and scenario cleanup remain not-run.

Latest historic-site and patrol-craft tranche (2026-07-26): `Protect a Historic Site` now requires regional participation, Social Consent 35, one rights-bearing local constituency, full control of state 135, 250 manpower, 5 Trucks, and a 10 Support Equipment maintenance-kit charge, and rechecks the admission contract before recording its direct Cultural Capacity result. `Organise Marine Patrols` binds an action-specific coastal patrol-craft coverage flag to its 3-Convoy charge; `Patrol the Neutral Approaches` rechecks that flag alongside port, repair, shipping, warning/rescue, and readiness proofs and releases it on every terminal path. Evidence: `docs/plans/ireland_focus_tree/historic_site_patrol_craft_implementation_tranche_2026-07-26.md`; live engine parsing, craft collision, AI behavior, mission ticking, and scenario cleanup remain not-run.

Latest bounded safeguard and clearance audit (2026-07-26): the current source reconciles the concealed-transition authority, historic-site and patrol-craft safeguards, Northern core writer, and authoritative asset ledger without promoting C1/C2 records or substituting generated historical material. Evidence: `docs/plans/ireland_focus_tree/safeguard_and_clearance_audit_2026-07-26.md`. This is an evidence reconciliation only; source clearance, the full canonical per-ID audit, live engine/reference checks, and required scenarios remain open.

Latest foreign-leverage safeguard tranche (2026-07-26): `Open a G2 Liaison Channel` now records 5 Foreign Exposure and a 3-point increase to the single priority sponsor channel that carries the liaison, while Northern-plan use carries exposure without inventing sponsor leverage. `Review Commonwealth Relations` now requires Finance Safeguards, Rural Credit, or Access Safeguards in addition to its constitutional transition and British-partner gates. Evidence: `docs/plans/ireland_focus_tree/foreign_leverage_safeguard_tranche_2026-07-26.md`. This is source-level burden wiring; live partner, reaction, AI, engine-reference, and cleanup scenarios remain not-run.

Latest neutrality foreign-leverage burden tranche (2026-07-26): `Release or Exchange Internees`, `Share a Controlled Weather Report`, `Answer a Foreign Access Request`, and `Recognise a Liberated Authority` now record 5 Foreign Exposure and 3 leverage to one currently valid named channel, with neutral-states or local-authority use remaining exposure-only. `Negotiate British Flexibility` records 3 Foreign Exposure and 4 British Leverage beside its +5 British Flexibility result. Evidence: `docs/plans/ireland_focus_tree/neutrality_foreign_leverage_burden_tranche_2026-07-26.md`; reusable effect contract in `docs/ireland_dynamic_effects.md`. Live multi-channel priority, partner invalidation, reaction, AI, engine-reference, and cleanup scenarios remain not-run.

Latest compact-obligation authority tranche (2026-07-26): `Fulfil a Compact Obligation` is now restricted to the balanced Otherworld compact path with an activated Compact Steward, live Otherworld cultural thresholds of `45/75/60/70`, and a real division already deployed in state 134 or 135. Its five-site map objective rechecks the named force and cultural components; the action still consumes 500 manpower and 20 Support Equipment and grants no units or supernatural material. Evidence: `docs/plans/ireland_focus_tree/compact_obligation_authority_tranche_2026-07-26.md`; trigger contract in `docs/ireland_dynamic_effects.md`. This closes one source-level canonical admission row only; live mission, unit-placement, cultural-decay, AI, engine-reference, and cleanup scenarios remain not-run.

Reconstruction-aid programme gate tranche (2026-07-25): `Accept or Refuse Reconstruction Aid` now requires a live or resolved FR11/RC07 foreign or multilateral programme offer, so the postwar calendar cannot create an unbacked aid action. The action retains its dynamic Political Power/Command Power and Foreign Exposure consequences without granting free materials, factories, shipping, units, territory, cores, recognition, or passive political power. Evidence: `docs/plans/ireland_focus_tree/reconstruction_aid_programme_gate_tranche_2026-07-25.md`. Live foreign-reaction, action, and cleanup scenarios remain not-run.

Commonwealth status gate tranche (2026-07-25): `Review Commonwealth Relations` now requires a recorded postwar constitutional or republican status transition—the standard republic/Commonwealth event closure or a full/partial Republic Settlement mission result—before British recognition, citizenship, trade, defence, and diplomatic review can begin. The action creates no free recognition, territory, cores, industry, equipment, units, shipping, fuel, administration, offices, alignment, or passive Political Power. Evidence: `docs/plans/ireland_focus_tree/commonwealth_status_gate_tranche_2026-07-25.md`. Live event, mission, AI, action, and cleanup scenarios remain not-run.

Current goal/law icon replacement (2026-07-28): the rejected prior goal and law sets have been replaced by 216 freshly generated, subject-specific HOI4-style goal emblems and 51 freshly generated, centered law-state emblems. Each goal is a transparent 100×88 icon with a readable silhouette, dark painted contour, matte period shading, route-specific subject matter, and no UI box, square tile, full-field background, or greenscreen matte. Each law state is a transparent 60×68 entry/reviewed/failure emblem with a shared visible center. Evidence: `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v12/manifest.json`, `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v12/audit_v12.md`, `assets/ireland_focus_tree/icons/regenerated_goal_icons_hoi4_focus_emblems_fresh_2026-07-28_v12/contact_sheets/goal_icons_complete_contact_sheet.png`, and `assets/ireland_focus_tree/icons/regenerated_law_icons_hoi4_idea_emblems_fresh_2026-07-28_v1/manifest.md`. The final DDS files are promoted under `gfx/interface/goals/ireland/` and `gfx/interface/ideas/ireland/laws/`; live engine and full feature validation remain open.

Latest Coastwatch sector lifecycle tranche (2026-07-28): the six historical Coastwatch sectors now have independent post, coverage, observer-training, communications, recognition, weather, rescue, and security-exposure ledgers. The existing action and 120-day mission select the first unfilled named sector, record full/partial/failure/escalation outcomes, allocate no more than the canonical 83 posts, and leave partial sectors retryable. Achievement history now reads only the operational sector records; unrelated air-warning, harbour-defence, and marine-patrol actions no longer satisfy Coastwatch-sector flags. Evidence: `docs/plans/ireland_focus_tree/coastwatch_sector_lifecycle_tranche_2026-07-28.md`; reusable effects are documented in `docs/ireland_dynamic_effects.md`. Live mission timing, AI selection, engine parsing, and cleanup scenarios remain not-run.

Latest Northern gate tranche (2026-07-25): `Plan a Coercive Northern Campaign` now requires route-valid command authority, separate border/corridor support, a produced Northern military cause, Readiness 60, Mobility 45, Provision 55, and Southern staging divisions. Belfast is no longer incorrectly required before the operation; full control, port, and arms-factory proof remains owned by the linked `Take and Hold Belfast` map objective. Evidence: `docs/plans/ireland_focus_tree/coercive_northern_campaign_gate_tranche_2026-07-25.md`. Live mission and cleanup scenarios remain not-run.

Latest intelligence admission tranche (2026-07-25): `Open a G2 Liaison Channel` now requires a valid foreign partner/channel or authored Northern war plan plus Irish sovereignty-and-review safeguards or Security Under Law. `Turn or Intern a Foreign Agent` now requires the active intelligence incident family plus Security Under Law or the National Emergency legal order. Evidence: `docs/plans/ireland_focus_tree/intelligence_admission_gate_tranche_2026-07-25.md`. Live incident, legal-order, partner-capitulation, and cleanup scenarios remain not-run.

Latest readiness authority tranche (2026-07-25): Coastwatch construction now hands its next unfilled named sector to the six-sector lifecycle, with controlled and infrastructure-connected regional platforms plus the border-observation record for the Northern interface; harbour defence requires a valid port authority and full control of the transferred Cork harbour; Marine Patrols require the Marine Service or a named shipping-route equivalent plus controlled port industry; and airspace interception requires Air Warning or a command-and-air-base Air Corps response. Evidence: `docs/plans/ireland_focus_tree/readiness_authority_gate_tranche_2026-07-25.md` and `docs/plans/ireland_focus_tree/coastwatch_sector_lifecycle_tranche_2026-07-28.md`. Live decision admission, mission, and cleanup scenarios remain not-run.

Latest occupation and regional authority tranche (2026-07-25): Disarm Paramilitary Organisations now requires a Northern division in state 119, Intelligence Readiness above the investigation floor, and a lawful Public Order, Security Under Law, or Vet and Rebuild Policing authority. Integrate or Devolve Military Command now consumes a Northern division, 25 Support Equipment, and 10 Army Experience. Offer a Protectorate Treaty now requires a recognised authority or proven Northern war/conquest/bargain record and opens the foreign-reaction window without granting free subjects, territory, cores, industry, equipment, units, fuel, shipping, administration, alignment, offices, or recognition. Evidence: `docs/plans/ireland_focus_tree/occupation_regional_authority_gate_tranche_2026-07-25.md`. Live unit-placement, authority-transition, foreign-reaction, and cleanup scenarios remain not-run.

Latest liberated-authority cause tranche (2026-07-25): Recognise a Liberated Authority now requires active war, war spillover, foreign-sponsor collapse, a Northern local-authority mandate, or a Northern wartime bargain in addition to its route, map, aid, and convoy gates. Recognition cannot appear from a regional route flag alone and still grants no free subject, territory, core, unit, or diplomatic status. Evidence: `docs/plans/ireland_focus_tree/liberated_authority_cause_gate_tranche_2026-07-25.md`. Live cause, foreign-reaction, mission, and cleanup scenarios remain not-run.

Latest Northern local-partner tranche (2026-07-25): Cross-Border Confidence Measures and Northern Delegations now require a named contact or mandate record in addition to their map, control, staff, consent, and mission gates. A Northern claim, route flag, or war plan alone is not treated as local participation. Evidence: `docs/plans/ireland_focus_tree/northern_local_partner_gate_tranche_2026-07-25.md`. Live partner, travel, mission, failure, and cleanup scenarios remain not-run.

Latest neutral-consultation partner tranche (2026-07-25): Convene a Neutral States Consultation now requires two separate valid diplomatic partners: a live Vatican channel with its named partner and the distinct neutral-states forum channel. The general foreign-safeguards flag can no longer count as two participants. Evidence: `docs/plans/ireland_focus_tree/neutral_consultation_partner_gate_tranche_2026-07-25.md`. Live one-channel, two-channel, invalidation, reaction-window, and cleanup scenarios remain not-run.

Latest foreign-access partner tranche (2026-07-25): Answer a Foreign Access Request now requires a named N07 access-chain source, a live valid foreign channel or recorded N07 reaction subject, and the sovereignty-mandate or sovereignty-safeguard record in addition to the active law, Treaty Port Complexes map, incident, and dynamic costs. A date alone can no longer create an access answer. Evidence: `docs/plans/ireland_focus_tree/foreign_access_request_partner_gate_tranche_2026-07-25.md`. Live source, channel, deadline, foreign-reaction, invalidation, and cleanup scenarios remain not-run.

Latest Atlantic-charter partner tranche (2026-07-25): Draft an Atlantic Consultation Charter now requires an explicit pair of willing state channels from the British, American, German, Vatican, or neutral-state families. A regional route or maritime value alone can no longer create a two-state charter. Evidence: `docs/plans/ireland_focus_tree/atlantic_charter_partner_gate_tranche_2026-07-25.md`. Live one-channel, two-channel, sponsor-invalidation, foreign-reaction, and cleanup scenarios remain not-run.

Latest failed-sponsor termination tranche (2026-07-25): Terminate a Failed Sponsor Agreement now requires a recorded British Supply, American Procurement, German Arms Promise, or Vatican Relief agreement plus matching channel invalidation, delivery failure, sponsor-collapse, dependency-failure, or named German-collapse refusal evidence. Completion closes only evidenced source channels, lowers their source leverage, applies a centralized Transport/Maritime Provision and Supply/Equipment Readiness shock, records termination, and opens replacement diplomacy; it grants no replacement aid or political victory reward. Evidence: `docs/plans/ireland_focus_tree/failed_sponsor_termination_gate_tranche_2026-07-25.md`. Live failure, source-specific closure, replacement, reaction-window, and cleanup scenarios remain not-run.

Latest operational platform safeguard tranche (2026-07-25): Organise Marine Patrols now requires full-control state 135 with both an industrial complex and naval base, and its convoy gate/charge are paired macros. Intercept an Airspace Violation now requires an air base in state 135 in addition to the active airspace family, response authority, Fighter, and Fuel gates. Evidence: `docs/plans/ireland_focus_tree/operational_platform_safeguard_tranche_2026-07-25.md`. Live building, incident, mission, AI, foreign-reaction, and cleanup scenarios remain not-run.

Latest wartime unity bargain tranche (2026-07-25): Prepare a Wartime Unity Bargain now requires the documented 1940/comparable-war context, defence estimates, command audit, ready Irish command, open valid British channel, Readiness 35, British Flexibility 45, Nationalist Consent 50, and Unionist Consent 20 or enforceable Northern safeguards. Its existing 50 Infantry Equipment and 25 Truck charges remain material costs; completion opens the Northern focus handoff and H14 gateway without granting control, occupation, settlement, integration, cores, or a finished war plan. Evidence: `docs/plans/ireland_focus_tree/wartime_unity_bargain_gate_tranche_2026-07-25.md`. Live focus, event, AI, reaction, and cleanup scenarios remain not-run.

Latest wartime unity lifecycle tranche (2026-07-25): the preparation action is one-shot, the H14 gateway is authoritative rather than date-autostarted, and the dated chain now records proposal rejection, defence cooperation without unity, postwar pledge, federal transition, Stormont refusal, Irish unpreparedness, negotiated unitary transition, and crisis destruction as distinct flags. An unresolved gateway is withdrawn at deadline, route closure, or British-partner loss; the Northern focus requires a resolved full-unity result and consumes its ready handoff. Evidence: `docs/plans/ireland_focus_tree/wartime_unity_lifecycle_tranche_2026-07-25.md`. Live event, AI, deadline, sponsor-collapse, focus, reaction, and cleanup scenarios remain not-run.

Latest member-contribution choice tranche (2026-07-28): the former single Support Equipment commitment is replaced by a five-way, paid selection event. The action now admits troops, ships, finance, intelligence, or infrastructure only when the selected payload and the current scarcity surcharge can be paid; event 431 records the class, the mission evaluates class-specific full/partial floors, cancellation refunds only that class, and terminal/route cleanup clears the ephemeral selection. Evidence: `docs/ireland_member_contribution_choice.md`. The later mission-capacity tranche resolves the Radical/Underground 8/10/conditional-12 capacity contract; source clearance remains open, while live checks remain excluded by user direction.

Historical completion-audit reconciliation (2026-07-29; superseded by the 2026-08-02 authority snapshot): this checkpoint recorded the earlier 64-review/57-blocked source state and 80/120 runtime budget. Its event consumers, source totals, and icon package evidence are historical; current status is stated at the top of this file and in `source_of_truth_map.md`.

The same sponsor tranche now persists `ireland_sponsor_dependence_failure` from a recorded agreement when source leverage breaches the shared dependency ceiling or the named German collapse refusal occurs. The failure feeds the law registry, AI recovery, route disqualification, and termination gate; the temporary foreign-sponsor overlay remains derived.

Current part: Part 7 of 7

Planning mode: implementation and validation follow-up

Project completion state: implementation is in progress; the current source manifest has 166 complete, 0 needs_user_review, and 3 blocked rows (3 portraits, 0 symbols/documents, 0 event/news), with the canonical 120/120 event-picture budget available. M2 and A2 are settled by the 2026-08-01 authority ruling. The GUI overlap reports are classified as intentional state-layer geometry; the aggregate validator remains false only for controlled-reuse/offline-renderer limitations. The five FRUS consumer gaps are repaired; Daniel Morrissey remains an external conditional-C3 extension and Father Edward Cahill remains blocked. The round-12 exact-source handoff records its conditional promotions, the round-13, round-14, and round-15 handoffs record the exact P-50, P-54, and P-31 promotions, and round 24 records the exact P-15 promotion. Rounds 25 and 26 record the negative evidence for P-26, P-45, and P-55; all three remain unresolved exact-person portrait blockers. The public-achievement dossier is wired through the existing third GUI surface. Live runtime scenarios are excluded from the goal completion gate by user direction.

Older static-tranche notes retain superseded goal/law packages as historical evidence. The fresh goal/law package at `assets/ireland_focus_tree/icons/regenerated_goal_and_law_icons_fresh_2026-08-01_v1/` and the seven-row fresh spirit package are the current source evidence; their verified DDS files are promoted under the standard runtime `gfx/` roots.

Documentation authority note (reconciled 2026-08-03): use `docs/plans/ireland_focus_tree/source_of_truth_map.md` for the normalized implemented/partial/blocked/queued/not-run ledger. The current authority snapshot at the top of this file and that map supersede older static rechecks; neither file is a gameplay completion claim.

Runtime asset placement correction (reconciled 2026-08-02): `assets/ireland_focus_tree/` is temporary source, processing, manifest, contact-sheet, review, and evidence staging. Final runtime DDS files belong under the standard mod `gfx/` tree; see `docs/plans/ireland_focus_tree/assets/runtime_placement.md`. The current Ireland-owned `.gfx` registrations contain no runtime texture paths into `assets/`.

Latest static tranche (2026-07-25, with 2026-07-28 asset/cost refresh): the 236-flavour localisation namespace has 944/944 source references resolved, 236 distinct substantive descriptions, and 472 distinct option labels; the standard event surface now has 220 unique descriptions and 217 unique `a`/`b` choices after the route-voice expansion, and all 140 action descriptions now have distinct route-specific prose; see `docs/plans/ireland_focus_tree/localisation_route_voice_tranche_2026-07-25.md` and `docs/plans/ireland_focus_tree/audits/ireland_localisation_recheck_2026-07-22.md`. The current v12 216-row focus-goal package and v1 51-row law-state package are freshly generated, reviewed as consistent transparent 100x88 and centered 60x68 families, documented with per-item/state manifests and audits, and promoted under `gfx/interface/goals/ireland/` and `gfx/interface/ideas/ireland/laws/`. Sixty-one actions consume explicit equipment, manpower, fuel, convoy, train, or truck inputs where the current canonical cost map names those commitments; named projects reserve native civilian-factory capacity with timed cleanup. The latest material tranche covers agricultural logistics, reserve/security forces, emergency turf/livestock, liberated-authority, command, compact-obligation, local administration, relief, neutral-shipping, cultural-congress, western-portfolio, historic-site, internment, Blacksod-station, and member-contribution burdens. The regional defence proposal also requires Readiness 75, Provision 65, a ratified membership record, common threat, safeguards, and a named division presence. The bounded 26 July material/safeguard audit finds no additional aircraft, listed shipping, foreign-channel, leverage, or physical-charge defect at source level; the full 140-row per-ID disposition, member-contribution class choice, source clearance, live engine/reference checks, and required scenarios remain open. Thirty-three coded cancellation-refund branches use the capped recoverable-input helper. Semantic GUI animation gates wait for convention, evidence-ledger, convergence, and explicit obligation-breach milestones. No live engine was launched.

Historical implementation recheck (2026-07-24): this record preserves earlier source-level cost, material, AI, and event-consumer measurements. It is not current status authority; the current decision-cost, AI, event-consumer, source-clearance, and asset evidence is recorded in the 2026-08-02 audit documents named above.

Latest focus/asset repair (2026-07-22): the focus filter now uses the vanilla `FOCUS_FILTER_INTERNATIONAL_TRADE` token; all 216 focus icons have paired shine registrations and final masks under `gfx/`; the standard shine overlay is also present under `gfx/`; O'Duffy's personal and corporate capstones are mutually exclusive; the 31 national-focus plans have valid focus references, including the serious-culture plan; clerical, High Kingship, Five Provinces, and Otherworld crisis/category gates now use the current route flags. Source clearance and live-engine gates remain open.

Material-cost follow-up correction (2026-07-24): the current material-cost evidence includes the electoral-staffing, harvest-fuel, operational-security, public/Northern-administration, cultural-congress, western-portfolio, historic-site, internment, Blacksod-station, member-contribution, Folklore, British-flexibility, and tax/debt follow-up. The current measured totals are 64 actions with explicit physical or manpower inputs and 33 coded cancellation-refund branches; the authoritative details are `docs/plans/ireland_focus_tree/ireland_material_cost_tranche_2026-07-24.md` and `docs/plans/ireland_focus_tree/action_material_gate_reconciliation_tranche_2026-07-26.md`.

Neutrality incident lifecycle tranche (2026-07-25): internment and foreign-access response actions now require their active incident flags and corresponding law flags, and each response closes the named incident through the shared cleanup helper. The aircrew internment map objective carries the same incident and law gates. Evidence: `docs/plans/ireland_focus_tree/neutrality_incident_lifecycle_tranche_2026-07-25.md`. This is a source-level repair; live law-transition, incident-response, and cleanup scenarios remain not-run.

Plan W liaison gate tranche (2026-07-25): `Formalise Plan W Liaison` now requires invasion danger or war, the British channel and partner, Border Belt control, Provision 40, Readiness 35 with Command 30, Intelligence 30, and Supply 25, plus the foreign-access law and sovereignty safeguards. Evidence: `docs/plans/ireland_focus_tree/plan_w_liaison_gate_tranche_2026-07-25.md`. Live partner, law, reaction, and cleanup scenarios remain not-run.

Border corridor gate tranche (2026-07-25): `Open a Border Corridor` now requires a named pressure source, a controlled division in the Border Belt force area, a completed local security/defence/policing preparation, the existing 250 manpower and 5 Truck commitment, and authored Northern Security Stability/British Leverage deltas. Evidence: `docs/plans/ireland_focus_tree/border_corridor_gate_tranche_2026-07-25.md`. Claims, control, occupation, settlement, integration, and cores remain separate; live map-control, failure, and cleanup scenarios remain not-run.

Airspace interception lifecycle tranche (2026-07-25): the interception action now reads the airspace incident family instead of the internment family, consumes its existing Fighter/Fuel commitments, improves Readiness Intelligence, and records a forced-landing handoff that the internment action and map objective can consume under the internment law. Mission, route, and incident cleanup clear the handoff. Evidence: `docs/plans/ireland_focus_tree/airspace_intercept_lifecycle_tranche_2026-07-25.md`. Live incident-source and timeout scenarios remain not-run.

Airspace equipment vocabulary repair (2026-07-28): the interception gate and negative five-aircraft charge now use the six concrete vanilla fighter equipment types, selecting the first qualifying type; the undefined bare `fighter_equipment` token is gone. The existing 100-fuel charge, readiness delta, forced-landing handoff, and cleanup boundaries are unchanged. Evidence: `docs/plans/ireland_focus_tree/equipment_archetype_vocabulary_repair_2026-07-28.md`. Live parser and airspace scenarios remain not-run.

Neutral shipping loss lifecycle tranche (2026-07-25): `Investigate a Neutral Shipping Loss` now reads the shipping incident family instead of the foreign-access family, requires the trade/shipping law plus Marine Service and Intelligence readiness above the canonical 5 floor, and mirrors the mission's full-control Munster industry and Leinster naval-base proof. `Mark and Publicise Neutral Shipping` also requires an existing Irish, chartered, purchased, or renewed merchant route. Evidence: `docs/plans/ireland_focus_tree/shipping_loss_lifecycle_tranche_2026-07-25.md`. Live shipping-source, law-transition, mission-result, foreign-reaction, and cleanup scenarios remain not-run.

This file began as a Part 7 planning checkpoint. Its source-processing and archive measurements below are retained as historical planning evidence. The current implementation status is recorded in the source-of-truth map and completion follow-up above.

# Source processing

The final-gate source sweep opened every available Markdown, TOML, text, JSON, and CSV source under `/mnt/data` before the repaired build was generated. The sweep covered 96 files, 3,157,304 decoded bytes, 42,620 lines, and 456,232 whitespace-delimited words with no decoding errors.

The canonical source set contains 35 Markdown files, 2,402,852 bytes, 30,809 lines, and 351,304 whitespace-delimited words. The semantic inventory also processed 2,634 headings and 763 Markdown tables.

The checksum-verified cumulative candidate was used as the repair base. Some direct workspace plan copies had been overwritten by older uploads, so they were not treated as authoritative until the repaired build was validated and synced back.

The offline Paradox wiki snapshot and local Windows Hearts of Iron IV installation were consulted during the implementation phase as required by `AGENTS.md`; the engine-facing checks and runtime scenarios remain open.

# Canonical Part 7 files

| File | Status | Purpose |
| --- | --- | --- |
| `docs/specs/ireland_focus_tree/ireland_focus_tree_index.md` | complete | source authority, file inventory, constants, labels, reading order, and package state |
| `docs/specs/ireland_focus_tree/matrices/ireland_focus_tree_route_coverage_matrix.md` | complete | all 30 profiles, support and recovery roles, standard conclusions, and composite convergence |
| `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_canonical_reconciliation_map.md` | complete | source precedence, implementation order, and canonical cleanup decisions |
| `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_mechanic_reconciliation_map.md` | complete | mechanic ownership, fixed constants, and cross-system interfaces |
| `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_cross_surface_reconciliation_map.md` | complete | events, AI, achievements, assets, research, GUI, animation, and prompt ownership |
| `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_coding_prompt.md` | complete | implementation order and completion contract |
| `docs/specs/ireland_focus_tree/prompts/ireland_focus_tree_goal_prompt.md` | complete | concise implementation goal below 4,000 characters |
| `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_improvement_loop_execution_prompt.md` | complete | self-contained prompt for the mandatory worker |
| `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_improvement_loop_execution_record.md` | complete | records the completed `fork_context=false` worker execution |
| `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_parent_review.md` | historical | parent closure review, retained as separate planning evidence |
| `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_finding_disposition.md` | implemented for planning findings | normalized implemented, queued, partial, and blocked findings |
| `docs/plans/ireland_focus_tree/part_7_final_gate_attempt_report.md` | complete | final-gate repairs and worker availability check |
| `docs/plans/ireland_focus_tree/part_7_source_processing_report.md` | complete | full source-processing and canonical-inventory evidence |
| `docs/plans/ireland_focus_tree/part_7_validation_report.md` | complete | canonical source validation and completion-gate state |
| `docs/plans/ireland_focus_tree/part_7_package_manifest.md` | complete | candidate archive boundary and verification contract |

# Integrated Part 7 repairs

1. Added one canonical source index and authority order.
2. Added a 30-profile route coverage ledger separating durable routes, support profiles, recovery profiles, and composite convergence.
3. Added the exact ten temporary AI overlays promised by Part 6.
4. Added the exact twelve foreign response action classes promised by Part 6.
5. Added five source-clearance states, eleven source tiers, and a per-item asset manifest contract.
6. Reserved AI-12 for a culture-led national programme while normal cultural work remains under the current host-government profile.
7. Defined final convergence as the composite highest variant of the fifteenth standard conclusion family.
8. Normalised GUI, Ailtirí, Five Provinces, Otherworld, and convergence labels.
9. Reconciled the minimum 484 player-facing events, 236-event flavour floor, and 120-image reuse programme.
10. Created the full coding prompt, bounded workstream prompts, and goal prompt.
11. Removed backups and interim checkpoint material from the canonical package boundary.
12. Reconciled source precedence, mechanic ownership, cross-surface dependencies, and implementation order.
13. Removed nonpackaged plan dependencies from the mandatory worker prompt.
14. Normalised AI-29 Otherworld containment from `A/P` to the canonical `P/A` transition.
15. Rebuilt the status, validation, and package ledgers from one measured source inventory.
16. Added the root README and corrected the archive boundary to 47 entries.
17. Replaced eleven circular focus self-gates with authoritative upstream
    milestones or live partner checks, and exposed the Treaty Port and
    sovereignty gateway prerequisites in the focus layout; see
    `focus_reachability_gate_tranche_2026-07-25.md`.
18. Replaced the repeated standard-event copy across constitutional, wartime,
    political, neutrality, economy, Northern, crisis, and postwar families with
    route-specific descriptions and choices that retain dynamic ledger values;
    the source-level result is 220 unique descriptions and 217 unique standard
    option pairs, with all 140 action descriptions also distinct after the
    route-specific tail cleanup. Mission wording remains open; see
    `localisation_route_voice_tranche_2026-07-25.md`.

# Fixed design state

All accepted Parts 1 through 6 constants and gates remain binding. This includes:

- National Settlement opening `+25`, momentum `-1`, seven stages, and transformation rules
- Social Consent `55`, Readiness `15`, and source-specific leverage
- Dáil `153` formal and `152` routine
- Provision components `55`, `25`, `40`, `30`, displayed `38`
- Readiness components `25`, `8`, `20`, `12`, `5`, `5`, `30`, displayed `15`
- Neutrality Integrity `72`
- Northern opening `U5 N40 L30 B10 S45 I10`
- three persistent route-spirit families
- thirteen decision categories, 140 actions, and 54 mission families
- mission caps `8`, `10`, and conditional `12`
- command power ceiling `60`
- eighteen historical event families, eighteen political crisis families, twelve foreign reaction families, at least 236 flavour events, and minimum 484 player-facing events
- exactly 30 AI profiles and ten overlays
- twelve foreign actor families and twelve primary action classes
- exactly 32 achievements
- the exact Part 6 asset budgets, three GUI surfaces, seven animations, and three optional audio briefs
- Northern cores only after stage `5` and final review
- the full canonical Dillon gate

# Validation state

The repaired Part 7 validation suite records:

- 35 canonical Markdown files
- 351,304 canonical words
- 30,809 canonical lines
- 2,402,852 canonical bytes
- 366 passed checks
- 0 failed checks
- 0 warnings
- 1 blocked completion gate

The planning gate is no longer blocked: the returned `hoi4_improvement_loop_planner` report is recorded and its findings are dispositioned. The current non-live engine-reference, asset-placement, localisation, AI, GUI, achievement, and event audits are reconciled; the remaining implementation gate is exact-source clearance. Live runtime scenarios remain excluded by user direction.

# Improvement-loop state

The parent review recommends closure rather than broad expansion. Twelve parent findings were recorded. Eleven were integrated into canonical sources. Earlier planning notes about unavailable local implementation references are retained as historical evidence; the current implementation audit has since consulted the required local references. Seven final-gate audit findings were also recorded, with six integrated and one blocked.

The required `hoi4_improvement_loop_planner` process completed with `fork_context=false`. Its returned report is recorded at `ireland_focus_tree_improvement_loop_execution_report.md`; the alias file preserves the expected output name. The parent review and older final-gate records remain historical and are not used as substitutes.

Accepted worker report:

`docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_improvement_loop_execution_report.md`

# Candidate package state

The repaired planning source set was packaged as:

`ireland_focus_tree_parts_1_to_7_canonical_candidate.zip`

The archive contains 35 canonical sources, 10 supporting evidence files, the root README, and the internal checksum ledger. It is planning evidence only; it does not prove gameplay completion. The current implementation remains incomplete until the three exact-person portrait blockers and every required non-live audit are closed; the local engine-reference evidence is recorded separately in the current audit set.

# Exact stopping point

The current stopping point is the implementation evidence gate recorded in `docs/plans/ireland_focus_tree/audits/ireland_completion_recheck_2026-07-23.md`.

Remaining work:

1. Resolve the three remaining blocked portrait rows (P-26, P-45, and P-55) only through exact person-labelled source objects with a compatible rights basis and period fit; do not use a wrong-person image, generic substitute, placeholder, or generated likeness. P-15, P-31, P-50, and P-54 are complete from exact mapped historical sources. The 120/120 event-picture budget and all 40 symbol/document packages are complete under the conditional handoffs. Preserve the separate Daniel Morrissey conditional-C3 and Father Edward Cahill blocked route-extension dispositions. Fresh scenarios are optional evidence and remain outside the completion gate by user direction.
2. The local engine-reference, parser, asset, localisation, AI, GUI, achievement, and event checks are recorded as complete at the non-live static boundary; rerun them after any source/runtime promotion.
3. Keep the fresh-1936, historical/nonhistorical, route, failure/recovery, Northern, hidden-route, AI, GUI, and 32-achievement scenario programme documented as optional unrun evidence; it is excluded from the goal completion gate by user direction.
4. Keep this status and the follow-up audit synchronized with any source-clearance promotion or rejection.
5. Mark the feature complete only after no canonical requirement or non-live validation requirement remains blocked.

# Tooling state

- The current workspace is the Ireland Total Overhaul Git repository; no completion commit has been made for the incomplete implementation.
- The offline wiki and local HOI4 installation were available and consulted; local engine-reference validation is reconciled, while live engine execution remains intentionally unrun.
- The custom improvement-loop worker execution is recorded with `fork_context=false`; no second broad planner pass is required while the current implementation blockers remain.
- The planning archive is release-candidate evidence, not a final gameplay-completion package.

## Round 23 portrait-source addendum

The direct official object checks did not close the three remaining source blockers. The
Oireachtas Patrick Cogan image endpoint returns a generic SVG avatar rather
than a Cogan portrait; the official Michael Fitzpatrick endpoint returns the
same generic avatar. The History Ireland Blueshirt image for P-55 is a group
scene with no face mapping to Walsh. No portrait row or runtime consumer
changed. The dated
handoff is
docs/plans/ireland_focus_tree/assets/source_research_handoffs/portrait_exact_object_search_round23_2026-08-03.md.
