# Project Goals

## Mission

Provide a small, reproducible scientific Python example that demonstrates how
the complete Codex instruction set guides code, testing, data handling,
documentation, and validation.

## Current Priorities

1. Keep the reference workflow correct and dependency-free.
2. Make all scientific units and assumptions explicit.
3. Demonstrate a complete but understandable Codex project configuration.

## Success Criteria

- All nine unit tests pass with Python 3.10 or newer.
- The reference CLI output matches the validated values in `MEMORY.md`.
- The example contains no unresolved template placeholders.
- A new contributor can run the project using only `README.md` and
  `WORKFLOW.md`.

## Non-goals

- Representing real seismicity or supporting scientific interpretation.
- Replacing a production earthquake catalogue library.
- Adding mapping, database, web-service, or HPC functionality.
- Optimizing performance for large catalogues.

## Users and Use Cases

| User | Need | Expected outcome |
|---|---|---|
| Codex user | Understand project instruction files | See every template completed consistently |
| Python learner | Run a scientific example | Execute a CLI and nine unit tests |
| Research developer | See data conventions documented | Identify units, CRS, depth sign, and provenance |

## Decision Principles

Prefer correctness and scientific clarity, then reproducibility, simplicity,
maintainability, and finally performance after measurement.

