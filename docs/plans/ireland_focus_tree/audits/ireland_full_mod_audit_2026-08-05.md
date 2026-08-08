# Ireland Total Overhaul full-mod audit

Audit date: 2026-08-05

Scope: full source tree, focus graph, decisions and missions, scripted GUIs,
events, AI plans, probabilities, technologies, localisation, GFX registrations,
runtime icon surfaces, source-package evidence, and a direct executable parse.

This is the current audit record. Older audit documents remain historical
evidence and may contain earlier counts or earlier MCP revisions.

## Current inventory

| Surface | Current result |
|---|---:|
| National focus blocks | 211 |
| Focus roots | 1 |
| Focus connectors | 234 |
| Decision categories | 14 |
| Primary decision actions | 144 |
| Marine Service actions | 4 |
| Mission families | 54 |
| Top-level Ireland event IDs | 495 |
| Persistent spirit IDs | 106 |
| Registered spirit sprites | 93, with controlled reuse recorded in the crosswalk |
| Manifest rows | 169 |
| Manifest status | 166 complete, 3 blocked |

## Specialist audit wave

Six bounded specialist audits were run in parallel. Their findings were
consolidated rather than copied blindly:

- Focus/AI audit: hidden `has_completed_focus` gates were identified as a
  visibility/documentation warning; the convergence AI plan was missing its
  final chain; ordinary focus reward repetition was identified.
- Asset/GUI audit: manifest source paths and coverage-tool false negatives were
  identified; registration-only assets and the three exact portrait blockers
  were separated from runtime failures.
- Logic/event audit: stale election gates, unwritten invasion/route aliases,
  and the malformed targetless AI strategy entries were identified.
- Parliament/GUI audit: the GUI lifecycle contract, state coverage, and direct
  decision parity were checked.
- Decision/mission audit: the Marine Service repeatable reward loop, route
  archival visibility, missing AI PP hints, missing effect tooltips, and stale
  inventory comments were identified.
- Improvement-loop audit: source-of-truth drift, composite AI-plan ownership,
  and the missing live-runtime evidence boundary were identified.

## Repairs applied

1. Removed ordinary repeated material focus reward bundles while retaining
   route-opening milestones and capstones. The current source retains 40 shared
   reward-helper calls, including 24 capstone calls; no focus blocks were
   deleted.
2. Restored the convergence AI focus chain for
   `ireland_fivefold_obligation`, `ireland_otherworld_convergence`, and
   `ireland_convergence_order_capstone`.
3. Replaced the stale election decision gate with the canonical
   `ireland_reveal_category_elections` trigger.
4. Added daily compatibility projections for invasion danger, regional order,
   Celtic route, IRA route, government vacancy, and provisional Northern
   authority. Canonical route/profile/office flags remain authoritative.
5. Added state targets to the developmental factory-score and Northern
   invasion-unit AI strategies so neither is targetless.
6. Made the Atlantic protection decision one-time. Its 120-day active detail
   still expires, but the permanent completion flag prevents re-awarding
   Provision, Readiness, or Navy Experience after removal.
7. Added route-archive visibility guards to the Marine Service category and all
   four Marine Service actions, plus their four explicit `ai_hint_pp_cost`
   values.
8. Added effect tooltips for the seven parliamentary/institutional decisions
   that previously exposed requirements but not outcomes. The long H14
   internal label was removed from the player-facing wartime bargain
   description.
9. Added mutually exclusive ownership guards to the broad Congress, O'Duffy,
   and clerical/producer AI plans. Once a precise subprofile is selected, the
   composite plan aborts instead of competing for focus ownership.
10. Regenerated the asset crosswalk with dynamic counts, `textSpriteType`
    parsing, corrected spirit-prefix matching, and preservation-path fallback
    for cleared source evidence.
11. Updated current status and source-of-truth notes. Historical snapshots
    remain marked as historical; they were not silently rewritten.

## Verification results

### Local source and asset checks

- `audit_runtime_icon_surfaces.py`: `all_complete: true`; focus goals, law
  stages, route spirits, decision categories/actions, missions, mechanic
  ledgers, overlays, emblems, and flags all passed.
