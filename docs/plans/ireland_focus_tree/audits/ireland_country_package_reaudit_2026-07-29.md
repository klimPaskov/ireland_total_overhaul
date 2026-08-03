# Ireland country-package re-audit — 2026-07-29

Status: **historical structural evidence; live play is intentionally excluded from the completion gate by user direction**.

Supersession note (2026-08-01): the source-clearance and portrait-status
measurements in this dated re-audit are historical. The current authority is
`docs/plans/ireland_focus_tree/assets/source_manifest.json` and
`docs/plans/ireland_focus_tree/audits/ireland_review_row_route_portrait_reaudit_2026-08-01.md`,
which reconcile the manifest to 110 complete / 2 review / 57 blocked rows,
clear the six canonical route portraits P-05, P-06, P-27, P-43, P-46, and
P-56 as conditional C3 runtime sources, and leave only the separate Daniel
Morrissey route extension review-gated among currently consumed portrait
extensions. The older measurements below remain preserved for audit history.

Fresh completion-audit reconciliation (2026-07-29): the authoritative
169-row manifest is currently 47 complete, 56 `needs_user_review`, and 66
blocked. Family status is portraits 11/33/16, symbols 7/11/22, and event/news
29/12/28 (complete/review/blocked). The clearance-state distribution is C1 40,
C2 29, C3 75, and C4 25. Tiers are T1 45, T2 18, T3 29, T4 24, T5 7, T6 9,
T7 19, T8 9, T9 7, T10 0, and T11 2. All twenty-three round-3 review
candidates remain non-runtime. Ten exact NLI/UCD
leads advanced from C1 to C2 while staying blocked. Current source evidence
maps EV-SRC-003 to event .109, EV-SRC-021 to .110, EV-SRC-039 to .111, and
EV-SRC-057 to .254. Runtime consumed budget assets are 80/80 complete, while
the overall 120-image budget is 80/120 complete. The runtime inventory is 878
DDS files total, of which 877 are Ireland-owned. The Ireland GFX audit records
1,106 texture references and 346 unique sprite names. These are current
static-audit facts, not a gameplay completion claim. The machine manifest is
the settled source-clearance authority for these counts.

This re-audit supersedes the package-gap conclusions in
`ireland_country_package_audit_2026-07-18.md` where later source repairs are
explicitly listed below. It is a read-only source audit; no HOI4 launch or
fresh-save scenario was used.

## Opening boundary

- `history/countries/IRE - Ireland.txt` starts Ireland in state `113`, keeps
  the vanilla `IRE_1936` baseline, recruits the vanilla 21-character roster,
  and calls the guarded `slopx_ireland_initialize_campaign` effect.
- `history/states/119-Northern Ireland.txt` keeps state `119` owned by `ENG`
  with only `ENG` and `NIR` cores. The mod does not give Ireland an opening
  owner, controller, core, or transfer there.
- The Northern ledger starts separately from the map and the dedicated focus
  still grants only a claim. Control, occupation, settlement, integration,
  final review, and the later core are separate ledgers.

## Route leaders and identity

`common/characters/slopx_ireland_route_characters.txt` contains 24 route
character blocks: ten named historical people and fourteen institutional or
collective offices. The institutional entries are used only for alternate or
symbolic route identities; they do not fabricate a real-person portrait.

`common/scripted_effects/slopx_ireland_runtime.txt` contains 24 matching
promotion paths and 24 recruitment calls across the route lifecycle. The
retirement helper clears outgoing route leaders before a new route is
activated, and the transition is protected by
`slopx_ireland_route_leader_transition_complete` plus per-route activation
flags. The ordinary route-specific political identity path also sets the
appropriate ruling ideology/election state and party-name keys.

