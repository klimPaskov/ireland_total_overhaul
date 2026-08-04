# Ireland route-spirit localisation handoff — 2026-07-29

Status: localisation pass complete. No gameplay, idea, decision, trigger, asset, manifest, achievement, or specification source was edited. No commit was created.

## Scope

Owned files:

- `localisation/english/ireland_l_english.yml`
- this handoff

The source audit used `common/ideas/ireland_spirits.txt`, the route-spirit lifecycle sections in Parts 3–6, the AI strategy matrix, the route refresh effect, the offline localisation and idea-modding wiki pages, and the installed vanilla modifier documentation.

A concurrent user edit to `ireland_northern_settlement_ledger_desc` was preserved exactly:

> Record Ireland's legal claim to Northern Ireland and open the settlement ledger. The claim grants no control, occupation, settlement, integration, or core: Unionist Consent, Nationalist Consent, Labour Cooperation, British Flexibility, Security Stability, and Integration Capacity remain separate tests.

That key is not part of this route-spirit patch.

## Count reconciliation and family coverage

The exact source composition is:

| Family | Opening | Route forms | Failure/corruption forms | Total |
| --- | ---: | ---: | ---: | ---: |
| Governing Order | 1 | 18 | 2 | 21 |
| Organised Society | 1 | 18 | 2 | 21 |
| Security and External Position | 1 | 18 | 2 | 21 |
| **Total** | **3** | **54** | **6** | **63** |

The earlier audit phrase that all 60 variants shared one template was imprecise. Fifty-four route-form descriptions used the repeated `takes the form of ... benefits and obligations` sentence. The six failure/corruption forms had separate prose, but each remained a short one-sentence summary that did not fully state its modifier-facing tradeoff. All 63 descriptions were audited and rewritten: the 54 route forms, six failure/corruption forms, and three opening forms whose modifier meaning was still under-described.

## Writing result

- Constitutional and H/P routes use legal, parliamentary, material, labour, rural, coalition, and professional-command institutions rather than generic ideology labels.
- De Valera reconciliation and emergency government are distinguished by amnesty and ordinary law versus reviewed exceptional administration.
- Lemass prose is tied to contracts, industrial construction, delivery, supply, and bottlenecks.
- Cosgrave, Mulcahy, Costello, and Dillon separately emphasise constitutional continuity, civilian defence command, coalition clauses, and a voted intervention mandate.
- Norton, Clann, and vocational government separately use affiliates and services, smallholders and county delivery, and freely constituted sector councils.
- IRA descriptions distinguish civil republican authority from contested Army Council command.
- Congress descriptions name unions, smallholders, committees, plural mandates, and the danger of directorate capture.
- O'Duffy, clerical-producer, and Ailtirí descriptions state coercion, hierarchy, compulsory representation, exclusion, antisemitism, patronage, and constitutional or social costs directly.
- High Kingship, Five Provinces, and Otherworld descriptions name their institutions only on their corresponding idea keys. Their prose assumes the route idea is already visible and does not place hidden-route terminology in the opening trio or ordinary constitutional route descriptions.
- Failure forms now state the institution that failed and the actual stability, political, civilian-economy, defence, invasion-defence, or subversion tradeoff represented by their idea block.

## Exact changed keys

### Opening trio

- `ireland_spirit_governing_order_desc`
- `ireland_spirit_organised_society_desc`
- `ireland_spirit_security_external_position_desc`

### Governing Order route and failure forms

- `ireland_spirit_governing_de_valera_reconciliation_desc`
- `ireland_spirit_governing_de_valera_emergency_desc`
- `ireland_spirit_governing_lemass_developmental_desc`
- `ireland_spirit_governing_cosgrave_institutional_desc`
- `ireland_spirit_governing_mulcahy_civil_defence_desc`
- `ireland_spirit_governing_costello_coalition_desc`
- `ireland_spirit_governing_dillon_intervention_desc`
- `ireland_spirit_governing_norton_parliamentary_desc`
- `ireland_spirit_governing_clann_agrarian_broker_desc`
- `ireland_spirit_governing_constitutional_vocational_desc`
- `ireland_spirit_governing_ira_republican_desc`
- `ireland_spirit_governing_congress_desc`
- `ireland_spirit_governing_oduffy_desc`
- `ireland_spirit_governing_clerical_producer_desc`
- `ireland_spirit_governing_ailtiri_total_state_desc`
- `ireland_spirit_governing_high_king_desc`
- `ireland_spirit_governing_five_provinces_desc`
- `ireland_spirit_governing_otherworld_desc`
- `ireland_spirit_governing_corrupted_desc`
- `ireland_spirit_governing_collapse_desc`

