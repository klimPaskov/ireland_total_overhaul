# Northern outcome and recovery tranche

Status: implemented on 2026-08-14.

The five family resolution focuses now represent completed political outcomes rather than free flags:

- democratic settlement requires a full or partial supervised-plebiscite result;
- the Congress settlement requires completion of the Workers' Border Campaign;
- the fascist enforcement focus requires an ultimatum refusal or rejected counteroffer;
- the Belfast Compact focus requires an accepted compact or accepted counteroffer;
- the restoration settlement requires completion of Provincial Assent.

An accepted Ulster ultimatum or counteroffer records the fascist Northern settlement directly and closes the enforcement file. The enforcement focus is bypassed in that state, so the player does not issue a second demand after already receiving Northern Ireland.

The oligarchic route now has a recovery action after a rejected Belfast Compact. `ireland_territorial_reopen_belfast_compact` waits for the territorial diplomatic cooldown, spends 15 Political Power over 35 days, rebuilds British Flexibility and Unionist Consent, clears the rejection record, and permits a renewed compact offer. This prevents a single refusal from silently dead-ending the route.

Each focus gate and recovery action has a named player-facing requirement or exact effect tooltip.
