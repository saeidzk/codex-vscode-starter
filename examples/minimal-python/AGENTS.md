# Project Instructions

## Project Summary

- Project: Minimal Temperature Converter
- Purpose: Convert temperatures between Celsius, Fahrenheit, and Kelvin.
- Runtime: Python 3.10 or newer
- Main entry point: `temperature.py`
- Test command: `python -m unittest discover -s tests -v`
- Dependencies: Python standard library only

## Repository Layout

- `temperature.py`: conversion logic and command-line interface
- `tests/test_temperature.py`: unit tests
- `README.md`: installation, usage, and example commands

## Working Rules

- Inspect the relevant code and tests before editing.
- Keep the project dependency-free unless the user explicitly approves a new
  dependency.
- Preserve the command-line interface: `python temperature.py VALUE FROM TO`.
- Keep conversion logic separate from command-line parsing.
- Use type hints for public functions.
- Raise `ValueError` for unsupported units and physically impossible
  temperatures.
- Do not silently clamp temperatures below absolute zero.
- Avoid unrelated refactoring.

## Testing

- Add or update tests for every behavior change.
- Use Python's built-in `unittest` framework.
- Use `assertAlmostEqual` for floating-point conversion results.
- Run the complete documented test command after modifying Python files.
- Do not weaken or delete existing tests merely to make a change pass.

## Documentation

- Update `README.md` if command-line usage or supported units change.
- Keep examples executable and synchronized with the actual interface.

## Definition of Done

A change is complete when:

- The requested behavior works.
- Relevant tests have been added or updated.
- `python -m unittest discover -s tests -v` passes.
- User-facing behavior is documented when necessary.
- Unrelated files remain unchanged.

