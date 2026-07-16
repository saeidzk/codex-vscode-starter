# Codex VS Code Starter Kit

A reusable, team-friendly set of project instructions for using Codex in Visual
Studio Code. The templates help Codex understand a repository's goals,
architecture, working conventions, validation commands, and durable decisions.

> [!IMPORTANT]
> These files are templates. Replace every `<PLACEHOLDER>`, remove rules that do
> not apply, and verify all commands before relying on them in a real project.

## Included Files

| File | Purpose |
|---|---|
| `AGENTS.md` | Automatically discovered entry point and instruction router |
| `GOALS.md` | Project objectives, priorities, success criteria, and non-goals |
| `INSTRUCTIONS.md` | Detailed coding, testing, data, security, and Git conventions |
| `ARCHITECTURE.md` | Repository map, components, interfaces, schemas, and data flow |
| `WORKFLOW.md` | Environment setup, build, run, test, validation, and delivery commands |
| `MEMORY.md` | Verified durable facts, decisions, conventions, and reference results |
| `PLANS.md` | Execution-plan template for substantial or long-running tasks |
| `.codex/config.toml.example` | Optional example of project-scoped Codex configuration |

## Recommended Project Structure

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
    ├── config.toml.example
    └── config.toml          # Optional; active only when created
```

## Prerequisites

- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/) or a compatible editor
- The [Codex IDE extension](https://learn.chatgpt.com/docs/codex/ide), installed
  and signed in

In VS Code, open Codex from its sidebar icon. If the icon is not visible, open
the Command Palette and run **Codex: Open Codex Sidebar**.

## Installation

### Option 1: Start a new repository from this template

This is the recommended option for a new project.

1. Select **Use this template** at the top of this GitHub repository.
2. Select **Create a new repository**.
3. Choose the owner, repository name, and visibility.
4. Clone the newly created repository:

   ```bash
   git clone git@github.com:<OWNER>/<NEW_REPOSITORY>.git
   cd <NEW_REPOSITORY>
   code .
   ```

5. Replace this README with a description of the new project.
6. Customize the instruction files as described under
   [Project customization](#project-customization).

The new repository has its own Git history and is not a fork of this starter.

### Option 2: Add the files to an existing repository

Clone this starter next to the existing project:

```bash
git clone https://github.com/saeidzk/codex-vscode-starter.git
cd <EXISTING_PROJECT>
```

Copy only the Codex template files. Do not overwrite the existing project's
`README.md`, `LICENSE`, or `.git/` directory.

```bash
cp ../codex-vscode-starter/AGENTS.md .
cp ../codex-vscode-starter/GOALS.md .
cp ../codex-vscode-starter/INSTRUCTIONS.md .
cp ../codex-vscode-starter/ARCHITECTURE.md .
cp ../codex-vscode-starter/WORKFLOW.md .
cp ../codex-vscode-starter/MEMORY.md .
cp ../codex-vscode-starter/PLANS.md .

mkdir -p .codex
cp ../codex-vscode-starter/.codex/config.toml.example .codex/
```

Review the copied files before committing them:

```bash
git status --short
git diff -- AGENTS.md GOALS.md INSTRUCTIONS.md ARCHITECTURE.md \
  WORKFLOW.md MEMORY.md PLANS.md
