# Ireland Event Programme

The Ireland event programme connects authored historical, political, material,
Northern, foreign, route and regional reports to one player-facing cadence.
It contains 495 top-level triggered country events and 998 event choices.

## Player cadence

The five family postwar conclusion reports are direct milestone events rather
than ordinary flavour-pool entries. Each uses distinct 210x176 report art and is
archived after its settlement decision, so the monthly cadence cannot replay a
conclusion or produce a second family popup.

The ordinary programme runs from `on_monthly_IRE`. It presents at most one
eligible report on a monthly pulse and then skips the next monthly pulse, giving
a maximum of six ordinary programme reports per year. Focus conclusions,
player-invoked parliamentary or contribution events, and other direct milestone
events remain immediate because they report an action the player just took.

A source that merits foreign attention may open a 14-day reaction window. The
window waits four days, selects one unresolved eligible actor response, and then
closes. When other actors also qualify, one aggregate digest follows. A global
120-day cooldown prevents a new foreign-reaction programme from opening for
every routine choice. Actor reports already seen are never reset; unresolved
actor nodes remain eligible in later windows, so pacing does not delete content.

## Clarity contract

- Every event has a report or news image registered through
  `interface/ireland_event_art.gfx` or `interface/ireland_sourced_assets.gfx`.
- Every choice calls a matching `<option_key>.effects` custom tooltip.
- Descriptions identify the actor, immediate problem and strategic stakes.
- Choice text states the policy being adopted; the effect tooltip lists the
  affected country values and whether each rises or falls. Every numeric ledger
  choice computes its exact signed, post-clamp result when the report opens.
  Fixed resource costs and timed reviews state their amounts and durations.
- Hidden flags, temporary arithmetic and recomputation helpers are not presented
  as rewards. They are described through the country value that the player sees.

## Runtime ownership

`ireland_dispatch_event_programme` owns the sparse ordinary queue.
`ireland_open_foreign_reaction_window` owns the 120-day admission cooldown and
window reset. `ireland_dispatch_foreign_reaction_response` owns the single actor
selection. `ireland_consolidate_foreign_reactions` closes the window, and event
`ireland_events.430` owns the player's digest choice.

The foreign response and digest bypass the ordinary unrolled dispatcher segment,
so a monthly pulse cannot produce a second actor popup. The one-response flag,
the digest-scheduled flag and durable `ireland_event_seen_400` through `_429`
records prevent duplicate scheduling and replay.

`ireland_event_option_<choice>_target_<n>_delta` values are presentation previews
calculated in the report's hidden immediate block. They mirror each option's
arithmetic and destination-ledger clamp without mutating the destination. The
matching option-effects localisation prints those preview variables, so each
numeric choice explains the exact applied values rather than only their
direction. This includes dynamically scaled route and flavour reports, foreign
responses, the foreign digest, Dillon's mandate setback, the Frank Ryan chain,
the Otherworld archive reveal, and the captive-crown outcome.

## Assets

Event pictures live under `gfx/event_pictures/ireland/`. Current event art uses
the stable `GFX_report_event_ireland_*` and `GFX_news_event_ireland_*` sprite
names. Historical chains use dated archival families where available; political,
regional and concealed routes use their matching family art. No missing-image
placeholder is part of the programme.

## AI and balance

All event choices retain authored `ai_chance` weights and route modifiers. The
cadence changes when a choice is presented, not which effect the AI selects.
Foreign actor selection is weighted evenly among currently eligible unresolved
nodes; actor validity, leverage thresholds and saturation still determine which
weights are non-zero.

## Future extensions

The remaining useful expansion is additional family-specific archival art for
the most reused flavour and Northern image groups. That work may increase visual
variety without raising event frequency or changing event IDs, triggers, choices
or effects.
