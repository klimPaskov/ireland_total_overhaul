# P0 family settlement and recovery decision-icon GFX handoff

Status: wired by the parent implementation in `interface/ireland_icons.gfx`.
The runtime sprite convention is the exact `GFX_decision_<decision_id>` form
shown below, including the `ireland_action_` segment.

Scope: source PNGs, processed 32x32 RGBA PNGs, runtime DDS files, manifest, prompts, contact sheets, and handoff only. No `.gfx`, gameplay, localisation, decision, GUI, or thumbnail files were edited by the asset worker.

Registered target: existing `interface/ireland_icons.gfx`, which owns the
Ireland decision-action sprite surface. The final DDS paths below are consumed
by the exact registered decision IDs.

Parent wiring disposition: the runtime registration retains each complete action
ID as `GFX_decision_<decision_id>` (for example,
`GFX_decision_ireland_action_ratify_the_postwar_republic`) because the decision
implementation already consumes that stable form. The DDS paths below are final;
the shorter names from the initial asset draft are historical and superseded by
these registered IDs.

```text
spriteType = { name = GFX_decision_ireland_action_ratify_the_postwar_republic texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_ratify_the_postwar_republic.dds" }
spriteType = { name = GFX_decision_ireland_action_civilianise_the_workers_congress texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_civilianise_the_workers_congress.dds" }
spriteType = { name = GFX_decision_ireland_action_place_the_directorate_under_statute texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_place_the_directorate_under_statute.dds" }
spriteType = { name = GFX_decision_ireland_action_convert_contracts_to_reconstruction_credit texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_convert_contracts_to_reconstruction_credit.dds" }
spriteType = { name = GFX_decision_ireland_action_define_the_postwar_crown texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_define_the_postwar_crown.dds" }
spriteType = { name = GFX_decision_ireland_action_reconstitute_the_postwar_coalition texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_reconstitute_the_postwar_coalition.dds" }
spriteType = { name = GFX_decision_ireland_action_reconvene_the_workers_congress texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_reconvene_the_workers_congress.dds" }
spriteType = { name = GFX_decision_ireland_action_demobilise_the_failed_directorate texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_demobilise_the_failed_directorate.dds" }
spriteType = { name = GFX_decision_ireland_action_rebalance_the_producer_estates texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_rebalance_the_producer_estates.dds" }
spriteType = { name = GFX_decision_ireland_action_reconvene_the_crown_council texturefile = "gfx/interface/decisions/ireland/actions/decision_ireland_reconvene_the_crown_council.dds" }
```

## Exact decision routing

| Exact decision ID | Registered sprite | Runtime texture |
| --- | --- | --- |
| `ireland_action_ratify_the_postwar_republic` | `GFX_decision_ireland_ratify_the_postwar_republic` | `gfx/interface/decisions/ireland/actions/decision_ireland_ratify_the_postwar_republic.dds` |
| `ireland_action_civilianise_the_workers_congress` | `GFX_decision_ireland_civilianise_the_workers_congress` | `gfx/interface/decisions/ireland/actions/decision_ireland_civilianise_the_workers_congress.dds` |
| `ireland_action_place_the_directorate_under_statute` | `GFX_decision_ireland_place_the_directorate_under_statute` | `gfx/interface/decisions/ireland/actions/decision_ireland_place_the_directorate_under_statute.dds` |
| `ireland_action_convert_contracts_to_reconstruction_credit` | `GFX_decision_ireland_convert_contracts_to_reconstruction_credit` | `gfx/interface/decisions/ireland/actions/decision_ireland_convert_contracts_to_reconstruction_credit.dds` |
| `ireland_action_define_the_postwar_crown` | `GFX_decision_ireland_define_the_postwar_crown` | `gfx/interface/decisions/ireland/actions/decision_ireland_define_the_postwar_crown.dds` |
| `ireland_action_reconstitute_the_postwar_coalition` | `GFX_decision_ireland_reconstitute_the_postwar_coalition` | `gfx/interface/decisions/ireland/actions/decision_ireland_reconstitute_the_postwar_coalition.dds` |
| `ireland_action_reconvene_the_workers_congress` | `GFX_decision_ireland_reconvene_the_workers_congress` | `gfx/interface/decisions/ireland/actions/decision_ireland_reconvene_the_workers_congress.dds` |
| `ireland_action_demobilise_the_failed_directorate` | `GFX_decision_ireland_demobilise_the_failed_directorate` | `gfx/interface/decisions/ireland/actions/decision_ireland_demobilise_the_failed_directorate.dds` |
| `ireland_action_rebalance_the_producer_estates` | `GFX_decision_ireland_rebalance_the_producer_estates` | `gfx/interface/decisions/ireland/actions/decision_ireland_rebalance_the_producer_estates.dds` |
| `ireland_action_reconvene_the_crown_council` | `GFX_decision_ireland_reconvene_the_crown_council` | `gfx/interface/decisions/ireland/actions/decision_ireland_reconvene_the_crown_council.dds` |

All textures are exact 32x32, 32-bit uncompressed BGRA DDS with alpha. The processed icons are intentionally transparent and use distinct silhouettes: republic parchment/seal, congress gavel/gear, statutory baton/tablet, credit ledger/coin/bridge, crown/pillar, coalition seals/handshake, reconvening bell/chairs, demobilised baton/pennant, producer scale, and crown council ring. The parent agent owns `.gfx` insertion and decision-file references.
