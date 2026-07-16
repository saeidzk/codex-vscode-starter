# Development Workflow

Replace placeholders with commands that have been tested in this repository.

## Prerequisites

- OS/platform: `<SUPPORTED_PLATFORM>`
- Runtime/toolchain: `<VERSIONS>`
- External services/data: `<REQUIREMENTS>`

## Setup

```bash
<ENVIRONMENT_SETUP_COMMANDS>
```

## Build

```bash
<BUILD_COMMAND>
```

## Run locally

```bash
<RUN_COMMAND>
```

## Fast verification

Use during normal iteration:

```bash
<TARGETED_TEST_COMMAND>
<LINT_COMMAND>
```

## Full verification

Use before delivery when scope and runtime justify it:

```bash
<FULL_TEST_COMMAND>
<TYPECHECK_COMMAND>
<BUILD_OR_INTEGRATION_COMMAND>
```

## Expensive or HPC workflows

- Command/job script: `<PATH_OR_COMMAND>`
- Approved execution environment: `<CLUSTER_OR_RUNNER>`
- Expected resources and runtime: `<RESOURCES>`
- Never run on: `<LOGIN_NODE_OR_LOCAL_MACHINE>`
- Require explicit user approval before job submission or cancellation.

## Debugging order

1. Reproduce with the smallest relevant command.
2. Capture the exact error and environment/version information.
3. Inspect the nearest code, configuration, and recent changes.
4. Form and test one hypothesis at a time.
5. Add a regression test when a code defect is fixed.

## Delivery checklist

- Review the final diff for unrelated changes.
- Run proportionate checks and record results.
- Update documentation and examples if usage changed.
- Mention migrations, compatibility concerns, assumptions, and unverified areas.

