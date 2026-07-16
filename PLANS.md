# Execution Plans

Use an execution plan for work that is multi-file, risky, ambiguous, expensive,
or expected to continue across sessions. For small changes, a short task list in
the conversation is enough.

Keep only the active plan here, or store completed plans under `docs/plans/`.

## Plan: `<OUTCOME>`

- Owner: `<PERSON_OR_TEAM>`
- Status: `draft | active | blocked | complete`
- Started: `<YYYY-MM-DD>`
- Last updated: `<YYYY-MM-DD>`

### Context

`<Why this work is needed and what currently happens.>`

### Desired outcome

`<Observable end state.>`

### Scope

- In scope: `<ITEMS>`
- Out of scope: `<ITEMS>`

### Constraints and risks

- `<CONSTRAINT_OR_RISK>` — mitigation: `<MITIGATION>`

### Steps

- [ ] Inspect `<FILES_SYSTEM_OR_DATA>` and confirm assumptions.
- [ ] Implement `<SMALLEST_COHERENT_CHANGE>`.
- [ ] Add or update `<TESTS_VALIDATION_OR_DOCS>`.
- [ ] Run `<VERIFICATION_COMMANDS>`.
- [ ] Review the diff and document remaining risks.

### Validation

- Automated: `<COMMANDS_AND_EXPECTED_RESULTS>`
- Manual/scientific: `<CHECKS_AND_ACCEPTANCE_CRITERIA>`
- Rollback: `<HOW_TO_REVERT_SAFELY>`

### Progress log

- `<YYYY-MM-DD>` — `<FACTUAL_PROGRESS_OR_DECISION>`

### Completion summary

- Changed: `<FILES_AND_BEHAVIOR>`
- Verified: `<CHECKS>`
- Remaining: `<LIMITATIONS_OR_FOLLOW_UP>`

