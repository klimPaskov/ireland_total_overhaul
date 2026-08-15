# Natural Cabinet Briefing correction

Date: 2026-08-15
Status: implemented and promoted into `docs/specs/ireland_mechanics_hub/`; final evidence is recorded in the feature completion report
Supersedes: the six-tab, 34-record interaction model in `national_situation_ledger_corrective_addendum_2026-08-15.md`

## Player problem

The implemented National Situation Ledger behaves like a diagnostic inspector. It asks the player to choose among six system tabs, select from as many as seven internal records, read separate purpose, status, consequence, and next-action sentences, and manually refresh cached projections. That is too much bookkeeping for a normal HOI4 country mechanic and makes existing systems feel artificial.

The correction keeps the underlying ledgers authoritative but exposes only decisions a cabinet could plausibly discuss. It removes the expectation that every internal component must be permanently visible.

## Accepted player-facing model

The decision-category scripted GUI becomes a compact **Cabinet Briefing** with four strategic cards:

1. **Government** — the constitutional/parliamentary programme and the government's ability to act.
2. **National Supply** — the existing Provision aggregate; component details remain in its tooltip and native decisions.
3. **Defence Readiness** — the existing Readiness aggregate; service details remain in its tooltip and native decisions.
4. **National Question** — the current Northern settlement stage and its active policy direction.

The panel shows one short cabinet assessment. It does not show permanent Foreign Pressure or Culture/Evidence rows. Those systems already have focuses, decisions, events, and dedicated ledgers; they appear contextually in tooltips and alerts when they become relevant.

The panel has no tabs, row selectors, selected-row markers, manual refresh, purpose heading, consequence heading, or debug-like language. It has at most one contextual button. The button is visible only when it delegates to an existing canonical action:

- the next guarded parliamentary programme step; or
- a currently valid Northern review request.

If neither action exists, the briefing is informational and no disabled decorative button is shown. AI continues to use the native decisions and never clicks the GUI.

## Focus-view inlay

The focus inlay remains, but becomes a compact strip rather than a second dashboard. It shows Government, Supply, and Defence plus a conditional National Question alert. It contains at most one contextual programme button and no refresh button.

The inlay must stay in an empty focus-tree corridor and must not overlap any focus node or connector after the final focus reflow.

## Text contract

All visible prose is in-world cabinet language. Do not use phrases such as “what this value does,” “consumer,” “selected row,” “refresh projection,” “binding gate,” “internal value,” or “mechanic family.”

Tooltips answer three questions naturally and compactly:

- What is the present condition?
- What part of government policy is affected?
- Which existing decision or focus can improve it?

No card tooltip may exceed six short lines in the normal state.

## Focus effect tooltip contract

Internal route-profile synchronisation, mass idea replacement, clamps, cache rebuilds, cosmetic-tag reconciliation, and mission-counter rebuilding are hidden effects. A focus shows its authored `*_reward_tt` plus genuinely material public effects only. In particular, `ireland_refresh_exceptional_route_state` must never expand into the full list of every removable Governing Order, Organised Society, or security spirit.

## Layout and focus integrity contract

- no orphan, isolated, or unintended dangling focus;
- no connector crossing, connector-through-node, or long connector;
- no hidden `available` relationship may create a visually misleading detached branch;
- all 28 branch families remain visible from the start;
- exactly the existing three opening trunks remain;
- search filters describe direct rewards or the focus's actual playable function, including territorial-expansion filters on Northern reclamation/territorial settlement focuses.

## Error correction contract

All mod-owned errors in the user-supplied error attachments are audited against current source. Already-corrected errors are recorded as closed. Remaining Ireland-owned parser, trigger, mutual-exclusion, scripted-localisation, or flag-format errors are fixed. Errors originating in unmodified vanilla country/history files are not overridden by this country mod.

## Acceptance

- four strategic cards, no tab or row-selection UI;
- zero manual-refresh controls;
- at most one visible contextual action per surface;
- no oversized internal-cleanup effect tooltip;
- focus inspector and rendered tree agree on zero orphan/long/crossing defects;
- GUI inspection/render at 1920x1080 and 2560x1440 has no overlap or dead click region;
- every visible key resolves and uses natural in-world language;
- every supplied Ireland-owned error is closed or identified as already corrected;
- no fallback art or placeholder UI is introduced.
