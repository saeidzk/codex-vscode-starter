# Durable Project Memory

This file stores verified facts and decisions, not conversation history,
temporary tasks, credentials, or speculation.

## Stable Facts

- The project uses only the Python standard library; verified 2026-07-16.
- `data/sample_events.csv` contains four fictional events; verified 2026-07-16.
- Coordinates use WGS 84 decimal degrees; verified against `ARCHITECTURE.md` on
  2026-07-16.
- Depth uses kilometres and is positive downward; verified 2026-07-16.
- The catalogue is synthetic and is not suitable for scientific interpretation.

## Decisions

### 2026-07-16 — Keep the Example Dependency-Free

- Decision: Use `csv`, `dataclasses`, `argparse`, and `unittest` from the Python
  standard library.
- Reason: Users should be able to run the example immediately after cloning.
- Alternative considered: pandas and pytest.
- Consequence: The example favors transparency over large-data performance.

### 2026-07-16 — Preserve Raw Example Data

- Decision: Treat `data/sample_events.csv` as immutable reference input.
- Reason: Stable input makes the documented output and regression tests
  reproducible.
- Consequence: Tests create temporary files when invalid input is needed.

## Validated Reference Results

| Result | Expected value | Tolerance or formatting | Evidence |
|---|---:|---|---|
| Event count | 4 | Exact | `tests/test_catalogue.py` |
| Mean magnitude | 2.875 | Floating-point comparison | `tests/test_catalogue.py` |
| Maximum magnitude | 4.0 | Floating-point comparison | `tests/test_catalogue.py` |
| Mean depth | 13.925 km | Floating-point comparison | `tests/test_catalogue.py` |

The CLI rounds the mean magnitude to `2.88` and mean depth to `13.93 km`.

## Known Constraints

- The example supports Python 3.10 or newer because it uses modern union type
  syntax.
- Summary generation rejects an empty selection.
- The example intentionally does not parse timestamp semantics or magnitude
  types.

