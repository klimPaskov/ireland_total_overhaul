# Ireland Exceptional Routes Improvement Handoff

Date: 2026-08-14  
Agent role: plan-only improvement-loop planner  
Parent scope: Ireland country package completion  

## Design problem

The current 218-focus, 222-connector tree compresses High Kingship to five
selectable nodes, Five Provinces to four, and Otherworld to six. Existing flags,
events, ideas, profiles, and art contain parts of the intended design, but the
player cannot select or sustain the promised captured and sacral crown outcomes,
confederation and Empty Chair forms, Fifth Province and Rival Irelands, Tuatha,
Fianna, regional court and exploitation forms, or cross-route conclusions.

The current `ireland_high_king_capstone` also sets every surviving convergence
flag. That makes component completion indistinguishable from the three pair
conclusions and the final convergence review.

## Proposed expansion

The addendum specifies exactly **38 new focuses**:

| Route scope | New focuses | Main outcomes |
| --- | ---: | --- |
| High Kingship | 7 | captive path, rescue, Captive Throne, verified sacral path, geasa, Living Land, Unbounded Sacred Rule |
| Five Provinces | 9 | powers convention, funded federation, Empty Chair, confederation, sovereign orders, pentarchy, Fifth Province, Rival Irelands |
| Otherworld | 18 | exploitation, balanced compact, Tuatha courts, Fianna service, regional courts, human restoration, Sealed State |
| convergence | 4 | Crown and Five Provinces, High King of Two Irelands, Five Courts, full three-family order |
| **Total** | **38** | **256 focuses after implementation** |

The plan preserves every existing focus ID, exactly three opening roots, all five
public family gateways at `y = 14`, the existing 30 durable route profiles, the
three-spirit ceiling, and `thumbnail.png`. Only current exceptional and
restoration-support coordinates are reflowed. The current 222 connectors are the
baseline and will grow from explicit new prerequisites.

## Files written

- `docs/plans/ireland_country_package/improvement_loop/ireland_exceptional_routes_depth_addendum_2026-08-14.md`
- `docs/plans/ireland_country_package/subagent_handoffs/ireland_exceptional_routes_improvement_handoff_2026-08-14.md`

No gameplay, localisation, interface, asset, specification, or thumbnail file
was edited. No commit was created, per parent instruction.

## Research basis and regional connections

The plan reconciles the current country-package implementation with the detailed
concealed-route source under `docs/specs/ireland_focus_tree/`, especially the
radical and hidden route specification, hidden cultural route map, AI matrix,
lifecycle matrix, asset ledger, and existing text research.

External primary or institutional references reviewed:

- Royal Sites of Ireland for Tara and Uisneach associations with kingship,
  assembly, and symbolic meeting
- Dúchas Schools' Collection for independently collected 1937 to 1939 local and
  county records
- CELT editions of *Cath Maige Tuired* and *Acallamh na Senórach* for literary
  vocabulary and absurd-route inspiration

The plan marks the limits directly. These sources do not establish a continuous
High Kingship, a fixed five-province 1936 constitution, a twentieth-century
Tuatha polity, or a twentieth-century Fianna military institution. Mide remains
an institutional meeting-place concept. Ulster participation always uses lawful
access and consent. No quotation, genealogy, proverb, or alleged tradition was
invented.

The required offline Paradox wiki pages and vanilla documentation were reviewed.
Relevant structural precedents included the British alternate-monarchy branch
for state-dependent branch visibility and commitment, the Swiss confederation
and council material for negotiated member authority, and the Ethiopian federal
and chamber material for institutional branching. The territorial or release
shortcuts in those precedents are explicitly rejected for Ireland.

## Implementation surfaces affected

The accepted implementation will touch:

- `common/national_focus/ireland_focus_tree.txt`
- a new `common/script_constants/ireland_exceptional_routes.txt`
- country initialisation and exceptional-route scripted effects and triggers
- decisions and missions in the existing government, culture, readiness,
  integration, and regional categories
