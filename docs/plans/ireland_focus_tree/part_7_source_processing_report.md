# Ireland Focus Tree Part 7 Source Processing Report

Feature slug: `ireland_focus_tree`

Status: complete source-processing evidence for the revalidated canonical candidate

# Input sweep

Every text source available under `/mnt/data` before the final-gate build was opened as UTF-8 and processed. Generated final-gate work folders were excluded from this input count so the report does not count its own outputs.

| Measure | Result |
| --- | ---: |
| Markdown, TOML, text, JSON, and CSV sources | 96 |
| decoded bytes | 3,157,304 |
| decoded lines | 42,620 |
| whitespace-delimited words | 456,232 |
| decoding errors | 0 |

The sweep includes all uploaded skills, every uploaded custom subagent definition, `AGENTS.md`, the project README, every continuation prompt, every available plan and validation record, the direct workspace copies of the Ireland sources, and the final unblock handoff. Duplicate checkpoints and superseded files were treated as development history.

# Canonical candidate verification

The cumulative Parts 1 through 7 candidate archive was extracted into an isolated build directory. Its internal `PACKAGE_CONTENTS.sha256` ledger passed before any repair was made. The extracted candidate, rather than stale direct workspace copies, became the starting source for final-gate reconciliation.

The canonical semantic inventory processed every heading, table, fixed identifier roster, source URL, route classification, failure reference, cleanup reference, AI reference, event reference, decision reference, and mission reference across the 35 canonical Markdown files.

| Canonical measure | Result |
| --- | ---: |
| files | 35 |
| bytes | 2,402,852 |
| lines | 30,809 |
| whitespace-delimited words | 351,304 |
| headings | 2,634 |
| Markdown tables | 763 |

# Source authority decision

The verified cumulative candidate is authoritative for this final-gate attempt. Direct `/mnt/data/docs/` copies were not trusted when they differed from the candidate because repeated tool uploads had overwritten some plan files with older checkpoints. The repaired build is synced back to the direct documentation paths only after validation.

# Limitations

The source sweep proves text availability, decoding, canonical inventory, and cross-file processing. It does not prove Hearts of Iron IV engine behaviour. The offline Paradox wiki and local game installation required by `AGENTS.md` remain unavailable and belong to implementation preflight.
