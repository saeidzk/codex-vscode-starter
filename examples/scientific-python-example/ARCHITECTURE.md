# Architecture

## System Overview

The project is a single-process, standard-library Python workflow. A CSV reader
converts validated rows into immutable `Event` objects. Optional filters select
events, summary functions calculate statistics, and the CLI formats the result.

## Repository Map

| Path | Responsibility | Important constraint |
|---|---|---|
| `catalogue.py` | Data model, CSV loading, validation, filtering, summary, and CLI | Keep scientific logic callable without the CLI |
| `data/sample_events.csv` | Immutable fictional input catalogue | Never describe it as observed data |
| `tests/test_catalogue.py` | Unit and regression tests | Preserve the documented reference values |
| `AGENTS.md` | Instruction entry point | Keep routing and completion rules concise |
| Supporting Markdown files | Goals, conventions, architecture, workflow, memory, and plans | Keep facts consistent across documents |

## Data Flow

1. `load_catalogue` reads UTF-8 CSV data.
2. Row validation creates immutable `Event` instances.
3. `filter_events` applies optional magnitude and depth thresholds.
4. `summarize_catalogue` calculates count, magnitude, and depth statistics.
5. `format_summary` produces stable terminal output.

## CSV Schema

| Column | Type | Unit or convention |
|---|---|---|
| `event_id` | text | Unique synthetic identifier |
| `time_utc` | text | ISO 8601 UTC timestamp ending in `Z` |
| `latitude_deg` | float | WGS 84 latitude in decimal degrees |
| `longitude_deg` | float | WGS 84 longitude in decimal degrees |
| `depth_km` | float | Kilometres, positive downward |
| `magnitude` | float | Unitless synthetic magnitude |

## Invariants

- Latitude is between -90 and 90 degrees.
- Longitude is between -180 and 180 degrees.
- Depth is not negative.
- Summary statistics require at least one selected event.
- Filters do not mutate input events.
- No function interprets the fictional events as real observations.

## Known Limitations

- Timestamps are preserved as validated non-empty text rather than parsed.
- Magnitude type is not distinguished.
- The whole catalogue is loaded into memory.
- The example does not perform spatial or uncertainty analysis.

