# Ireland authority rulings: M2, A2, and C3 approval

Date: 2026-08-01

This document records the project-owner decisions for the final Ireland
implementation tranche. It supersedes earlier pending-review notes for these
three decisions only.

## M2: mission-family merge

M2 is accepted and implemented. The feature keeps exactly 13 decision
categories, 140 actions, and 54 mission families.

- The by-election mode now launches the base Conduct a Free General Election
  mission with `ireland_election_mission_by_election_mode`. Its deadline
  is 100 days; the ordinary general-election mode remains 105 days.
- The parish-audit mode now launches the base Keep Essential Services Running
  mission with `ireland_service_mission_parish_audit_mode`. Its deadline
  is 120 days; the ordinary essential-services mode remains 60 days.
- The freed mission ordinals are now the Radical/Underground families
  Consolidate the Movement Network (006) and Secure Constituent Authority
  (009), physically nested under the Radical/Underground decision category.
  Each has named map objectives, mode-specific thresholds, full and partial
  success, failure, escalation, cancellation, and AI handling.
- The old standalone mission identifiers are no longer active mission
  definitions, activation/removal targets, sprite names, or standalone
  localisation entries. The merged missions retain mode-specific by-election
  and parish-audit objective, requirement, and durable-result keys so those
  outcomes remain distinct and auditable.

## A2: hidden achievements

A2 is accepted. Achievements A-22, A-27, and A-28 retain static
`hidden = yes` declarations and their existing earned/reveal conditions in
`happened`.

The implementation does not add an undocumented dynamic visibility key. This
keeps the achievement file within the locally documented vanilla schema while
concealing the three achievements until their canonical route milestones are
reached.

## C3: source-package approval

The project-owner approval covers all 60 C3 entries that were previously
marked `needs_user_review`. The subsequent explicit approval also covers the
conditional local-mod promotion of S-24, S-27, and the eight exact event/news
rows in `assets/source_research_handoffs/event_news_user_approved_conditional_2026-08-01.md`.
The source manifest records the promoted packages as `complete`, with final
DDS paths and SHA-256 hashes, and registers their sprites in
`interface/ireland_sourced_assets.gfx`. The conditional packages retain
their attribution and object-use boundaries and are not represented as C4 or
unrestricted redistribution permission.

The follow-up EV-SRC-055 package uses the exact-period Houses of the Oireachtas
scan of the Constitution (Consequential Provisions) Bill 1937, Bill No. 41a,
as passed by Dáil Éireann. It is a conditional C3 document promotion, not an
invented facsimile or a silent generic substitution. The modern eISB Act No.
40 HTML remains supporting legal text, while the source-derived bill scan is
the runtime visual. Its licence conditions and hash are recorded in
`assets/source_research_handoffs/EV055_Oireachtas_clearance_2026-08-01.md`.

The follow-up EV-SRC-059 package uses the exact UWM/AGSL Admiralty Chart 1765
scan for Cork Harbour. Its chart title records the 23 January 1891 Admiralty
publication after an 1888 survey; UWM also retains the 1898/BA 1765 1898
catalogue record. The underlying UK government work is recorded as public
domain, while UWM’s reuse guidance supplies the required source credit and
conditional C3 boundary. The chart is a geographic flavour-family context
object, not a facsimile of the separate 1941 claim record. Its handoff is
`assets/source_research_handoffs/EV059_UKHO_chart_clearance_2026-08-01.md`.

The approval-time manifest distribution recorded by this ruling was:

- C3 complete: 93 (including the user-approved conditional tranche and the
  dated EV-SRC-055 and EV-SRC-059 follow-up packages)
- C3 still unpromoted: 0
- C2 review: 0 in the 169-row manifest; the separate Daniel Morrissey route
  extension is complete under conditional C3 local-mod scope outside that
  manifest, with NLI and Wikimedia credits retained
- C1 blocked: 27
- C2 blocked: 18
- C4 complete: 31
- Total source-budget entries: 169

The current source-of-truth status superseding that approval-time snapshot is
132 complete and 37 blocked, with C1/C2/C3/C4 distributed as 20/17/101/31.
No manifest rows are currently `needs_user_review`; the remaining 37 rows are
the separately audited external source-clearance blocker.

The 45 C1/C2 blocked manifest entries were not replaced by generated or
fallback art. Source bytes and the preserved leader-portrait packages remain
under `docs/portraits`; runtime DDS files are under the standard feature
`gfx/` roots.

## Validation scope

The user explicitly excluded live in-game testing from completion. This ruling
therefore covers static source, manifest, GFX, mission-count, localisation,
and cleanup checks only; it makes no claim of a running HOI4 session.

## Post-approval static repairs

The follow-up Dillon audit added a distinct
`ireland_dillon_named_vote_gate`: the invasion-danger exception remains
available only to the final war-entry gate, so it cannot synthesize the named
Dail assent. The named vote is written by the explicit event option and is
cleared only by route cleanup. The ten promoted event/news packages also gained
concrete consumers; the crosswalk and evidence are recorded in
`audits/ireland_event_source_consumer_repair_2026-08-01.md`. The later
EV-SRC-055 Oireachtas clearance handoff adds its H01 constitutional-event
consumer without changing the canonical event-family inventory.
