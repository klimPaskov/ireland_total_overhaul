# Ireland intelligence admission gate tranche — 2026-07-25

Feature slug: `ireland_focus_tree`

Status: source-level implementation tranche; live engine and scenario evidence remain open.

## Canonical rows addressed

The decision and mission map gives the G2 liaison action two separate proofs: a valid foreign partner or Northern plan, and an Irish-controlled information channel with exposure and review rules. The foreign-agent action requires an identified agent and legal authority. A generic intelligence readiness value is not sufficient for either row.

## Implemented source changes

- Added `ireland_g2_partner_or_northern_plan` to `common/scripted_triggers/ireland_triggers.txt`.
- Added `ireland_g2_liaison_authority`, requiring the channel/plan proof plus sovereignty-and-review safeguards or Security Under Law.
- Added `ireland_foreign_agent_case_ready`, requiring the active intelligence incident family plus Security Under Law or the National Emergency legal order.
- Wired `Open a G2 Liaison Channel` to the liaison-authority trigger.
- Wired `Turn or Intern a Foreign Agent` to the foreign-agent-case trigger.
- Updated the two action descriptions and requirement tooltips so the live gate is readable before the player pays the existing physical and power costs.

## Boundaries

These triggers do not grant intelligence, access, leverage, equipment, units, territory, cores, offices, recognition, alignment, or diplomatic status. The G2 action still consumes its authored Support Equipment and power burden; the agent action still consumes its security staff and intelligence burden. Existing partner lifecycle cleanup remains authoritative for foreign channels.

## Static evidence

- Each new scripted trigger is defined once and consumed once by its owning action.
- The partner checks reuse the existing GBR/USA/GER/ITA validity triggers and do not create a new actor family.
- The legal flags are already produced by the Security Under Law focus and National Emergency runtime.
- Localisation remains UTF-8 with BOM after the edit.

## Remaining proof

No HOI4 process was launched. Fresh 1936, channel-capitulation, Northern-plan, intelligence-incident, legal-order, failed-case, route-cleanup, AI, and GUI scenarios remain not-run. This tranche does not close source clearance or the overall Ireland completion gate.