```

## Project Customization

Open the repository root in VS Code and replace all placeholders. On systems
with `rg` installed, unresolved placeholders can be found with:

```bash
rg -n '<[^>]+>' --glob '*.md'
```

At minimum, customize:

1. `AGENTS.md`: project name, purpose, runtime, entry point, and test command.
2. `GOALS.md`: current priorities, measurable success criteria, and non-goals.
3. `INSTRUCTIONS.md`: actual formatter, linter, type checker, and Git workflow.
4. `ARCHITECTURE.md`: real directories, component boundaries, schemas, units,
   and coordinate conventions.
5. `WORKFLOW.md`: commands that have been tested in the actual environment.
6. `MEMORY.md`: only verified, durable facts and decisions.
7. `PLANS.md`: keep it as a template until a substantial task needs a written
   execution plan.

Delete sections that are irrelevant. Short, accurate instructions are more
useful than long, generic instructions.

## How the Instruction Files Work

`AGENTS.md` is the standard automatically discovered project-instruction file.
It acts as the entry point and tells Codex when the supporting documents are
relevant:

- Read `GOALS.md` when prioritizing behavior or making project choices.
- Read `INSTRUCTIONS.md` before changing code, tests, data, or dependencies.
- Read `ARCHITECTURE.md` before changing interfaces, schemas, coordinate
  systems, module boundaries, or data flow.
- Read `WORKFLOW.md` before building, running, testing, or delivering work.
- Read `MEMORY.md` when verified prior decisions or durable facts matter.
- Use `PLANS.md` for multi-file, risky, ambiguous, expensive, or long-running
  work.

Codex can also use nested `AGENTS.md` files. Guidance closer to the working
directory takes precedence, so use nested files only where a subdirectory needs
genuinely different commands or constraints.

## Using `.codex/config.toml.example`

The included `.codex/config.toml.example` is documentation only. Codex does not
load it because the filename ends in `.example`.

The example currently documents:

- `project_doc_max_bytes`: the maximum combined size of automatically loaded
  project instruction documents;
- `project_doc_fallback_filenames`: alternative instruction filenames to check
  when `AGENTS.md` is absent.

This starter uses the standard `AGENTS.md` filename, so no fallback filename is
required.

### Activate project-scoped configuration

Activate it only when the repository is trusted and the settings should apply to
the project:

```bash
cp .codex/config.toml.example .codex/config.toml
```

Then review and edit `.codex/config.toml`. Codex loads project-scoped
configuration only for trusted repositories.

If the settings should apply to every contributor, review and commit
`.codex/config.toml`. If they are personal preferences—such as model selection
or reasoning effort—put them in the user configuration instead:

```text
~/.codex/config.toml
```

Keep the `.example` file in the repository so new contributors can see the
supported project configuration without automatically activating it.

After activating or changing project configuration, start a new Codex session.

## Verify the Setup

Before committing the customized files:

```bash
git status --short
rg -n '<[^>]+>' --glob '*.md'
```

Start a new Codex session from the project root and ask:

```text
Summarize the applicable project instructions, identify unresolved
placeholders, and list the documented verification commands. Do not modify
files.
```

Confirm that the response matches the repository before asking Codex to make
changes.

## Important Guidelines

- Keep `AGENTS.md` concise and use it as the authoritative instruction router.
- Store rules at the narrowest scope where they apply.
- Keep instructions concrete, verifiable, and repository-specific.
- Add guidance after repeated mistakes or recurring review feedback.
- Use tests, linters, hooks, and continuous integration to enforce mechanical
  rules.
- Never store passwords, tokens, credentials, private personal information, or
  confidential data in these files.
- Start a new Codex session after changing applicable instruction files so the
  updated instruction chain is loaded.

## Using `MEMORY.md`

`MEMORY.md` is not a conversation transcript, daily log, or substitute for Git
history. Use it only for durable, verified information, such as:

- architectural decisions;
- domain, unit, coordinate, and sign conventions;
- validated reference results;
- important compatibility constraints;
- verified reasons a previous approach failed.

Temporary work belongs in the issue tracker or `PLANS.md`. Code history belongs
in Git. Never put credentials, personal data, or speculation in `MEMORY.md`.

## Scientific and HPC Projects

The templates include conventions useful for scientific Python, geoscience,
numerical modelling, data provenance, and HPC workflows. For scientific
repositories, document these points explicitly:

- units and sign conventions;
- coordinate reference systems and axis order;
- vertical datum and positive depth direction;
- input-data provenance and immutable raw-data locations;
- numerical tolerances and validated reference results;
- approved HPC execution environments and resource expectations;
- commands that must not run on cluster login nodes.

Remove this guidance when it does not apply to the project.

## Documentation

- [Codex IDE extension](https://learn.chatgpt.com/docs/codex/ide)
- [Custom instructions with `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Advanced Codex configuration](https://learn.chatgpt.com/docs/config-file/config-advanced)

## License

This project is available under the terms in [LICENSE](LICENSE).
