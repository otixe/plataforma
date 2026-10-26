# Pi · execution runtime

## What it is / what it solves

Pi is the extensible agent runtime: a model conversation loop, tool execution, durable sessions and a terminal UI. The platform uses it as the execution substrate rather than asking the memory service to execute arbitrary jobs. An Otixe fork exists; it must be distinguished from upstream and from the separately published extensions.

## Internals and technologies

Node.js/TypeScript hosts extensions and tools. An extension can register tools, commands and lifecycle hooks. Markdown skills provide task-specific instructions. Session history and context compaction support long work; they do not replace a shared task board. Models and providers are configured independently of Cerebro.

Codemode runs JavaScript in QuickJS: no direct Node, filesystem, network or timer globals. Scripts use registered tools for external operations and emit selected results with `text`, `console.log` or `return`. This can filter a large result before it reaches the model; it is not permission isolation for the underlying tools.

## Quickstart: public runtime

Prerequisite: Node.js **22.19+** and a provider/account you are authorized to use. Review the upstream package and its trust policy first.

```sh
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
pi --version
pi
```

Complete the chosen provider's login/configuration in the terminal; keep secrets out of Git and documentation. Runtime installation alone does **not** install Cerebro, provision an identity or create offices. For the fork's behavior and supported extension API, consult the [Pi repository](https://github.com/otixe/pi).

## Quickstart: an extension

```sh
pi install npm:@otixe/pi-oficinas@0.1.0
```

After configuring a team, start a **fresh Pi process**. Review [Oficinas](oficinas.md) before attempting delegation. AMA specifically requires compatible exposure/codemode support (validated against Pi 1.4.0); installing a package is not proof that its entry points loaded.

## Safety and acceptance

- Trust installed code: extensions have the process's OS permissions.
- Verify the runtime version, active tool list and your own identity after configuration.
- Do not equate a successful CLI install with a functioning service or authorized action.
- Keep external model data policy and local tool permissions explicit.

Sources: [upstream README](https://github.com/earendil-works/pi), [extension monorepo](https://github.com/otixe/pi-oficinas), [source ledger](sources.md).
