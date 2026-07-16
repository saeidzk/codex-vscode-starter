# Complete Scientific Python Example

This completed example shows how all files from the Codex VS Code Starter Kit
can work together in a small scientific project. It reads a synthetic earthquake
catalogue, applies magnitude and depth filters, and reports summary statistics.

The catalogue is fictional and intended only for testing and documentation. It
must not be interpreted as an observed seismic catalogue.

## Structure

```text
complete-scientific-python/
├── .codex/
│   └── config.toml.example
├── data/
│   └── sample_events.csv
├── tests/
│   └── test_catalogue.py
├── .gitignore
├── AGENTS.md
├── ARCHITECTURE.md
├── GOALS.md
├── INSTRUCTIONS.md
├── MEMORY.md
├── PLANS.md
├── README.md
├── WORKFLOW.md
└── catalogue.py
```

## Requirements

- Python 3.10 or newer
- No third-party packages

## Run

From this directory:

```bash
python catalogue.py data/sample_events.csv
```

Reference output:

```text
Events: 4
Mean magnitude: 2.88
Maximum magnitude: 4.00
Mean depth: 13.93 km
```

Apply optional filters:

```bash
python catalogue.py data/sample_events.csv --min-magnitude 2.5
python catalogue.py data/sample_events.csv --max-depth-km 15
python catalogue.py data/sample_events.csv --min-magnitude 2.5 --max-depth-km 20
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Verify the Documented Workflow

```bash
python -m compileall -q catalogue.py tests
python -m unittest discover -s tests -v
python catalogue.py data/sample_events.csv
```

## Try It with Codex

Open this directory in VS Code, start a new Codex session, and ask:

```text
Summarize the applicable project instructions, explain the scientific data
conventions, and run the documented fast verification. Do not modify files.
```

Then try a focused task:

```text
Add an optional maximum-magnitude filter to the Python API and command-line
interface. Update the documentation and tests, then run full verification.
```

## Codex Configuration Example

`.codex/config.toml.example` is inactive documentation. In a trusted copy of
the project, activate it with:

```bash
cp .codex/config.toml.example .codex/config.toml
```

Review the file before activation and start a new Codex session afterward.

## What This Example Demonstrates

- `AGENTS.md` routes Codex to the supporting project documents.
- Scientific units, coordinate conventions, and provenance are explicit.
- All setup, run, and verification commands are executable.
- `MEMORY.md` stores only verified durable facts and reference results.
- `PLANS.md` records a completed example plan rather than chat history.
- The project is dependency-free and all nine tests pass.

