"""Tests for the temperature converter."""

import unittest

from temperature import convert_temperature


class ConvertTemperatureTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self) -> None:
        self.assertAlmostEqual(convert_temperature(100.0, "C", "F"), 212.0)

    def test_fahrenheit_to_celsius(self) -> None:
        self.assertAlmostEqual(convert_temperature(32.0, "F", "C"), 0.0)

    def test_celsius_to_kelvin(self) -> None:
        self.assertAlmostEqual(convert_temperature(0.0, "C", "K"), 273.15)

    def test_kelvin_to_celsius(self) -> None:
        self.assertAlmostEqual(convert_temperature(273.15, "K", "C"), 0.0)

    def test_same_unit_returns_same_temperature(self) -> None:
        self.assertAlmostEqual(convert_temperature(18.5, "C", "C"), 18.5)

    def test_unit_names_are_case_insensitive_in_conversion_function(self) -> None:
        self.assertAlmostEqual(convert_temperature(100.0, "c", "f"), 212.0)

    def test_rejects_unsupported_source_unit(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unsupported source unit"):
            convert_temperature(10.0, "X", "C")

    def test_rejects_unsupported_target_unit(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unsupported target unit"):
            convert_temperature(10.0, "C", "X")

    def test_rejects_temperature_below_absolute_zero(self) -> None:
        with self.assertRaisesRegex(ValueError, "below absolute zero"):
            convert_temperature(-1.0, "K", "C")


if __name__ == "__main__":
    unittest.main()
