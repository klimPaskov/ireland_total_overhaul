# Ireland Mechanics Hub Improvement Loop Handoff

Date: 2026-08-15
Subagent role: `hoi4_improvement_loop_planner`
Mode: Plan only
Parent feature: Ireland National Situation Ledger and focus-tree inlay

## Outcome

I recommend one bounded corrective implementation pass, not a broad expansion and not immediate closure. The six-family architecture is already deep enough. The remaining work is to make the current system truthful, accessible, and visibly interactive.

The implementation-ready addendum is:

- `docs/plans/ireland_mechanics_hub/improvement_loop/national_situation_ledger_corrective_addendum_2026-08-15.md`

No gameplay, GUI, localisation, asset, or specification file was edited by this subagent.

Concurrent implementation note: during the final handoff review, the parent implementation tranche had already moved the inlay to `x = -600, y = 10`, added persistent tab and row selector assets, and routed row click eligibility through row-visibility helpers. Keep the matching P0 sections as acceptance contracts and mark them implemented only after source review and the required focus and GUI evidence. The other P0 and P1 findings remain subject to the parent's final implementation review.

## Design problem

The dashboard successfully centralizes the six existing mechanic families, but several current presentation and access contracts fall short of the feature promise:

- The focus inlay physically occupies authored focus space.
- The hub can reveal Northern values before their dedicated ledger reveals them.
- Tab and row selection changes internal state without a persistent selected presentation.
- A selected value does not consistently name the currently binding consequence, gate, and next canonical route.
- Archived refresh controls can look usable while the shared helper intentionally no-ops.
- North and Culture summaries present lone variables beside statuses calculated from several independent conditions.
- Refresh wording is broader than the actual idempotent adapter.
- Current GUI review scenarios do not resolve and prove the critical interaction states.

## Classified findings

### P0

- `NSL-P0-01`: Move the inlay from `x = -720, y = 10` to the exact safe replacement `x = -600, y = 10`.
- `NSL-P0-02`: Mirror the dedicated Northern row reveal predicates in hub visibility and click eligibility.
- `NSL-P0-03`: Add persistent selected-tab and selected-row presentation.
- `NSL-P0-04`: Add a dynamic current consequence, binding gate, and next canonical route contract to the selected-row explanation.
- `NSL-P0-05`: Remove archived no-op affordances by sharing the open-state predicate with every calling control.
- `NSL-P0-06`: Add deterministic review scenarios for locked, bottleneck, partial reveal, evidence, archive, selection, disabled, and long-text states.

### P1

- `NSL-P1-01`: Replace the North and Culture inlay's misleading lone-number proxies with short public state or bottleneck phrases.
- `NSL-P1-02`: Narrow refresh wording to the displayed public report instead of claiming that every ledger is recalculated.

### Queued

- `NSL-Q-01`: Consider engine-safe navigation to an existing dedicated Northern or Evidence ledger only after P0 completion and only with a proven non-bypassing precedent.
- `NSL-Q-02`: Consider one small static selector strip only if existing assets and text treatment cannot express persistent selection.

### Rejected

- `NSL-R-01`: New spending buttons, meters, decision stores, or cloned canonical executors.
- `NSL-R-02`: New animation or background families.
- `NSL-R-03`: AI interaction with the human-only dashboard.
- `NSL-R-04`: Unrelated focus-route repair in this pass.
- `NSL-R-05`: Convenience exposure of concealed Evidence or unrevealed Northern values.

Every identified finding is assigned one of P0, P1, queued, or rejected in the addendum. There are no unclassified audit notes.

## Exact focus inlay handoff

Use:

```txt
position = { x = -600 y = 10 }
```

I resolved all 256 current focus positions. With the current 96-pixel horizontal and 130-pixel vertical spacing, the 460 by 248 inlay occupies `x = -600..-140` and `y = 10..258`. This is the empty top corridor between the cultural lane at `x = -8`, pixel anchor `-768`, and the economic lane at `x = 0`, pixel anchor `0`. Row 2 begins at `y = 260`.

