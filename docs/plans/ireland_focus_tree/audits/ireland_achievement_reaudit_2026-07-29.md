# Ireland achievement reaudit — 2026-07-29

## Scope

This is a current-worktree source, history-writer, localisation, and visual-asset
audit of the canonical 32 Ireland custom achievements. Hearts of Iron IV was not
launched, and no live achievement unlock is claimed.

The engine references used for the schema check were:

- `paradox_wiki/Achievement modding - Hearts of Iron 4 Wiki.md`;
- vanilla `common/achievements.txt`;
- vanilla trigger documentation for
  `has_completed_custom_achievement`;
- the approved Kaiserreich precedent
  `common/achievements/KR_achievements.txt`.

## Exact roster and eligibility

`common/achievements/ireland_achievements.txt` contains:

- the unique package ID `ireland_total_overhaul_ireland_focus_tree`;
- exactly 32 achievement blocks;
- the same 32 identifiers, in the same order, as
  `ireland_focus_tree_achievement_matrix.md`;
- exactly seven `hidden = yes` entries: A-22, A-27, A-28, and A-29 through
  A-32.

Every `possible` block requires Ironman, difficulty above one, the exact 1936
start-date window, no custom difficulty setting, achievement-compatible game
rules, current tag IRE, and original tag IRE. Every `happened` block rechecks the
current and original tag, the Ireland initializer, and the shared campaign
disqualification record.

The last two literal achievement thresholds were moved into the file-scoped
tuning contract:

- the partner-depth ceiling used by A-03;
- the zero floor used by A-29's accepted-obligation count.

## Current A2 authority disposition — 2026-08-01

A2 is accepted. A-22, A-27, and A-28 use static `hidden = yes` declarations
with their canonical earned and reveal conditions in `happened`. The local
engine references do not provide a supported trigger-valued visibility field,
so this implementation does not invent one. The schema discussion below is
historical evidence for that decision, not an open approval blocker.

## Historical proof and anti-exploit wiring

The achievement blocks consume 192 distinct `ireland_achievement_*`
history flags and 24 distinct achievement-history variables. A current source
scan found at least one gameplay writer for every consumed flag and variable
outside the achievement declaration file.

The Northern achievements A-23, A-24, A-25, A-28, and A-32 all require the
stage-five/core-eligible integration threshold and
`ireland_northern_final_review_passed`. None treats a claim, control,
occupation, settlement, or war victory as integration.

The authoritative hidden and mastery entries retain their named public-reveal
or evidence gates, full conclusions, disqualifiers, obligation history, rights
checks, sponsor/client checks, and Northern final-review checks. No achievement
unlocks from route selection or a single focus.

## Localisation and icon budget

All 64 required localisation keys (`_NAME` and `_DESC` for every identifier)
resolve.

The authoritative runtime icon root is `gfx/achievements/`. It contains exactly
96 Ireland DDS files:

- 32 completed icons;
- 32 `_grey` icons;
- 32 `_not_eligible` icons.

Every file uses its full achievement identifier, all are `64x64`, all 96 byte
hashes are unique, and no extra ordinal `achievement_ireland_NNN.dds` copy
remains in the runtime root. DDS readback found no bright-green key pixels.
Visual review of the full contact sheet found consistent square medallion
framing, centred subjects, matched grey states, and the same red ineligibility
overlay across the family. No neighbouring atlas tile appears at an edge.

The staging-only asset package contains the matching 96 source PNGs and 96
processed PNGs plus the contact sheet. Its ordinal basenames map one-to-one to
the full runtime identifiers documented in
`assets/ireland_focus_tree/icons/ireland_icon_animation_manifest.md`.

## Historical staged-visibility engine analysis

The canonical roster asks A-22, A-27, and A-28 to be hidden before a named public
route reveal and visible afterwards. The offline achievement wiki documents
`possible` and `happened` for custom achievements, plus optional ribbon data. It
documents no custom-achievement visibility field. The local vanilla
`common/achievements.txt` contains one `hidden = yes` occurrence, on the legacy
`vojtek_commander` achievement, and no trigger-valued visibility form. The
approved Kaiserreich custom-achievement file contains no `hidden` field or
dynamic visibility precedent. The shipped effect and trigger documentation
contains `has_completed_custom_achievement`, but no effect, trigger, or refresh
interface that changes an achievement definition's visibility.

