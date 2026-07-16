"""Read, filter, and summarize a small synthetic earthquake catalogue."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REQUIRED_COLUMNS = {
    "event_id",
    "time_utc",
    "latitude_deg",
    "longitude_deg",
    "depth_km",
    "magnitude",
}


@dataclass(frozen=True)
class Event:
    """One event from the synthetic earthquake catalogue."""

    event_id: str
    time_utc: str
    latitude_deg: float
    longitude_deg: float
    depth_km: float
    magnitude: float


@dataclass(frozen=True)
class CatalogueSummary:
    """Summary statistics for a non-empty sequence of events."""

    event_count: int
    mean_magnitude: float
    maximum_magnitude: float
    mean_depth_km: float


def _parse_event(row: dict[str, str], row_number: int) -> Event:
    """Validate and convert one CSV row."""
    try:
        event = Event(
            event_id=row["event_id"].strip(),
            time_utc=row["time_utc"].strip(),
            latitude_deg=float(row["latitude_deg"]),
            longitude_deg=float(row["longitude_deg"]),
            depth_km=float(row["depth_km"]),
            magnitude=float(row["magnitude"]),
        )
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(f"Invalid catalogue value in CSV row {row_number}") from error

    if not event.event_id:
        raise ValueError(f"Missing event_id in CSV row {row_number}")
    if not event.time_utc:
        raise ValueError(f"Missing time_utc in CSV row {row_number}")
    if not -90.0 <= event.latitude_deg <= 90.0:
        raise ValueError(f"Invalid latitude in CSV row {row_number}")
    if not -180.0 <= event.longitude_deg <= 180.0:
        raise ValueError(f"Invalid longitude in CSV row {row_number}")
    if event.depth_km < 0.0:
        raise ValueError(f"Depth cannot be negative in CSV row {row_number}")

    return event


def load_catalogue(path: str | Path) -> list[Event]:
    """Load and validate catalogue events from a UTF-8 CSV file."""
    source = Path(path)
    with source.open("r", encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        columns = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - columns
        if missing:
            missing_list = ", ".join(sorted(missing))
            raise ValueError(f"Missing required CSV columns: {missing_list}")

        return [_parse_event(row, row_number) for row_number, row in enumerate(reader, 2)]


def filter_events(
    events: Iterable[Event],
    *,
    minimum_magnitude: float | None = None,
    maximum_depth_km: float | None = None,
) -> list[Event]:
    """Return events satisfying optional magnitude and depth thresholds."""
    if maximum_depth_km is not None and maximum_depth_km < 0.0:
        raise ValueError("maximum_depth_km cannot be negative")

    selected = []
    for event in events:
        if minimum_magnitude is not None and event.magnitude < minimum_magnitude:
            continue
        if maximum_depth_km is not None and event.depth_km > maximum_depth_km:
            continue
        selected.append(event)
    return selected


def summarize_catalogue(events: Iterable[Event]) -> CatalogueSummary:
    """Calculate summary statistics for a non-empty event collection."""
    event_list = list(events)
    if not event_list:
        raise ValueError("Cannot summarize an empty catalogue")

    return CatalogueSummary(
        event_count=len(event_list),
        mean_magnitude=sum(event.magnitude for event in event_list) / len(event_list),
        maximum_magnitude=max(event.magnitude for event in event_list),
        mean_depth_km=sum(event.depth_km for event in event_list) / len(event_list),
    )


def format_summary(summary: CatalogueSummary) -> str:
    """Format summary statistics for terminal output."""
    return "\n".join(
        [
            f"Events: {summary.event_count}",
            f"Mean magnitude: {summary.mean_magnitude:.2f}",
            f"Maximum magnitude: {summary.maximum_magnitude:.2f}",
            f"Mean depth: {summary.mean_depth_km:.2f} km",
        ]
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize a synthetic earthquake catalogue."
    )
    parser.add_argument("catalogue", type=Path, help="input CSV catalogue")
    parser.add_argument(
        "--min-magnitude",
        type=float,
        default=None,
        help="retain events at or above this magnitude",
    )
    parser.add_argument(
        "--max-depth-km",
        type=float,
        default=None,
        help="retain events at or shallower than this depth in kilometres",
    )
    return parser.parse_args()


def main() -> None:
    """Run the catalogue summary command-line interface."""
    args = _parse_args()
    try:
        events = load_catalogue(args.catalogue)
        selected = filter_events(
            events,
            minimum_magnitude=args.min_magnitude,
            maximum_depth_km=args.max_depth_km,
        )
        summary = summarize_catalogue(selected)
    except (OSError, ValueError) as error:
        raise SystemExit(f"Error: {error}") from error

    print(format_summary(summary))


if __name__ == "__main__":
    main()

