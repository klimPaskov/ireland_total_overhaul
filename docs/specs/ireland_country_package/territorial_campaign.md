# Ireland Country Package — Territorial Campaign

## Architecture repair

The existing territorial focus island is replaced by a connected campaign lane.
It does not create a fourth opening trunk.

```text
National Settlement
        |
The Unfinished National Question        (visible foreshadowing)
        |
Northern Contacts + Foreign Safeguards + Provision + Readiness
        |
Define the National Question             (campaign gateway)
        |
Authorize Instruments                    (decisions and ledger)
        |
route-specific Northern method
        |
Northern outcome / refusal / crisis
        |
Atlantic Policy                          (route-specific, not always expansionist)
        |
operations, escalation, occupation, settlement
```

The foreshadowing focus sits below politics and visually points toward the
territorial lane. It names the four proof families still required. The politics
shortcut centres far enough right to include the National Question gateway; the
branch may add a navigation shortcut only if the total visible shortcut count
remains three by merging or retargeting an existing shortcut.

## Stage 1: Northern evidence and preparation

The Northern Settlement Ledger tracks:

- nationalist legitimacy;
- unionist consent/resistance;
- labour and social support;
- British leverage;
- security exposure;
- administrative integration.

Projects gather contacts, border information, customs evidence, labour/church
links, industrial dependencies, and British response. Values are shown, not
hidden helper variables.

## Stage 2: family methods

### Democratic — supervised settlement

- negotiate guarantees with Britain and local communities;
- run a timed plebiscite preparation mission;
- protect campaigning, register voters, and prevent coercion;
- accept partition, negotiate federal safeguards, or implement lawful transfer.

No success is guaranteed. Failure may preserve partition while improving
relations, or create a later constitutional reopening.

### Congress socialist — all-island workers' campaign

- build cross-border union and tenant networks;
- supply political organization, not free divisions;
- choose labour federation, workers' plebiscite, or revolutionary escalation;
- manage unionist workers, clerical opposition, Britain, and armed factions.

### Blueshirt authoritarian — Ulster ultimatum

- mobilize border forces and demonstrate readiness;
- issue a target-country demand event;
- process acceptance, counteroffer, or refusal;
- unlock border enforcement only after refusal and a fresh material check.

### Producer-estate — Belfast compact

- use customs, credit, industrial procurement, and port access;
- bargain with Belfast industry and Britain;
- accept commercial association, protectorate-style access, or a broader compact;
- failure harms credit, trade, and producer support.

### Restoration — crown and province mandate

- secure provincial assent and constitutional legitimacy;
- negotiate local guarantees and a symbolic place for Ulster;
- reject automatic royal claims: the mandate must be accepted or enforced through
  the same diplomatic/material safeguards as other coercive routes.

## Stage 3: Atlantic policies

Not every family is expansionist:

- democratic: security compacts, guarantees, basing/access, no conquest lane;
- socialist: support Scottish/Welsh republican movements and release subjects;
- fascist: staged claims on 120, then 122/123 after naval proof and refusal;
- oligarchic: concessions, leases, protectorates, customs access;
- restoration: Dál Riata claim on state 120 after legitimacy conclusion.

State scope is fixed to 119 Northern Ireland, 120 Scottish Highlands, 122 Wales,
and 123 Cornwall. No Isle of Man state is invented.

## Material enforcement gate

Every coercive operation checks at launch and completion:

- peace and no active territorial demand;
- Dublin controlled and Dáil majority/valid authoritarian replacement;
- readiness conclusion;
- centralized minimum manpower, infantry equipment, support equipment, convoys,
  fuel, and command power;
- target exists, controls the state, and is not an ally/subject/faction partner;
- favourable alliance and target strength ratios;
- naval reach for Wales/Cornwall;
- recorded diplomatic refusal.

Cancellation refunds only the documented unspent administrative portion. It does
not restore consumed equipment or erase foreign reaction.

## Target response and foreign reaction

Every demand saves requester, controller, and state targets, then fires a target
event with accept, counteroffer, and refuse choices. Target AI weighs relative
strength, faction backing, war, opinion, guarantees, and the demanded outcome.
Every terminal option clears pending flags and event targets and applies a shared
cooldown. Stale controller changes resolve safely.

## Occupation and settlement

Territory is recorded per holding. Each controlled state/subject relation must
receive one outcome:

- withdraw or release;
- protectorate/subject with reconstruction obligations;
- local rights charter with resistance/compliance review;
- long integration review where the route permits it.

No external core is automatic. Northern core review remains a final high-stage
settlement requiring control, compliance, legitimacy, and completed integration.
The Atlantic conclusion is blocked until all relevant holdings are resolved.

The conclusion requires at least one of the rights-charter, protectorate-statute,
or integration-review policies, not all three. One policy is sufficient when it
resolves every relevant holding; mixed holdings may require several policies.
The per-holding scripted resolution trigger remains authoritative.

Each public method has a recoverable failure path: supervised plebiscite
relaunch, workers' campaign reconstruction, Belfast Compact reopening, coercive
withdrawal before a war goal, or a reconvened provincial assent convention.
Recovery never refunds reserves or erases the first failure record.

The P1 implementation records these recovery surfaces explicitly: democratic
plebiscite relaunch, Congress Workers' Border Campaign rebuild, fascist border
enforcement withdrawal, restoration Provincial Assent reconvening, and the
existing producer-estate `ireland_territorial_reopen_belfast_compact`. The
Congress route preserves full, partial, and failed mission records; Provincial
Assent records assent only after all four live floors are met; and fascist
withdrawal records a valid partial Northern outcome without refunding consumed
enforcement reserves.

## Concrete focus payoffs

Settlement and policy capability handoffs are concrete route outcomes even
when they should not grant arbitrary equipment. `ireland_settlement_under_law`,
`ireland_all_island_workers_republic`, `ireland_belfast_compact`, and
`ireland_restore_ulsters_place` write durable settlement records consumed by
their named territorial decisions, diplomatic events, and final Northern
review. `ireland_atlantic_ambition` opens the family-specific Atlantic policy
and postwar review surfaces. These five cards are accepted capability handoffs,
not helper-only filler; their custom tooltips must name the operations and
records they enable.

Search filters follow direct-effect parity. Industry, annexation, character,
Army XP, Navy XP, Air XP, and Research tags may appear only when the focus's
completion reward contains the matching direct effect or explicit engine
capability. A downstream thematic relationship alone is not sufficient.

Territorial focuses visibly grant one of:

- named operation/mission unlock;
- claim with stated state and no-core warning;
- equipment/logistics preparation;
- access/guarantee/subject policy capability;
- settlement office and per-state review decisions;
- persistent diplomatic or occupation institution.

Flags that only make later source code work remain undocumented implementation
state and do not replace these payoffs.
