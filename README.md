# Ireland Total Overhaul

Ireland Total Overhaul is a research-grounded Hearts of Iron IV overhaul for
Ireland. It combines a large non-linear national focus tree with constitutional
politics, route-linked decisions and missions, historical event chains,
neutrality gameplay, Northern Ireland progression, custom interfaces, and
source-documented visual assets.

## Installation

### Steam Workshop

The easiest way to install the mod is through the Steam Workshop.

Steam Workshop: not yet assigned

Subscribe to the mod, enable it in the Paradox Launcher, and launch Hearts of Iron IV.

### Manual install

Clone the repository into your Hearts of Iron IV mod folder:

```bash
git clone https://github.com/klimPaskov/ireland_total_overhaul.git
```

Then enable the mod in the Paradox Launcher.

## Development setup

This mod uses the repo instructions and skills together with HOI4 Agent Tools.
Start the coding agent from this repository root.

1. Install Node.js 22 or 24.
2. Install and configure the MCP server:

   ```powershell
   npm install --global hoi4-agent-tools@1.2.0
   hoi4-agent-tools-setup --init `
     --mod-root "C:\Users\<you>\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod" `
     --game-root "C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV"
   hoi4-agent-tools-setup --print-client-config
   ```

3. Add the printed client entry to the coding agent and reload it.
4. Call `hoi4.mods` and use the returned Ireland Total Overhaul workspace ID.

Agents can inspect, render, create, and clean focus trees, scripted GUIs, and
maps through MCP. For event chains they inspect a bounded route, edit normal
mod files, then compare, lint, and render the result. Large artifacts stay in
linked MCP resources so the rest of the skills and subagents keep their context.

## Contributing

The main way to contribute is by suggesting ideas through Discord or comments on the video series.

You can also open GitHub issues for:

* Bugs
* Broken localisation
* Broken focus effects
* Balance problems
* Missing icons
* Suggestions
* Compatibility issues

Before reporting a bug, check whether someone has already reported the same issue.

## Status

This repository contains the Ireland overhaul implementation, its canonical
specifications and audits, and the local development references used to
maintain it.
