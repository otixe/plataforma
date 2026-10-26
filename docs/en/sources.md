# Sources & status

**Documentation snapshot: 2026-10-25.** Availability is not the same as production readiness. This ledger keeps publication, reported architecture and measured evidence separate.

## Public sources

| Source | What it supports | Qualification |
| --- | --- | --- |
| [Pi upstream](https://github.com/earendil-works/pi) and [Otixe fork](https://github.com/otixe/pi) | Runtime, package/extension lifecycle, codemode and security model. | Local runtime docs were 1.4.0; future versions can differ. |
| [pi-oficinas](https://github.com/otixe/pi-oficinas) | Team configuration, identity resolution and extension family. | Inspected source revision: `8bb092653cefa886165cf4588c1d6bc43fd14b95`. |
| [AMA README](https://github.com/otixe/pi-oficinas/tree/main/packages/pi-cerebro-ama) | 8/14 profiles, setup, compatibility, measurement and rollback. | Surface adapter for existing Cerebro; no bundled server. |
| [AMA measurement script](https://github.com/otixe/pi-oficinas/blob/main/packages/pi-cerebro-ama/bin/measure-jsonl.py) | Offline usage calculation and partitions. | Recorded metadata, not invoices or causality. |
| npm registry `@otixe/*` | Six package versions at `0.1.0`. | Registry metadata verified; this handoff did not test all registry installs. |
| [Hermes fork](https://github.com/otixe/hermes-agent) | Adjacent agent-runtime work. | Not claimed to be one of the four platform components. |

Some package prose was written before publication and still describes local artifacts. Live registry metadata takes precedence for availability; compatibility caveats still apply.

## Internal sources, safely summarized

The Cerebro architecture plan and master guide support the gateway/storage/retrieval/task/RBAC description. Harness v5 supports separation of powers, proportionate gates and durable evidence. A Sinapsis UI redesign/deployment runbook supports the **reported** React/Vite frontend + FastAPI BFF (backend for frontend), acting as a Cerebro client. The project coordinator confirmed this architecture and the pending public release.

These private documents are **not included or linked to private endpoints**. They are not a public server distribution or reproducible Sinapsis installer. No raw logs, personal agent documents or private deployment settings are exported. Public release instructions remain pending for those components.

## AMA and quantified results

This manual carries **no savings figures**. AMA is presented as a design — the code-against-a-typed-API pattern applied to Cerebro — and its efficiency is to be verified on your own workload. Quantified results will be added after a representative, reproducible measurement. The 8/14 profile definitions come from the package README and a census of real tool use; no leader-profile savings measurement is asserted.

## Publication prerequisites

1. Independent QA of facts, translations, diagrams, links and private-data scanning.
2. Maintainer creates/reviews `otixe/otixe` and `otixe/plataforma`; these are proposed destinations, not verified active repositories at this snapshot.
3. Publish the profile; configure Pages (Actions) and environment protection; manually approve documentation deployment.
4. Replace pending source links/status only after Cerebro and Sinapsis releases exist and installation QA passes.

A strict build and zero secret-scanner findings are evidence, not proof that every claim is true or every private fact has been removed. Human review remains part of acceptance.
