# Oficinas · persistent teams

## What it is / what it solves

An office is a persistent, role-scoped agent workspace: configuration, authorized tools and durable work references survive individual conversations. A coordinator assigns work; specialists execute their own tasks; reviewers test acceptance independently. A transient helper is not a persistent office and should not inherit administrative powers.

## Internals and technologies

The Pi extension is TypeScript, with explicit JSON team configuration and Markdown agent/skill files. A version-2 team map declares roles, workspaces and identity-key sources. Team configuration is owner-controlled and validated; no key value belongs in an example. Task state and correspondence live in Cerebro, not only in local panes.

The extension's delegated-agent interface is asynchronous: assign bounded work, follow the result, and preserve ownership. A visible pane or incoming notification is not an instruction that bypasses the task board, trust decision or review gate.

## Quickstart: published package, configured team

Prerequisites: a compatible Pi runtime, trusted code, an operator-managed team definition and —for shared work— a provisioned Cerebro identity. Start from the package's example rather than inventing a team schema.

```sh
git clone https://github.com/otixe/pi-oficinas.git
cd pi-oficinas
pi install npm:@otixe/pi-oficinas@0.1.0
```

1. Adapt the [team example and setup instructions](https://github.com/otixe/pi-oficinas/tree/main/packages/pi-oficinas) to your own authorized workspaces and roles.
2. Set `PI_OFICINAS_EQUIPO` to the validated version-2 team configuration; provision each agent's own key out of band. Restrict write access to the configuration owner.
3. Launch a new Pi process in the chosen workspace. Verify identity, allowed tools and server attribution.
4. Test one reversible task: read → claim → evidence → submit → independent review. Do not use publication or production changes as the first test.

## The extension family

| npm package | Focus |
| --- | --- |
| `@otixe/pi-oficinas` | Team/office coordination. |
| `@otixe/pi-plan-gate` | Working plan and gates. |
| `@otixe/pi-renovacion` | Continuity/renewal workflow. |
| `@otixe/pi-cache-estable` | Stable prompt/cache behavior. |
| `@otixe/pi-herramientas` | Tool catalog/activation integration. |
| `@otixe/pi-cerebro-ama` | Cerebro bridge plus AMA profiles. |

All six have public `0.1.0` registry metadata. This is **not** a recommendation to load all six blindly: AMA replaces the Cerebro bridge and herramientas activator; avoid duplicate bridge/activator entry points. Read [AMA setup](ama.md) for compatibility and rollback.

## Acceptance and limits

Test a denied operation as well as a permitted one. Ensure a specialist cannot review its own high-impact deliverable merely because a review tool is visible. Persistence needs backup, current-state checks and retained evidence; keeping a terminal open is not enough.