### Organised Society route and failure forms

- `ireland_spirit_society_de_valera_reconciliation_desc`
- `ireland_spirit_society_de_valera_emergency_desc`
- `ireland_spirit_society_lemass_developmental_desc`
- `ireland_spirit_society_cosgrave_institutional_desc`
- `ireland_spirit_society_mulcahy_civil_defence_desc`
- `ireland_spirit_society_costello_coalition_desc`
- `ireland_spirit_society_dillon_intervention_desc`
- `ireland_spirit_society_norton_parliamentary_desc`
- `ireland_spirit_society_clann_agrarian_broker_desc`
- `ireland_spirit_society_constitutional_vocational_desc`
- `ireland_spirit_society_ira_republican_desc`
- `ireland_spirit_society_congress_desc`
- `ireland_spirit_society_oduffy_desc`
- `ireland_spirit_society_clerical_producer_desc`
- `ireland_spirit_society_ailtiri_total_state_desc`
- `ireland_spirit_society_high_king_desc`
- `ireland_spirit_society_five_provinces_desc`
- `ireland_spirit_society_otherworld_desc`
- `ireland_spirit_society_patronage_desc`
- `ireland_spirit_society_broken_services_desc`

### Security and External Position route and failure forms

- `ireland_spirit_security_de_valera_reconciliation_desc`
- `ireland_spirit_security_de_valera_emergency_desc`
- `ireland_spirit_security_lemass_developmental_desc`
- `ireland_spirit_security_cosgrave_institutional_desc`
- `ireland_spirit_security_mulcahy_civil_defence_desc`
- `ireland_spirit_security_costello_coalition_desc`
- `ireland_spirit_security_dillon_intervention_desc`
- `ireland_spirit_security_norton_parliamentary_desc`
- `ireland_spirit_security_clann_agrarian_broker_desc`
- `ireland_spirit_security_constitutional_vocational_desc`
- `ireland_spirit_security_ira_republican_desc`
- `ireland_spirit_security_congress_desc`
- `ireland_spirit_security_oduffy_desc`
- `ireland_spirit_security_clerical_producer_desc`
- `ireland_spirit_security_ailtiri_total_state_desc`
- `ireland_spirit_security_high_king_desc`
- `ireland_spirit_security_five_provinces_desc`
- `ireland_spirit_security_otherworld_desc`
- `ireland_spirit_security_compromised_desc`
- `ireland_spirit_security_disarmed_desc`

## Exact modifier cross-check

Abbreviations: `Stab` stability, `PP` political-power factor, `War` war-support factor, `CG` consumer-goods factor, `CivBuild` industrial-complex construction speed, `ArmsBuild` arms-factory construction speed, `Def` army defence, `Atk` army attack, `Coast` naval-invasion defence, and `Res` local-resources factor. Values below are percentages represented by the fixed modifiers in `common/ideas/ireland_spirits.txt`.

| Route suffix | Governing Order | Organised Society | Security and External Position |
| --- | --- | --- | --- |
| `de_valera_reconciliation` | Stab +5, War +2 | Stab +4, PP +2 | Def +3, Stab +2 |
| `de_valera_emergency` | Stab +2, PP +4, War +4 | CG +3, Stab -2 | Def +5, War +3 |
| `lemass_developmental` | CivBuild +5, PP +2 | CivBuild +4, CG -2 | Def +3, ArmsBuild +3 |
| `cosgrave_institutional` | Stab +5, PP +2 | CG -3, Stab +3 | Def +3, PP +2 |
| `mulcahy_civil_defence` | Def +5, Stab +2 | Stab +3, Def +2 | Def +5, Coast +4 |
| `costello_coalition` | Stab +4, CG -2 | Stab +4, CG -3 | Coast +4, Stab +2 |
| `dillon_intervention` | War +5, PP +2 | War +4, CG -1 | Atk +4, Def +3 |
| `norton_parliamentary` | Stab +4, CG -3 | Stab +5, CG -4 | Def +3, Stab +3 |
| `clann_agrarian_broker` | Stab +3, Res +5 | Res +6, Stab +3 | Def +4, Res +3 |
| `constitutional_vocational` | Stab +4, PP +2 | Stab +4, CG -2 | Def +3, Stab +3 |
| `ira_republican` | Def +4, Stab +2 | Stab +2, Def +3 | Atk +5, Def +2, Stab -3 |
| `congress` | Stab +3, PP +4 | Stab +4, CG -3 | Def +4, Stab +3 |
| `oduffy` | War +6, Stab -2 | Stab +1, CG +2, War +3 | Atk +5, Def +2, Stab -3 |
| `clerical_producer` | Stab +5, CG -1 | Stab +5, CG -3 | Def +4, Stab +3 |
| `ailtiri_total_state` | War +5, PP +5, Stab -4 | War +5, Stab -4, CG +2 | Atk +6, Def +3, Stab -5 |
| `high_king` | Stab +6, PP +2 | Stab +5, CG -2 | Def +5, PP +2 |
| `five_provinces` | Stab +4, PP +3 | Stab +4, Res +4 | Def +4, Coast +5 |
| `otherworld` | Stab +3, PP +3 | Stab +3, CG -1 | Def +3, Coast +4 |