Relevant neighboring focuses are:

- `ireland_cultural_survey` at absolute grid `-8, 0`
- `ireland_archival_record` at absolute grid `-8, 1`
- `ireland_economic_war_review` at absolute grid `0, 0`
- `ireland_rural_price_board` at absolute grid `0, 1`

Focus inspection evidence:

- workspace: `mod_ireland_total_overhaul_aaca88216c92`
- current inspection revision: `6e50c82578457bbc120701b8b831d54b40d73860d0f452c7bca68e205fc40cfb`
- layout hash: `dee813d687f55041d88e9456d9ce5d57ee2d5971763bf373b11bf55102b00c92`
- focus count: 256
- current connector count: 234
- current connector crossings: 0
- current node intersections: 0

The high-fidelity raster call did not yield consumable combined inlay evidence during this planning pass. The implementation pass must still produce a full focus-view image with the inlay present before claiming this P0 closed.

## Exact Northern progressive-reveal handoff

Mirror these predicates for both visibility and click eligibility:

| Row | Value | Predicate |
| --- | --- | --- |
| 1 | Unionist Consent | `has_completed_focus = ireland_northern_settlement_ledger` |
| 2 | Nationalist Consent | `has_completed_focus = ireland_northern_settlement_ledger` |
| 3 | Labour Cooperation | `has_completed_focus = ireland_northern_labour_social_bridge` |
| 4 | British Flexibility | `has_completed_focus = ireland_northern_trade_corridor` |
| 5 | Security Stability | `has_completed_focus = ireland_northern_local_authorities` |
| 6 | Integration Capacity | `OR = { has_completed_focus = ireland_northern_federal_preparation has_completed_focus = ireland_northern_unitary_preparation }` |

Keep overall access on `ireland_mechanics_hub_northern_visible`, which requires initialization, `ireland_reveal_category_northern`, and `ireland_northern_settlement_ledger`. The dedicated Northern ledger additionally uses `ireland_northern_claim_open` for its own window visibility. Do not weaken either surface's existing top-level contract.

## Research and precedent basis

I inspected the current specification, value-purpose matrix, implementation prompt, feature documentation, implementation files, localisation, asset manifest, and all three prior feature handoffs. I also used the required offline wiki pages, vanilla scripted-GUI and focus-inlay documentation, and vanilla focus-inlay precedents.

The relevant historical and regional connections are already present in the implementation. Dáil and Seanad procedure, small-state provision and maritime access, neutrality enforcement, the distinct Northern consent and administration conditions, and language, archive, regional, and stewardship institutions give the values their purpose. The addendum makes those connections visible. It does not introduce new historical claims, quotes, slogans, or audio needs.

Vanilla precedent families inspected for presentation shape include the German inner-circle inlay, Japanese influence inlay, Czechoslovak industry inlay, Australian campaign inlay, and Siamese Khana Ratsadon inlay. They support the compact, static, state-driven presentation. They do not justify a new gameplay mechanic.

## Implementation surfaces affected

Expected implementation surfaces are:

- `common/national_focus/ireland_focus_tree.txt`
- `common/scripted_guis/ireland_scripted_guis.txt`
- `common/scripted_triggers/ireland_mechanics_hub.txt`
- `common/scripted_effects/ireland_mechanics_hub.txt`
- `common/scripted_localisation/ireland_localisation.txt`
- `common/focus_inlay_windows/ireland_national_situation_inlay.txt`
- `interface/ireland_national_situation.gui`
- `interface/ireland_national_situation_inlay.gui`
- `localisation/english/ireland_l_english.yml`
- `docs/ireland_national_situation_ledger.md`
- `docs/specs/ireland_mechanics_hub/ireland_mechanics_hub_spec.md`
- `docs/specs/ireland_mechanics_hub/value_purpose_matrix.md`
- feature GUI review scenarios or manifests

