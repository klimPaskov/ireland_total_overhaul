# Ireland event-surface re-audit — 2026-07-29

Feature slug: `ireland_focus_tree`

This is a non-live source audit. Hearts of Iron IV was not launched, and no
in-game scenario or save was used.

## Source files checked

| Surface | Source | Blocks | Unique IDs | Options |
| --- | --- | ---: | ---: | ---: |
| Main historical, crisis, material, Northern, foreign-reaction and conclusion events | `events/ireland_events.txt` | 251 | 251 | 506 |
| Generated public-conclusion records | `events/ireland_public_conclusion_events.txt` | 2 | 2 | 2 |
| Regional member-contribution selection | `events/ireland_member_contribution_events.txt` | 1 | 1 | 5 |
| Consequential flavour events | `events/ireland_flavour_events.txt` | 236 | 236 | 473 |

The main file has 248 registry-marked H/P/N/NR/FR/PW nodes. The three
additional blocks are the two explicitly named Five Provinces evidence nodes
(`ireland_events.217` and `.219`) and the foreign-reaction digest
(`ireland_events.430`). The separately owned public-conclusion file
contains `.432` and `.433`, which consume the generated High Kingship and
Northern unity news assets without granting territory, cores, resources, or
offices. Event `.431` remains the separately owned member-contribution
selection. The flavour registry contains F01–F19 and all 236 node markers are
present.

## Localisation and lifecycle results

- Every main event title and description key resolves in
  `localisation/english/ireland_l_english.yml`.
- Every main option name resolves: 506/506.
- All six title, description, and option keys in the two public-conclusion
  records resolve.
- All seven title, description, and option keys in the separately owned
  member-contribution selection resolve.
- Every flavour title and description key resolves.
- Every flavour option name resolves: 473/473.
- Every event block contains an `ai_chance` block and an `after` cleanup
  block.
- Every flavour block contains at least one consequential state/effect
  surface; no flavour block is an empty narrative shell.
- Main and flavour event IDs are unique within their source files.

## Picture registration

The four event files use 78 unique `picture` sprite names. All 78 are
registered in the Ireland-owned interface GFX sources. Runtime texture paths
for those registrations were checked separately against the standard mod
`gfx/` tree; no event-picture registration points into the temporary
`assets/` tree.

## Scope and remaining gates

This re-audit closes the source-level event/localisation coverage check. It
does not prove engine parsing, event ordering, AI selection, live timing,
source-rights clearance, or scenario outcomes. The broader completion gate
therefore remains open for the source-clearance queue, the documented
achievement-schema limitation, the Radical/Underground mission-capacity
wording contradiction, and any remaining local engine-reference evidence.