The 24 portrait sprite names referenced by the route-character file are all
registered in the Ireland interface GFX files. Sourced real-person portrait
masters and processed crops are preserved in
`docs/portraits/source_originals/` and `docs/portraits/processed_png/`;
clearance states remain authoritative in the source manifest. Generated
collective portraits remain outside that archive because they are symbolic
route assets rather than source-found people.

The 18 route cosmetic tags in
`common/countries/slopx_ireland_cosmetic.txt` are all referenced by the route
identity synchroniser, with no undefined or unused route tag in the static
registry sweep.

## Northern core boundary

`slopx_ireland_can_northern_core_review` requires, in addition to stage five
integration and the completed settlement ledger:

- the consent floors for Unionist, Nationalist, Labour, and British channels;
- security stability and integration capacity floors;
- controlled state `119` with the resistance ceiling;
- all named policy-proof, representation, policing, courts, finance,
  services, transport, rights, resistance, guarantees, withdrawal,
  demobilisation, security-sustainment, and emergency-law completion flags;
- no occupation or settlement failure and no core-review block.

`slopx_ireland_apply_northern_core_review` is the sole map-core mutation. It
adds the Ireland core only when that trigger passes, records the durable core
flag, and is idempotent. A completed final review without control records a
blocked review instead of granting a core.

## Static reference checks

- 24/24 route portrait GFX references are registered.
- 18/18 route cosmetic tags are defined and referenced.
- The current runtime inventory contains 878 DDS files, with 877 identified as
  Ireland-owned by the fresh completion audit.
- The Ireland GFX audit records 1,106 texture references and 346 unique sprite
  names. The Daniel Morrissey DDS remains a review-gated runtime candidate and
  does not change its manifest clearance.
- The current source consumers are EV-SRC-003 -> .109, EV-SRC-021 -> .110,
  EV-SRC-039 -> .111, and EV-SRC-057 -> .254. This is static source wiring
  evidence, not a live event-firing claim.
- The exact ten NLI/UCD leads that advanced from C1 to C2 while remaining
  blocked are S-06, S-07, S-08, S-09, S-12, S-13, S-15, S-18, S-19, and S-20.
- New symbol review IDs S-04, S-11, S-14, and S-21 remain review-only and are
  not promoted to runtime.
- Runtime consumed budget assets are 80/80 complete against the overall
  120-image budget of 80/120 complete; review-only symbol candidates remain
  outside runtime promotion.
- The 216-focus Ireland inspection remains at zero Ireland-local layout or
  source diagnostics; unrelated global vanilla diagnostics are not patched.

## Remaining open surfaces

This re-audit does not close the authoritative source-clearance queue
(56 review-gated and 66 blocked manifest entries, including 16 blocked
portraits), the two-slot Radical / Underground mission wording contradiction,
or the documented stock achievement visibility limitation. The fresh
completion audit also found seven live-review portrait references still wired
to current route-character/GFX surfaces: P-05, P-06, P-27, P-43, P-46, P-56,
and route extension RC-PORTRAIT-01 (Daniel Morrissey). Current source evidence
still shows those review-gated references; no fix is claimed. The NR07
early-admission defect is fixed: the four event blocks and matching dispatcher
limits directly require `slopx_ireland_northern_core_review_open`, and its sole
writer enforces final-review proof, stage-five integration, control, and clean
occupation/settlement state. The bounded source checks pass; the full
comparison tool timed out and remains a tooling limitation. The unresolved
issues require an accepted source/design decision
or an engine-supported schema decision and must not be hidden by a generic
fallback. Live engine parsing and gameplay scenarios remain recorded as
unrun evidence only, per user direction.

## Superseded measurements retained for audit history

The earlier 808-texture-reference and 28-review/101-blocked measurements are
historical snapshots from the first pass of this reaudit. The preceding
47/42/80 and 47/32/90 completion snapshots, with their earlier clearance
totals, are also superseded for current status by the latest
1,106-reference / 346-sprite and 55-review / 67-blocked results above. The
historical values are retained here so the audit record is not rewritten.
