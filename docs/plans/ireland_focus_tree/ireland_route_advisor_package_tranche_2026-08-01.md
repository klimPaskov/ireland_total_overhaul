# Ireland route advisor package tranche — 2026-08-01

## Scope

This tranche closes the country-package gap where route characters were only
country leaders and the Ireland package still relied on an undifferentiated
vanilla advisor roster. It adds thirty sourced historical advisor characters,
retains the two earlier paid route advisors, and replaces the three vanilla
source-backed starting advisor tokens for Oscar Traynor, Douglas Hyde, and
Seán T. O'Kelly.

The package remains inside the H/P boundary. No alternate, supernatural, or
fictional person is represented by a real-person portrait, and no advisor is
activated for free by a focus or political victory.

## Added roles

| Surface | Characters | Runtime role |
| --- | --- | --- |
| Historical starting roster | Oscar Traynor; Douglas Hyde; Seán T. O'Kelly | theorist or political advisor with dated constitutional visibility |
| Fianna Fáil and developmental government | Frank Aiken; Seán MacEntee | political advisor on the de Valera/Lemass routes |
| Fine Gael, coalition, and intervention | Joseph Walshe; Seán Mac Eoin; Thomas F. O'Higgins; Patrick McGilligan | foreign, defence, interim-parliamentary, and legal/administrative portfolios |
| Labour and unions | James Everett; William O'Brien; James Hickey; William Davin | parliamentary and union-facing political portfolios on the Norton route |
| Clann na Talmhan | Michael Donnellan | agrarian political portfolio after the dated party foundation |
| Church and service domains | Edward Joseph Byrne; John Charles McQuaid; Joseph MacRory; Frank Duff; John Hayes | domain-specific service, Church, lay, and vocational portfolios |
| IRA | Maurice Twomey; Tom Barry; Jim O'Donovan; Seán MacBride; Charles Kerins | civil movement, Army Council, intelligence, bridge, and late-command portfolios |
| Republican Congress | George Gilmore; Nora Connolly O'Brien; Seán Murray | plural and vanguard movement portfolios |
| O'Duffy and Ailtirí | Patrick Belton; Ernest Blythe; Oliver J. Flanagan | corporate patronage, ideological movement, and dated postwar Ailtirí portfolio |

`common/characters/slopx_ireland_route_characters.txt` now contains 32
advisor blocks: the existing Seán Lemass and Richard Mulcahy appointments plus
the thirty roles above. Each role has a stable `idea_token`, a registered
portrait sprite, an explicit slot and trait, a normal 100 PP appointment cost,
and a route/date/office gate.

## Lifecycle contract

`slopx_ireland_route_advisor_*` scripted triggers in
`common/scripted_triggers/slopx_ireland_triggers.txt` separate constitutional,
Fine Gael, Labour, Clann, vocational, clerical, IRA civil, IRA command,
Congress, O'Duffy, and Ailtirí authority. The route activation effect recruits
only the roster that belongs to the selected route. The lifecycle synchroniser
dismisses hired advisors after route, office, archive, command, closure, or
date invalidation; route cleanup retires the character so a later valid
recovery can recruit the role again without stacking duplicate identities.

The starting history now uses the custom sourced tokens for Traynor, Hyde, and
O'Kelly. Their portraits remain ordinary paid advisors: historical start
recruitment does not hire them or grant political power.

## Source and asset evidence

Every portrait used by this tranche is a `complete` P-row in
`docs/plans/ireland_focus_tree/assets/source_manifest.json`, with C4 or the
user-approved C3 conditional clearance state. Source masters remain preserved
under `docs/portraits/` and temporary `assets/` research packages; runtime DDS
files remain under the standard mod paths in `gfx/leaders/ireland/`. Existing
GFX registrations in `interface/slopx_ireland_sourced_assets.gfx` are reused;
no portrait was generated or reprocessed as a substitute for a missing source.

## Validation evidence

- Ireland route character source braces: `539/539`.
- Ireland runtime effect braces after the lifecycle additions: `10106/10106`.
- Ireland scripted-trigger braces: `1786/1786`.
- Custom advisor tokens: `32`, all unique.
- Custom advisor recruits: all have matching character definitions.
- Portrait references: all resolve to registered GFX sprites.
- Touched files contain no unsupported `<=` or `>=` operators.
- Live HOI4 testing was intentionally excluded from this tranche.

## Remaining package boundary

This tranche does not silently convert every sourced event actor into an
advisor. Frank Ryan, Peadar O'Donnell, Gearóid Ó Cuinneagáin, Eoin O'Duffy,
and collective councils remain movement or country-leader offices whose
canonical survival, succession, or route-law gates are separate from ordinary
advisor hiring. Their existing lifecycle code remains authoritative until a
matching office matrix and failure chain is wired.