- Asset crosswalk regeneration completed with
  `focus=211 categories=14 actions=144 missions=54 spirits=106
  achievements=32 manifest=169`.
- `git diff --check` reported no whitespace errors. Only normal Git line-ending
  conversion warnings were emitted.
- No duplicate focus IDs, category IDs, decision IDs, mission IDs, or
  localisation IDs were introduced by the repair pass.

### MCP focus loop

The current Ireland national tree was inspected, rendered, and rasterized.
Ireland-owned diagnostics are clean:

- 211 focus nodes, one root, 234 connectors.
- 0 connector crossings.
- 0 node intersections.
- 0 long connectors.
- 0 same-row overlap pairs.
- Maximum horizontal connector span: 8 columns.
- Maximum vertical connector span: 4 rows.
- Maximum Manhattan span: 10.

The MCP also reports fourteen missing continuous-focus sprites and one missing
vanilla continuous-focus localisation. All are under `game:common/continuous_focus/generic.txt`,
not the Ireland mod, and were not patched into the mod as fake replacements.

### MCP scripted-GUI loop

The parliament panel was inspected and rendered at 1280x720 and 1920x1080
across normal, hover, selected, locked, disabled, warning, active, completed,
empty, full, minimum, maximum, long-text, and missing-localisation states.

- Source graph: passed.
- Visible overlap: not detected.
- Comparison and ancestor budgets: not blocked.
- State matrix: 14 states, 2 resolutions, 5 variants.
- Offline renderer limitation: live variable values remain unresolved and
  `gfx/FX/buttonstate.lua` is not executed; the source graph still contains the
  button-state binding and the direct executable parse did not report an error.
- One informational spacing diagnostic remains because the panel intentionally
  separates its status rows from the action stack by a larger prompt gap.

### MCP event, probability, and technology passes

- Ireland event namespace lint/render completed with zero blocking diagnostics.
  Workspace-wide event helper/lifecycle projections were deferred by the MCP
  large-workspace boundary; the linked report retains the full evidence.
- Probability adapter inventory passed: 11 adapters, 0 unresolved candidates,
  and 0 unresolved required inputs.
- Technology lint completed without blockers. The workspace-wide report covers
  552 technologies, 16 folders, 423 placements, 429 edges, and 717 unlocks;
  one unresolved item and deferred helper projections remain global tool-scope
  evidence, not an Ireland-local error.

## Direct executable check

`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\hoi4.exe`
was launched directly with `-debug`, without going through Steam. After the
mod was allowed to parse, the process was closed by PID. The resulting log was:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\logs\error.log`

Result: 0 lines, 0 bytes, and 0 Ireland-local error matches.

This validates executable parsing and registration loading. It does not claim a
fresh-save route playthrough, save/load cycle, AI simulation, or every GUI click
inside a live campaign.

## Remaining explicit boundaries

- P-26 Patrick Cogan, P-45 Mick Fitzpatrick, and P-55 Liam D. Walsh remain
  blocked because exact cleared source portraits were not supplied. No
  generated likeness or fallback portrait was substituted.
- Seven animation packages are registered as evidence/static-fallback surfaces;
  their live player-facing playback consumers remain a documented future asset
  verification item.
- Some source symbols, reports, and GUI sprites are intentionally retained as
  clearance or compatibility evidence when no live player-facing consumer is
  currently claimed. They are listed in the regenerated crosswalk rather than
  being deleted.
- Event preference flags and many hidden focus availability gates remain
  design-level audit warnings. They do not block parsing or the Ireland focus
  graph, but the audit does not claim that every optional AI preference hint has
  a live setter or that every hidden gate is represented by a visible connector.
- Fresh 1936/1939 route scenarios and AI simulations require an interactive
  campaign session; they are not represented as completed merely because the
  executable loaded with an empty error log.

## Disposition

No Ireland-local source parse error, missing runtime icon surface, focus-layout
blocker, GUI overlap blocker, or direct executable error remains in this audit
pass. The remaining items are either exact-source clearance blockers,
offline-MCP modelling limits, or explicitly marked live-play evidence gaps.