No balance constants, costs, rewards, AI weights, event chains, decision families, or hidden reveal rules are authorized by this plan.

## Existing MCP review evidence

The full dashboard and focus inlay were inspected and rendered at 1920 by 1080 and 2560 by 1440. Current scenario data was intentionally insufficient to resolve all dynamic conditions, which is why the addendum makes deterministic scenarios a P0 rather than treating generic renders as proof.

Known review revisions from the implementation tranche are:

- full dashboard shared revision: `7566fda7b0b5211f9115af3d0ca7ad5a29e1f578726d0f90af2707986662257d`
- focus inlay shared revision: `9b9f84192d0d31a354e9ee4333933201547cde47dc2db6f15d36f8e6435ca563`

Current renders show no standalone inlay child overlap, but they do not prove placement inside the focus tree or mutually exclusive scripted status states. The implementation pass must use value-driven scenarios.

## Open questions

There are no open questions blocking P0 implementation.

Two optional questions are explicitly queued:

1. Does the engine and repository have a proven safe way to navigate from a selected hub row to the exact existing dedicated ledger without bypassing its visibility contract?
2. Can existing tab and row assets plus text treatment provide a persistent selected state, or is one small static selector strip required?

Neither question authorizes delay of the P0 work. The conservative implementation is explanatory text with existing assets.

## Prior addendum status

No earlier improvement-loop addendum exists for `ireland_mechanics_hub`. The existing files under `subagent_handoffs/` are repository mapping, scripted-system implementation, and inlay asset handoffs. Therefore this pass does not duplicate an unresolved previous addendum.

This addendum is now unresolved and must not be followed by another improvement-loop pass for the same feature until it is implemented, folded into the source specification, explicitly queued with a reason, or rejected with a reason.

## Promotion recommendation

Keep the addendum in `docs/plans/ireland_mechanics_hub/improvement_loop/` while any P0 or P1 item is unresolved. After implementation and review, promote the durable rules into the feature specification and value-purpose matrix, update `docs/ireland_national_situation_ledger.md`, and record the addendum as implemented or superseded.

After those corrections pass the named scenario matrix, stop expanding the feature. Remaining work should be final localisation review, asset handoff verification, focus and GUI audit reruns, and cleanup. A new mechanic family would be bloat.

## Subagent completion statement

Completed:

- repository, specification, documentation, implementation, localisation, asset, and prior-handoff inspection
- required offline wiki, vanilla documentation, and vanilla precedent review
- focus and GUI evidence review
- one bounded improvement addendum
- one parent handoff

Blocked:

- none for planning

Uncertainty:

- combined focus-tree raster evidence with the inlay must be produced during implementation
- safe cross-category navigation remains queued pending a proven engine precedent

Simplifications or omissions:

- No gameplay changes were made because this subagent is plan-only.
- No new visual or audio package was requested because the identified defects do not require one.
- No external historical research package was opened because this pass adds no new historical content or claims.

## Integration closure appended 2026-08-15

This plan-only handoff remains a historical record of the corrective recommendation. The parent implementation and documentation pass now support closure of the P0/P1 contracts:

- the source specification and value-purpose matrix are marked implemented, and the durable corrective rules are carried into `docs/ireland_national_situation_ledger.md`;
- focus inspection revision `90beeec44304c287` records 256 focuses, 234 connectors, and zero crossings, node intersections, long connectors, or too-close pairs;
- dashboard and inlay GUI inspection revisions `5cfb9c81e35e17db` and `7f7b1126f87a3ebc` report no blockers at 1920x1080 and 2560x1440;
- the older planning revision `6e50c82578457bbc120701b8b831d54b40d73860d0f452c7bca68e205fc40cfb` and its unresolved-P0 wording remain historical and are superseded by the frozen evidence above;
- `NSL-Q-01` remains queued because no cross-category navigation control was added. Existing static selection markers supersede the need for `NSL-Q-02`.