| Local reference | Result |
| --- | --- |
| Offline `Achievement modding` page | `possible`, `happened`, and optional ribbon schema; no visibility trigger |
| Vanilla `common/achievements.txt` | one fixed `hidden = yes`; zero `visible` fields; zero trigger-valued `hidden` blocks |
| Vanilla effect and trigger documentation | completion query only; no reveal or visibility mutation |
| Kaiserreich `KR_achievements.txt` | zero hidden-achievement or staged-reveal examples |

The current implementation therefore preserves the only documented concealed
form, `hidden = yes`, and keeps each reveal flag inside `happened`. This prevents
premature route disclosure if the custom-achievement loader accepts the vanilla
scalar field, but cannot make the entry visible between public route reveal and
completion. Because the custom-achievement reference does not itself document
`hidden`, acceptance of that scalar also remains a local engine-reference check
rather than a proven custom-achievement contract. Replacing it with an invented
`visible = { ... }` or `hidden = { ... }` block would be an unsupported fallback
and is not done.

This is the sole source-schema gap in the 32-achievement package. Resolving it
requires either:

1. a verified engine schema or vanilla precedent for dynamic custom-achievement
   visibility; or
2. canonical approval to change A-22, A-27, and A-28 to either always visible
   with spoiler-safe wording or permanently hidden until earned.

### Engine-compatible staged-disclosure candidate

The narrowest interpretation that preserves concealment, the exact 32
achievements, and the exact three scripted GUI windows is:

1. Keep A-22, A-27, and A-28 as fixed `hidden = yes` custom achievements.
   Their unlock requirements, disqualifiers, history setters, and 96-file icon
   package remain unchanged.
2. Extend the existing Concealed Evidence Ledger window rather than creating a
   fourth GUI. Its registration may open when the hidden-evidence gate is
   active or when one of the three canonical public-reveal flags is present:
   `ireland_achievement_reveal_ailtiri_public_launch`,
   `ireland_achievement_reveal_royal_convention`, or
   `ireland_achievement_reveal_fivefold_convention`.
3. Reuse the existing A-22, A-27, and A-28 achievement sprites in three compact
   dossier entries. Each entry is invisible before its own reveal flag. After
   reveal it shows the final title, readable criteria, current dynamic values,
   unmet conditions, permanent disqualifiers, and completion state through
   scripted-GUI text and tooltips. No hidden route variable or unrevealed title
   is exposed.
4. When the window is opened only by a public-achievement reveal, use a
   context-aware `Public Achievement Dossier` title and hide the unrelated
   evidence rows. When the hidden-evidence gate is active, preserve the current
   Concealed Evidence Ledger title and evidence workflow. The underlying
   achievement menu remains fixed-hidden because the local engine contract
   provides no supported dynamic visibility field.
5. A-29 through A-32 remain permanently hidden as designed; no dossier entry is
   added for them.

This uses existing assets and an existing GUI surface, adds no fourth GUI, and
does not weaken an unlock condition. It is still a canonical interpretation:
the public in-game dossier, rather than HOI4's unsupported achievement-menu
visibility, becomes the staged reveal surface. The interpretation was accepted
and implemented in the 2026-08-03 non-live completion tranche; the current
source-level evidence is recorded in
`ireland_non_live_completion_audit_2026-08-03.md`.

## Historical result

The roster, eligibility, history tracking, disqualifiers, Northern safeguards,
localisation, and exact 96-file visual budget are complete at source level. The
documented engine schema does not provide dynamic menu visibility, and the
approved A2 ruling accepts the static-hidden implementation with the canonical
reveal conditions retained in `happened`; no unsupported field is claimed. Live
unlock testing is outside this goal's completion gate by user direction.

For the current authority state, the source-level A2 question is closed by the
static-hidden ruling above. The implementation claims no dynamic achievement
menu reveal behavior, and live in-game display testing remains outside the
completion gate. The accepted staged-disclosure interpretation is implemented
through the existing Concealed Evidence Ledger window: public reveal flags open
the window in dossier mode, individually reveal A-22, A-27, and A-28, reuse
their normal/grey/not-eligible sprites, and expose current German Leverage or
Northern integration stage in the dossier text and tooltips. A-29 through A-32
remain absent from the dossier.
