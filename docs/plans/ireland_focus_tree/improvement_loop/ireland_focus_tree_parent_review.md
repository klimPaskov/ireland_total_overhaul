# Ireland Focus Tree Parent Review

Feature slug: `ireland_focus_tree`

Review type: parent-agent improvement review

Status: completed, but not a substitute for the required `hoi4_improvement_loop_planner` execution

## Overall judgment

Broad expansion is no longer recommended. The six-part design already covers political routes, economy, defence, neutrality, diplomacy, Northern Ireland, decisions, events, lifecycles, AI, achievements, assets, research, hidden content, failures, recovery, conclusions, and implementation ownership at a scale where additional mechanics would add maintenance burden and repetition.

The remaining useful work is canonical closure. It consists of repairing omitted authoritative ledger sections, clarifying a few route-to-conclusion links, establishing source precedence, writing the implementation prompts, and validating the package. The review therefore recommends a closure handoff after the findings below are integrated.

## Findings

### IL-001: promised AI overlays were absent from the AI matrix

Evidence:

- `project_status.md` records exactly ten temporary overlays.
- The Part 6 AI matrix previously contained only the 30 durable profiles.

Consequence:

Implementation could either duplicate profiles for temporary states or ignore election, emergency, shortage, war, occupation, sponsor-collapse, office-vacancy, postwar, and conclusion priority shifts.

Required resolution:

Add OV-01 through OV-10 to the authoritative AI matrix with activation, priority, exit, cleanup, and hard limits.

### IL-002: promised foreign response action classes were absent

Evidence:

- Part 6 status records twelve primary response action classes.
- The foreign matrix previously contained actor families and score bands without an exact action-class registry.

Consequence:

Implementation could produce inconsistent response types, hide severe actions in digests, or grant material responses to incapable actors.

Required resolution:

Add RC-01 through RC-12 with score bands, capability rules, persistence, and visibility requirements.

### IL-003: promised source-clearance workflow was absent

Evidence:

- Part 6 status records five clearance states, source hierarchy, and per-item manifests.
- The asset ledger previously began directly with the portrait roster.

Consequence:

Catalogue discovery could be mistaken for permission, and sourced assets could enter production without rights, provenance, or credit records.

Required resolution:

Add C0 through C4, eleven source tiers, and the complete per-item manifest contract.

### IL-004: Serious Cultural Stewardship could displace a government profile during ordinary cross-route play

Evidence:

- AI-12 previously activated whenever the public cultural lane was active under any lawful government.
- The AI model defines one durable route profile plus temporary overlays.

Consequence:

A de Valera, Labour, coalition, or other government could lose its political strategy merely because it funded archives or language work.

Required resolution:

Reserve AI-12 for a government whose primary national programme is public cultural stewardship. Keep ordinary cross-route cultural investigation and reveal work under the current host profile and its normal Culture category priority.

### IL-005: final convergence lacked a clear Part 5 conclusion-family mapping

Evidence:

- AI-30 and A-32 define the Fivefold High Kingdom of Two Irelands.
- The Part 5 conclusion table had an Otherworld row but did not name the final convergence variant.

Consequence:

Implementation could treat convergence as a cosmetic reveal, skip the 180-day consolidation process, or add an unbudgeted conclusion family.

Required resolution:

Expand the existing Otherworld conclusion family to include the final convergence as its highest gated variant. Keep the fixed conclusion-image family count stable.

### IL-006: support profiles lacked one canonical conclusion registry

Evidence:

- Clann na Talmhan, constitutional vocationalism, serious culture, and emergency restoration have durable AI treatment but do not all create separate sovereign regimes.
- Their valid host conclusions were spread across several specifications.

Consequence:

Implementation could invent free regime conclusions or leave these profiles without a finish state.

Required resolution:

Create the 30-row route coverage matrix and identify a separate conclusion or lawful host conclusion for every profile.

### IL-007: source precedence was implicit

Evidence:

- Six specifications, nine maps, eight existing matrices, four prompts, and cumulative research overlap by design.
- No file stated how an implementation agent should resolve overlapping detail.

Consequence:

Later summaries could be treated as silent overrides, and exact matrices could be ignored in favour of broad route prose.

Required resolution:

Create the canonical index and reconciliation map with explicit precedence and surface ownership.

### IL-008: implementation dependency order was scattered

Evidence:

- The package defines all required systems but their build order was spread across part interfaces and prompts.

Consequence:

Implementation could begin with focus rewards or event text before identifiers, values, cleanup helpers, country state, and route gates exist.

Required resolution:

Add one dependency sequence to the reconciliation map and the complete coding prompt.

### IL-009: the prior Part 6 validation report overstated confidence

Evidence:

- A rerun of the available Part 6 validation script found missing action classes and source-clearance sections.
- The old report recorded zero failures.

Consequence:

Development history could be mistaken for current completion evidence.

Required resolution:

Keep the old report as supporting history, mark it superseded for final confidence, and make Part 7 validation authoritative.

### IL-010: local engine references remain unavailable

Evidence:

- The offline Paradox wiki and local Hearts of Iron IV installation named by `AGENTS.md` are not mounted.

Consequence:

This planning package cannot validate engine syntax, exact GUI support, focus loading, achievement wiring, or local vanilla precedent.

Required resolution:

Queue the reference audit to the implementation owner before code changes. Do not simplify a mapped system because the references are currently absent.

### IL-011: final implementation and goal prompts were missing

Evidence:

- Four specialised prompts existed, but no complete coding prompt or sub-4,000-character goal prompt existed.

Consequence:

An implementation agent would need to infer ordering and global completion gates.

Required resolution:

Create both prompts and make the coding prompt the coordinator rather than a duplicate owner of specialised work.

### IL-012: the final package inventory was not classified

Evidence:

- Backup copies, continuation prompts, old validation files, and checkpoint manifests coexist with canonical sources.

Consequence:

A final archive could include stale or contradictory files.

Required resolution:

Classify every file as canonical, supporting, superseded, or temporary. Exclude backups and old checkpoint history from the canonical source package.

## Closure handoff

After IL-001 through IL-012 are resolved, no broad mechanic, route, country package, GUI surface, asset family, achievement family, or event family should be added. Remaining work is limited to:

- actual execution of the named improvement-loop subagent
- classification of any returned findings
- final local engine-reference audit during implementation
- final validation rerun and archive naming

Additional route or mechanic expansion would duplicate existing systems and make implementation less reliable.
