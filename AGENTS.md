# AGENTS.md

## Purpose

This file is the authoritative entry point for AI coding agents in this
repository. Follow it for every task. Prefer repository evidence over guesses.

## Instruction precedence

1. The user's current request.
2. This file and any closer nested `AGENTS.md` applicable to the edited file.
3. The supporting project documents linked below.
4. Existing code, tests, configuration, and established repository patterns.

If instructions conflict or a change would exceed the requested scope, stop and
ask for clarification.

## Read before working

- Read `GOALS.md` when prioritizing behavior or making product/research choices.
- Read `INSTRUCTIONS.md` before modifying code, data, tests, or dependencies.
- Read `ARCHITECTURE.md` before changing module boundaries, interfaces, schemas,
  coordinate systems, or data flow.
- Read `WORKFLOW.md` before building, running, testing, or delivering changes.
- Read `MEMORY.md` when prior decisions or durable project facts matter.
- Use `PLANS.md` for multi-file, risky, ambiguous, or long-running tasks.

Do not read every supporting document mechanically for a trivial task. Read the
smallest relevant set.

## Project summary

- Project: `<PROJECT_NAME>`
- Purpose: `<ONE_SENTENCE_PURPOSE>`
- Primary language/runtime: `<LANGUAGE_AND_VERSION>`
- Main entry point: `<PATH_OR_COMMAND>`
- Test command: `<TEST_COMMAND>`

## Working agreement

- Inspect relevant files and current Git status before editing.
- Preserve user changes and avoid unrelated modifications.
- Prefer the smallest maintainable change that satisfies the request.
- Follow existing patterns unless they conflict with documented requirements.
- Do not invent APIs, file formats, units, schemas, or scientific assumptions.
- Do not add or upgrade dependencies without a clear need and explicit report.
- Never expose secrets or place credentials in source files, logs, or examples.
- Do not commit, push, publish, deploy, submit jobs, or contact people unless the
  user explicitly requests it.
- Ask before destructive, irreversible, expensive, or externally visible work.

## Definition of done

A task is complete when:

- The requested outcome is implemented or answered.
- Relevant checks from `WORKFLOW.md` pass, or limitations are reported.
- New behavior is tested when practical.
- Documentation is updated when interfaces or usage changed.
- Units, assumptions, and data provenance are preserved where relevant.
- The final report lists changed files, verification, and remaining risks.

## Nested guidance

Add nested `AGENTS.md` files only for directories that genuinely need different
commands or constraints. Keep general rules here and specialized rules close to
the code they govern.

