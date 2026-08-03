# Ireland decision and mission audit — 2026-07-22

Feature slug: `ireland_focus_tree`

This is an implementation follow-up to the canonical decision/mission map and the independent decision-mission audit. It records source-level repairs; it is not a claim of engine or scenario completion.

## Proven inventory

- 13 decision categories, 140 action decisions, and 54 mission families remain present.
- Every authored action has a dynamic cost trigger/text pair and an AI block.
- Every mission has a named map objective, timer, cancellation trigger/effect, timeout effect, complete effect, full/partial/failure/cancellation/escalation result paths, and AI block.
- The static objective inventory is 54/54 and no mission objective wrapper aliases one of the generic map predicates.

## Repairs recorded

- The 54 mission objective wrappers now carry mission-specific state, building, railway, ledger, route, or actor conditions. The Dublin–Belfast railway objective remains reserved for the actual corridor mission.
- British supply delivery now targets controlled Dublin port and infrastructure with the British channel and GBR validity. It no longer requires Irish control of state 119.
- Cross-border health now targets Dublin infrastructure plus the Northern contact/trade-corridor state rather than a generic Dublin administrative check.
- Campaign-wide escalation is limited to national emergency, route failure, Northern settlement failure, or war. An unrelated foreign-reaction window or neutrality incident no longer escalates every mission timeout.
- The five foreign channels used by decisions are opened by their corresponding focus gates: British leverage management, American diaspora mission, Vatican mediation, foreign safeguards/neutral states, and the German channel.

## Remaining audit boundary

- Physical stockpile/manpower costs are present on the major provision, readiness, defence, transport, and merchant-fleet actions. The rest of the action surface uses dynamic political-power/command-power scarcity and burden costs; this remains a balance review item rather than a passive resource store.
- GUI click bindings, mission timer behaviour, event presentation, initial map state, and AI scenario behaviour still require the local engine/scenario suite. HOI4 was not launched for this audit.
