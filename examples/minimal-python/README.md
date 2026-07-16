# Minimal Python Example

This directory demonstrates the smallest practical Codex setup for a Python
project. It contains a working temperature-conversion command-line program,
unit tests, and one project-specific `AGENTS.md`.

Small projects do not need `GOALS.md`, `ARCHITECTURE.md`, `MEMORY.md`, or the
other supporting templates unless those files provide useful project context.
Start with `AGENTS.md` and add supporting documents only when the project grows.

## Structure

```text
minimal-python/
├── AGENTS.md
├── README.md
├── temperature.py
└── tests/
    └── test_temperature.py
```

## Requirements

- Python 3.10 or newer
- No third-party packages

## Run the Program

From this directory:

```bash
python temperature.py 100 C F
```

Expected output:

```text
100.00 °C = 212.00 °F
```

Other examples:

```bash
python temperature.py 32 F C
python temperature.py 0 C K
python temperature.py 273.15 K C
```

Supported units are `C`, `F`, and `K`.

## Run the Tests

```bash
python -m unittest discover -s tests -v
```

## Try It with Codex

Open this directory in VS Code, start a new Codex session, and ask:

```text
Summarize the project instructions and run the documented tests. Do not modify
any files.
```

Then try a small implementation request:

```text
Add support for converting temperatures from command-line input written as
lowercase unit names, while preserving the existing interface and tests.
```

Before accepting changes, confirm that Codex followed `AGENTS.md`, added or
updated appropriate tests, and ran the documented test command.

## What This Example Demonstrates

- `AGENTS.md` can be sufficient for a small repository.
- Instructions should contain real paths and verified commands.
- The definition of done should include proportionate testing.
- The example has no unresolved placeholders.
- Supporting instruction files should be introduced because they are useful,
  not merely because templates exist.

