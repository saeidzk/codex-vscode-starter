# Project Instructions

## Purpose

This is a completed scientific Python example for the Codex VS Code Starter
Kit. It processes a fictional four-event earthquake catalogue.

## Read Before Working

- Read `GOALS.md` before changing project scope or scientific behavior.
- Read `INSTRUCTIONS.md` before editing code, data, or tests.
- Read `ARCHITECTURE.md` before changing the CSV schema, units, interfaces, or
  data flow.
- Read `WORKFLOW.md` before running or verifying the project.
- Read `MEMORY.md` when reference results or prior decisions matter.
- Use `PLANS.md` for multi-file, risky, or long-running changes.

## Project Summary

- Project: Synthetic Earthquake Catalogue Summary
- Runtime: Python 3.10 or newer
- Main entry point: `catalogue.py`
- Input: `data/sample_events.csv`
- Test command: `python -m unittest discover -s tests -v`
- Dependencies: Python standard library only

## Working Agreement

- Preserve the documented CSV schema, units, and coordinate conventions.
- Treat `data/sample_events.csv` as immutable reference input.
- Keep the catalogue explicitly identified as synthetic.
- Keep scientific calculations separate from command-line parsing.
- Do not add dependencies without explicit user approval.
- Add or update tests for behavior changes.
- Avoid unrelated refactoring and preserve user changes.
- Do not commit, push, publish, or submit external work unless requested.

## Definition of Done

A task is complete when the requested behavior works, relevant tests exist, the
commands in `WORKFLOW.md` pass, documentation matches the interface, scientific
conventions remain explicit, and unrelated files are unchanged.