- a new `events/ireland_exceptional_route_events.txt`, IDs `438` through `460`
- same-slot national spirit forms, cosmetic tags, flags, AI strategy weights,
  English localisation, focus icons, report art, and asset manifests
- `interface/ireland_icons.gfx` and the matching shine registrations
- `docs/ireland_dynamic_effects.md`
- final focus, decision, country-package, localisation, and completion audits

No new decision category, scripted GUI, on-action scan, durable route profile,
audio dependency, or animation package is required. Six existing animated
transition families and six existing focus sprites can be reused where their
subjects match exactly.

## Critical implementation notes

1. Replace the High King capstone's automatic convergence grants. Each new pair
   focus owns only its component flags. The final 180-day review alone owns the
   three final convergence completion flags.
2. The current High Kingship route clamp of `-60` through `+60` prevents the
   canonical Captive Crown and Unbounded Sacred Rule thresholds at above `+75`
   and below `-75`. Apply the global Settlement clamp only while this conclusion
   is unresolved.
3. The current Otherworld dominion focus must cease requiring both compact and
   containment. It becomes the exploitation terminal after deliberate breach.
4. Five Provinces mandates are live province-specific values. Ulster cannot gain
   a mandate from ownership, a claim, a core, or occupation. Empty Chair is a
   stable lawful partial conclusion.
5. The Fianna route recognises only a player-trained, deployed, equipped,
   supplied, commanded formation with a completed service objective. It creates
   no division, manpower, or equipment.
6. Brehon law remains a supporting learned-order module, not a fourth concealed
   sovereignty route.
7. The full convergence is reachable through an elected crown that takes the
   verified sacral branch while retaining constitutional law, a valid five-voice
   federal or confederal settlement, and the balanced Otherworld compact plus
   regional courts.

## Balance and failure coverage

The addendum centralises all new thresholds, costs, durations, deltas, and AI
weights. It gives each action and mission a full, partial, failure, cleanup, and
recovery state. The final convergence requires Site Stewardship `85`, Regional
Participation `80`, Archival Record `85`, Social Consent `65`, valid component
orders, and no captured, warlord, fabricated, exclusion, foreign-patron,
dominion, breach, or sealing result.

No free core, territory, annexation, war goal, war, unit, manpower, equipment, or
magical resource is planned. Extraordinary benefits are timed and tied to
obligations, site care, material delivery, or continuing reviews.

## Open questions

There are no design questions that block implementation. The main agent still
needs to make production choices inside the accepted contract:

- which exact existing named state or site targets each royal circuit and
  Otherworld mission uses, after checking the current site ledger and lawful
  northern-access state
- whether `GFX_focus_ireland_otherworld_statecraft` depicts exploitation closely
  enough to reuse, or needs a replacement icon
- which existing public leader portrait is used for a human steward office, if
  that optional office is shown. No historical person should be promoted to
  supernatural leadership without a separate reviewed design

These choices cannot change the route count, prerequisites, conclusions,
thresholds, no-free-material rule, or lawful Ulster rule.

## Prior addendum and promotion status

The previous country-package improvement addendum was accepted, promoted, and
implemented at `89ff719`. No previous addendum for this same gap remains
unresolved, so this pass is permitted.

This plan should remain in `docs/plans/ireland_country_package/improvement_loop/`
until accepted and implemented. On acceptance, merge its architecture into
`campaign_architecture.md`, lifecycles into `systems_and_lifecycles.md`, AI,
balance, text, and asset rules into `ai_balance_assets_and_text.md`, and source
IDs and proof into `implementation_matrix.md`.

## Completion boundary

Implementing this addendum closes the exceptional-route simplification reported
in `final_completion_report_2026-08-14.md`. It does not by itself close any other
country-package blockers in that report, including remaining portrait,
dispatcher, documentation, or final validation work. The parent should claim the
overall goal complete only after this addendum is promoted and implemented and
all other report blockers are resolved.

Skills used for this planning pass:

- `hoi4-improvement-loop`
- `hoi4-feature-planning`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`
- `hoi4-events`
- `hoi4-feature-assets`
- `hoi4-text-audio-research`
- `hoi4-subagents`
