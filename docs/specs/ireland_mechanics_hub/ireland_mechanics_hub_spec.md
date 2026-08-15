# Ireland Cabinet Briefing specification

Status: accepted correction implemented and independently audited complete.

## Player experience

The Cabinet Briefing is a compact decision-category summary and national-focus inlay. It gives the player a cabinet-level reading of four matters without exposing every internal ledger variable:

1. Government: a qualitative judgement of the parliamentary programme and governing authority.
2. National Supply: the existing Provision aggregate.
3. Defence: the existing Readiness aggregate.
4. National Question: a qualitative judgement or the active Northern settlement stage.

Foreign leverage, culture, evidence, exceptional-route obligations, event previews, dispatch cursors, temporary calculations, dirty counters, and component caches remain in their existing focuses, decisions, events, and dedicated ledgers. They are not permanent dashboard rows.

## Presentation contract

- The interface is a 460 by 248 cabinet paper with four distinct category emblems.
- Each card has one short colour-coded state and a compact tooltip written as ordinary policy language.
- Only National Supply and Defence show public aggregate numbers.
- There are no tabs, row selectors, purpose/consequence headings, manual refresh controls, or diagnostic language.
- The panel has one short assessment line that identifies the cabinet's immediate concern.
- The informational focus inlay uses the same four-card vocabulary and occupies an empty authored corridor.

## Action contract

At most one button is shown. It delegates to the next existing guarded Parliament executor in canonical order: Dáil, Seanad, Confidence Pact, then Joint Budget. The executor repeats every normal requirement and cost. If no programme step is presently available, the button is absent instead of being displayed as a decorative disabled control.

The briefing never grants a ledger value, route step, focus completion, resource, or alternate AI path. AI continues to use native decisions and focus plans.

## State and lifecycle

- Government, Supply, and Defence are represented after Ireland's normal initialization, with locked wording until their authored records open.
- The National Question is `Unopened` until its existing Northern route becomes public.
- Active states use restrained colour in their ordinary state text; the briefing does not add a second layer of status seals.
- Route archival leaves an informational record and removes the contextual action.
- Dirty refreshes come from the systems that already mutate the underlying state; there is no player-facing refresh action.

## Tooltip contract

Tooltips state the present condition, the policy area affected, and the existing decision or focus family that can improve it. They must not describe implementation concepts such as consumers, cached projections, selected rows, internal values, or binding-gate plumbing.

Internal exceptional-route profile synchronization is wrapped in `hidden_effect`. Focus cards expose their authored reward tooltip and material public effects, not the complete list of every removable route spirit.

## Assets

- Decision category: `GFX_decision_category_ireland_national_situation`.
- Background: `GFX_ireland_mechanics_hub_inlay_background`.
- Card emblems: the existing Government, Provision, Readiness, and Northern decision-category sprites.
- Existing project status seals remain available to other interfaces but are not part of the Cabinet Briefing.
- Action: `GFX_ireland_gui_parliament_step_button`.

The former selected-tab and selected-row assets are retained only as superseded source evidence. They are not active interface elements.

## Acceptance

- four cards and no additional permanent values;
- only two public numeric aggregates;
- no tabs, row selection, or refresh;
- no dead or bypassing action;
- no oversized internal-cleanup focus tooltip;
- no focus orphan, crossing, connector-through-node, or long connector;
- focus inlay does not cover a focus or connector and contains no permanently grey control;
- player-facing text resolves and remains natural policy prose;
- no placeholder or fallback art.
