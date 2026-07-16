# Codex VS Code Starter Kit

This repository uses a reusable, team-friendly Codex setup for VS Code.

The starter kit contains:

- `AGENTS.md` — the automatically discovered entry point
- `GOALS.md` — objectives, priorities, success criteria, and non-goals
- `INSTRUCTIONS.md` — coding, testing, scientific-data, security, and Git rules
- `ARCHITECTURE.md` — repository structure, components, data flow, CRS, and units
- `WORKFLOW.md` — tested setup, build, run, validation, and HPC commands
- `MEMORY.md` — verified, durable decisions and project facts
- `PLANS.md` — execution-plan template for substantial tasks
- `README.md` — installation and maintenance guidance
- `.codex/config.toml.example` — optional project-level configuration

## Recommended Structure

```text
project/
├── AGENTS.md
├── GOALS.md
├── INSTRUCTIONS.md
├── ARCHITECTURE.md
├── WORKFLOW.md
├── MEMORY.md
├── PLANS.md
└── .codex/
    └── config.toml
```

## How It Works

Only `AGENTS.md` is automatically recognized as the standard project-instruction
file. It therefore acts as the entry point, telling Codex which supporting
documents to read for each kind of task.

For example:

- Codex reads `GOALS.md` when it needs to understand project priorities.
- Codex reads `INSTRUCTIONS.md` before changing code, tests, data, or dependencies.
- Codex reads `ARCHITECTURE.md` before changing interfaces, schemas, module
  boundaries, coordinate systems, or data flow.
- Codex reads `WORKFLOW.md` before building, running, testing, or delivering work.
- Codex reads `MEMORY.md` when earlier verified decisions or durable project facts
  matter.
- Codex uses `PLANS.md` for multi-file, risky, ambiguous, or long-running tasks.

## Setup

1. Copy the template files into the root of the Git repository.
2. Replace every `<PLACEHOLDER>` with project-specific information.
3. Remove sections and rules that do not apply.
4. Verify every command documented in `WORKFLOW.md`.
5. Commit the Markdown files as shared team documentation.
6. Rename `.codex/config.toml.example` to `.codex/config.toml` only if the team
   wants shared project-level Codex settings and trusts the repository.
7. Start a new Codex session and ask:

   ```text
   Summarize the applicable project instructions and identify any
   unresolved placeholders.
   ```

## Important Guidelines

- Keep `AGENTS.md` short and use it as the authoritative instruction router.
- Put specialized rules in the supporting documents instead of making
  `AGENTS.md` excessively long.
- Add nested `AGENTS.md` files only when a specific directory genuinely requires
  different commands or constraints.
- Keep instructions concrete, verifiable, and specific to the repository.
- Verify documented commands whenever the project toolchain changes.
- Add new guidance after repeated mistakes or recurring review feedback.
- Use tests, linters, hooks, and continuous integration to enforce mechanical
  rules.
- Never include passwords, access tokens, credentials, or private personal
  information in these files.

## Using `MEMORY.md`

Do not use `MEMORY.md` as a conversation history or daily progress log. It should
contain only durable and verified information, such as:

- architectural decisions;
- scientific or domain conventions;
- validated reference results;
- important compatibility constraints;
- verified reasons why a previous approach failed.

Temporary tasks belong in the issue tracker or `PLANS.md`. Code history belongs
in Git.

## Scientific and HPC Projects

The templates are designed to accommodate scientific Python, geoscience,
coordinate-system, numerical-validation, data-provenance, and HPC workflows,
while remaining suitable for ordinary software projects.

For scientific repositories, document the following explicitly:

- units and sign conventions;
- coordinate reference systems and axis order;
- vertical datum and positive depth direction;
- input-data provenance;
- numerical tolerances and reference results;
- immutable raw-data locations;
- approved HPC execution environments;
- commands that must not run on cluster login nodes.

## References

This structure follows the official
[Codex `AGENTS.md` guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
