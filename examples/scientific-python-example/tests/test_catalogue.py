"""Tests for the synthetic earthquake catalogue workflow."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from catalogue import (
    filter_events,
    format_summary,
    load_catalogue,
    summarize_catalogue,
)


DATA_PATH = Path(__file__).parents[1] / "data" / "sample_events.csv"


class CatalogueTests(unittest.TestCase):
    def setUp(self) -> None:
        self.events = load_catalogue(DATA_PATH)

    def test_loads_all_sample_events(self) -> None:
        self.assertEqual(len(self.events), 4)

    def test_parses_units_and_values(self) -> None:
        event = self.events[0]
        self.assertEqual(event.event_id, "syn-001")
        self.assertAlmostEqual(event.latitude_deg, 49.120)
        self.assertAlmostEqual(event.depth_km, 5.2)

    def test_calculates_reference_summary(self) -> None:
        summary = summarize_catalogue(self.events)
        self.assertEqual(summary.event_count, 4)
        self.assertAlmostEqual(summary.mean_magnitude, 2.875)
        self.assertAlmostEqual(summary.maximum_magnitude, 4.0)
        self.assertAlmostEqual(summary.mean_depth_km, 13.925)

    def test_filters_by_minimum_magnitude(self) -> None:
        selected = filter_events(self.events, minimum_magnitude=2.9)
        self.assertEqual([event.event_id for event in selected], ["syn-003", "syn-004"])

    def test_filters_by_maximum_depth(self) -> None:
        selected = filter_events(self.events, maximum_depth_km=10.0)
        self.assertEqual([event.event_id for event in selected], ["syn-001", "syn-002"])

    def test_combines_magnitude_and_depth_filters(self) -> None:
        selected = filter_events(
            self.events,
            minimum_magnitude=2.5,
            maximum_depth_km=20.0,
        )
        self.assertEqual([event.event_id for event in selected], ["syn-002", "syn-003"])

    def test_rejects_empty_summary(self) -> None:
        with self.assertRaisesRegex(ValueError, "empty catalogue"):
            summarize_catalogue([])

    def test_rejects_missing_required_column(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.csv"
            path.write_text("event_id,magnitude\nsyn-001,2.0\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Missing required CSV columns"):
                load_catalogue(path)

    def test_formats_documented_reference_output(self) -> None:
        expected = "\n".join(
            [
                "Events: 4",
                "Mean magnitude: 2.88",
                "Maximum magnitude: 4.00",
                "Mean depth: 13.93 km",
            ]
        )
        self.assertEqual(format_summary(summarize_catalogue(self.events)), expected)


if __name__ == "__main__":
    unittest.main()
