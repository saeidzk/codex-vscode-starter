# Execution Plans

Use this file for multi-file, risky, ambiguous, or long-running work. Small
changes can use a short checklist in the Codex conversation.

## Completed Plan: Initial Catalogue Summary Workflow

- Owner: Example maintainers
- Status: complete
- Started: 2026-07-16
- Last updated: 2026-07-16

### Context

The complete example needed a small scientific workflow that made every
instruction document concrete and verifiable without third-party dependencies.

### Desired Outcome

A fictional earthquake catalogue can be loaded, validated, filtered,
summarized, tested, and documented using only Python's standard library.

### Scope

- In scope: CSV schema, event model, validation, filters, statistics, CLI,
  tests, reference output, and completed Codex documentation.
- Out of scope: real catalogues, mapping, databases, uncertainty analysis, web
  services, and HPC execution.

### Completed Steps

- [x] Define the synthetic catalogue and scientific conventions.
- [x] Implement loading, validation, filtering, statistics, and CLI formatting.
- [x] Add nine unit and regression tests.
- [x] Document executable setup, run, and verification commands.
- [x] Validate the reference output and remove unresolved placeholders.

### Validation

- Automated: `python -m unittest discover -s tests -v`
- Compilation: `python -m compileall -q catalogue.py tests`
- Manual: compare CLI output with the reference block in `WORKFLOW.md`.
- Rollback: revert the focused commit that introduced the example.

### Completion Summary

- Changed: added a complete scientific Python example with all starter files.
- Verified: nine tests, compilation, reference CLI output, and documentation.
- Remaining: no required follow-up; optional extensions should use a new plan.
