# Development Workflow

Run all commands from the root of this example.

## Prerequisites

- Python 3.10 or newer
- No third-party dependencies or external services

Confirm the interpreter:

```bash
python --version
```

## Run the Reference Workflow

```bash
python catalogue.py data/sample_events.csv
```

## Fast Verification

Use during normal iteration:

```bash
python -m unittest discover -s tests -p 'test_catalogue.py' -v
```

## Full Verification

Use before delivery:

```bash
python -m compileall -q catalogue.py tests
python -m unittest discover -s tests -v
python catalogue.py data/sample_events.csv
```

The final command must produce:

```text
Events: 4
Mean magnitude: 2.88
Maximum magnitude: 4.00
Mean depth: 13.93 km
```

## Debugging Order

1. Reproduce the problem using the smallest relevant command.
2. Check the Python version and exact input path.
3. Inspect the CSV header, values, units, and missing fields.
4. Test one hypothesis at a time.
5. Add a regression test when fixing a defect.

## Delivery Checklist

- Review the final diff for unrelated changes.
- Run full verification.
- Confirm that reference output and documentation agree.
- Check that scientific units and synthetic provenance remain explicit.
- Report any check that could not be completed.

