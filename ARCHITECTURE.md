# Architecture

## System overview

`<Describe the system in one short paragraph.>`

## Repository map

| Path | Responsibility | Important constraints |
|---|---|---|
| `<PATH>` | `<PURPOSE>` | `<CONSTRAINTS>` |
| `<PATH>` | `<PURPOSE>` | `<CONSTRAINTS>` |

## Components

### `<COMPONENT_NAME>`

- Responsibility: `<WHAT_IT_OWNS>`
- Inputs: `<INPUTS>`
- Outputs: `<OUTPUTS>`
- Public interfaces: `<API_OR_FILES>`
- Must not: `<BOUNDARY_OR_PROHIBITION>`

## Data flow

1. `<SOURCE>` produces `<DATA_AND_FORMAT>`.
2. `<PROCESS>` validates/transforms it.
3. `<DESTINATION>` stores or consumes the result.

## Data and coordinate conventions

- Canonical CRS: `<EPSG_OR_DESCRIPTION>`
- Horizontal units: `<UNITS>`
- Vertical datum/convention: `<DATUM_AND_POSITIVE_DIRECTION>`
- Time zone/calendar: `<CONVENTION>`
- Missing-value convention: `<CONVENTION>`
- Canonical file/schema definitions: `<PATHS>`

## External systems

| System | Purpose | Interface | Failure behavior |
|---|---|---|---|
| `<SYSTEM>` | `<PURPOSE>` | `<API_FILE_OR_PROTOCOL>` | `<EXPECTED_HANDLING>` |

## Architectural invariants

- `<Rule that must remain true across changes>`
- `<Boundary that components must respect>`
- `<Compatibility or data-integrity guarantee>`

## Known limitations and technical debt

- `<LIMITATION>` — impact: `<IMPACT>` — tracking: `<ISSUE_OR_OWNER>`

