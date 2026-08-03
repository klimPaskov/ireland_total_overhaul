# Radical and Underground mission-capacity gap

Date: 2026-07-26

## Evidence

The canonical roster in `docs/specs/ireland_focus_tree/maps/ireland_focus_tree_decision_and_mission_map.md` reserves two active slots for Radical and Underground Transition: one organisational mission and one seizure or constituent mission. The same document and Part 5 fix the total at exactly 54 mission families.

Current source has the required ten Radical and Underground actions in `common/decisions/slopx_ireland_decisions.txt`, but no `slopx_ireland_mission_*` block inside `slopx_ireland_radical_underground`. The measured implementation remains exactly 54 missions because all current families belong to the other twelve categories.

## Why this is not a small patch

Adding the two implied radical missions would increase the fixed total to 56 unless the parent deliberately replaces or moves two existing canonical mission families. That decision changes pacing, capacity, route integration, outcomes, AI, and localisation across the fixed 13/140/54 contract. It is outside a narrow audit repair.

## Parent decision needed

Choose one of the following before implementation:

1. Treat the two Radical slots as conditional future capacity only, then amend the canonical category roster and Part 5 text to say that this category currently has no mapped timed mission family.
2. Preserve the two Radical mission slots as binding design. Select two existing mission families to retire, merge, or move so the total remains exactly 54, then specify the Radical organisational and constituent or seizure objectives, named locations, material or capacity commitments, full/partial/failure/escalation outcomes, AI route gates, and route-closure cleanup.

No gameplay source, localisation, GUI, or asset change is made by this handoff.

## Exact 54-preserving implementation candidate

The least destructive binding interpretation is to retain every canonical
objective while consolidating two mission families whose scope is already a
strict subcase of another family:

1. Fold `Maintain Cabinet Discipline` into `Complete the Six-Month Settlement
   Review` as its Cabinet-discipline phase. `Convene a Cabinet Cohesion Review`
   still launches a timed objective, but it launches the shared settlement
   review family with a Cabinet-phase flag, the 90-day deadline, the current
   Dublin/Social Consent objective, and its existing full, partial, failure,
   escalation, AI, and cleanup outcomes. `Review the Six-Month Settlement`
   launches the same family with the full-review phase and its existing
   180-day contract.
2. Fold `Protect a By-Election` into `Conduct a Free General Election` as its
   named-constituency variant. `Prepare a By-Election` still launches a timed
   objective, but it launches the shared election family with the
   by-election-variant flag, the existing 100-day South and Southeast/state
   135 objective, and its existing result and cleanup contract. `Update the
   Electoral Register` retains the national-election variant and its existing
   deadline and safeguards.

This frees exactly two family identifiers while preserving 140 actions, all
four action-to-objective relationships, all current named places and deadlines,
and the exact 54-family ceiling.

The replacement Radical families would be:

| Family | Launching action variants | Named objective surface | Deadline | Result contract |
| --- | --- | --- | ---: | --- |
| `Organise the Radical Movement` [proposed] | `Audit the Republican Commands`, `Rebuild the Republican Congress`, `Reassemble the National Corporate Party`, `Organise Ailtirí Cells`, and the valid clerical/producer capture variant | IRA commands in Dublin and the Border Belt; Congress delegates in Dublin, Cork and the industrial regions; O'Duffy branches in Dublin and Leinster; Ailtirí cells in Connacht and the Western Seaboard; clerical/producer councils in the named service regions | 120 | full organisation records a route-specific mandate; partial records a divided or exposed organisation and opens remediation; failure dissolves or fractures the network; escalation opens the matching political crisis; cancellation and route cleanup remove cells, delegates, branch, council and temporary-capacity flags |
| `Secure the Radical Transition Mandate` [proposed] | `Convene the Convention of Commands`, `Create a Civil Republican Directorate`, `Ratify the Common Programme`, `Impose Compulsory Estates`, `Launch the Ailtirí Party State`, and the valid clerical/producer seizure or constituent variant | IRA convention or civil mandate in Dublin; Congress constituent vote across its delegate regions; O'Duffy authority and estates in Dublin/Leinster; Ailtirí public launch in Dublin after the dated Connacht cell gate; clerical/producer return or retention through its lawful bodies | 180 | full success authorises only the route-specific transition gate; partial success creates a conditional mandate and a dated recovery requirement; failure blocks seizure or constituent authority and records the route failure; escalation fires the matching crisis/foreign-reaction handoff; cleanup removes provisional commands, delegates, estates, launch bodies and temporary offices without granting free territory, cores, industry, equipment, units, alignment, recognition or office |

Both families use the existing Radical category cap of two and the global
8/10/conditional-12 capacity helpers. They are mutually variant-driven: only
the active route's named objective, text, map checks, AI profile, outcome flags,
and cleanup run. Historical AI retains zero Ailtirí commitment weight before
the dated public gate. Neither family is a passive variable timer or a
one-click political transformation.

This candidate remains parent-policy material. It is not an accepted canonical
amendment until the user authorises the consolidation.

## Planner status

No new improvement-loop planner was spawned. The existing Ireland improvement loop still has partial and blocked findings recorded in `docs/plans/ireland_focus_tree/improvement_loop/ireland_focus_tree_finding_disposition.md`, and repository guidance forbids stacking another planner pass before those findings are disposed.
