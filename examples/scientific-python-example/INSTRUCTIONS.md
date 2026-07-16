# Detailed Project Instructions

## Scope

- Make only changes required by the current task.
- Preserve backward compatibility unless a breaking change is requested.
- Do not turn a focused change into a broad refactor.

## Python

- Support Python 3.10 or newer.
- Use the standard library unless a dependency is explicitly approved.
- Use type hints and concise docstrings for public functions and data classes.
- Keep file input, validation, filtering, statistics, formatting, and CLI
  responsibilities distinct.
- Prefer clear loops and expressions over premature abstraction.

## Scientific Data

- Treat `data/sample_events.csv` as immutable.
- Preserve the schema documented in `ARCHITECTURE.md`.
- Use WGS 84 geographic coordinates in decimal degrees.
- Use depth in kilometres, positive downward from the reference surface.
- Treat magnitude as a unitless synthetic example value.
- Use UTC timestamps in ISO 8601 format ending in `Z`.
- Reject invalid coordinates, negative depth, missing identifiers, and missing
  required columns rather than silently repairing them.

## Testing

- Use the built-in `unittest` framework.
- Add or update a test for every behavior change.
- Use `assertAlmostEqual` for floating-point results.
- Do not weaken assertions or replace reference results only to make tests pass.
- Run fast and full checks from `WORKFLOW.md` after relevant changes.

## Security and Privacy

- Never introduce secrets, credentials, or personal data.
- Keep example data fictional and clearly labelled as synthetic.
- Treat external CSV input as untrusted and validate it at the boundary.

## Git and Documentation

- Inspect Git status before and after editing.
- Do not overwrite unrelated uncommitted work.
- Update `README.md`, `ARCHITECTURE.md`, and tests when the CLI or schema changes.
- Do not commit or push unless the user requests it.