Opening and failure forms:

| Idea | Exact modifiers reflected in prose |
| --- | --- |
| `ireland_spirit_governing_order` | Stab +3, PP +2 |
| `ireland_spirit_organised_society` | Stab +3, CG -1 |
| `ireland_spirit_security_external_position` | Def +3, Coast +4 |
| `ireland_spirit_governing_corrupted` | Stab -4, PP -2, War +3 |
| `ireland_spirit_governing_collapse` | Stab -8, Def -4 |
| `ireland_spirit_society_patronage` | CG +4, Stab -3 |
| `ireland_spirit_society_broken_services` | Stab -5, CG +3 |
| `ireland_spirit_security_compromised` | Def -4, `foreign_subversive_activites` +5 |
| `ireland_spirit_security_disarmed` | Def -6, Coast -5 |

No modifier value, cost, dynamic effect, or gameplay promise was added to localisation beyond the direction represented by these blocks.

## Concealment check

The static route refresh adds the High Kingship, Five Provinces, and Otherworld idea triplets only after `ireland_route_high_king`, `ireland_route_five_provinces`, or `ireland_route_otherworld` is present. Hidden-route institutional language is confined to those corresponding idea descriptions. The opening trio, ordinary constitutional variants, radical variants, and failure forms do not announce an unrevealed concealed route.

There is no convergence-specific persistent idea or description among the 63 source ideas. Consequently, this pass added no convergence wording that could leak before the convergence order is visible.

## Idea/localisation semantic mismatches requiring parent action

These cannot be resolved by description-only edits without changing idea or runtime architecture:

1. **Historical de Valera and reconciliation share one triplet:** `ireland_refresh_route_spirits` applies the `de_valera_reconciliation` ideas to either `ireland_route_de_valera_stewardship` or `ireland_route_de_valera_reconciliation`. The title and description therefore cannot fully distinguish AI-01 historical stewardship from AI-02 reconciliation.
2. **IRA civil and GHQ profiles share one triplet:** the canonical matrix separates civil republican government from GHQ command, but the idea source provides only `ira_republican` forms titled around Civil Republican Authority. The new prose makes the command contest visible, but a true GHQ state still lacks its own final idea identity.
3. **Congress plural and vanguard profiles share one triplet:** the source has one `congress` triplet for both plural congress and possible directorate outcomes.
4. **O'Duffy personal and corporate profiles share one triplet:** the current `oduffy` forms blend personal command and corporate institutions rather than selecting one profile-specific form.
5. **Clerical guardianship and producer-council profiles share one triplet:** `clerical_producer` combines Church-service guardianship and compulsory producer representation even though the canonical matrix treats them as separate profiles.
6. **Hidden subprofiles are compressed:** constitutional and sacral High Kingship share `high_king`; federation and pentarchy share `five_provinces`; compact, dominion, and containment share `otherworld`. The shared descriptions state institutions and tradeoffs common to each family, but the titles and modifiers cannot identify the active subprofile.
7. **Convergence has no persistent idea merger form:** the canonical AI-30 convergence order and convergence focus sequence have no dedicated governing, society, or security idea block in the 63-idea source. The parent should confirm whether convergence deliberately retains a predecessor triplet or whether three merged forms are missing.

Resolved during parent review: `ireland_spirit_security_compromised`
now uses the documented engine token `foreign_subversive_activites`.

## Validation

- Parsed 63 source idea IDs and found one description key for every ID.
- Family coverage is exactly 21/21/21.
- All 63 descriptions are unique and contain at least two complete sentences.
- No old generic template phrase remains.
- No duplicate complete sentence or repeated eight-word opening scaffold remains across the set.
- No update-history wording was introduced.
- The localisation file remains strict UTF-8 with BOM, and the complete file has no duplicate keys.
- The working diff contains 63 route-spirit description changes plus the separately owned Northern ledger change noted above. No other localisation key was changed by this pass.

Live HOI4 testing was not performed; the meaningful validation for this description-only task was the exact source-modifier, route-identity, key-coverage, concealment, and encoding comparison above.
