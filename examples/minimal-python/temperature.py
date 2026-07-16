"""Convert temperatures between Celsius, Fahrenheit, and Kelvin."""

from __future__ import annotations

import argparse


SUPPORTED_UNITS = {"C", "F", "K"}


def _to_kelvin(value: float, unit: str) -> float:
    """Convert a temperature to Kelvin."""
    if unit == "C":
        return value + 273.15
    if unit == "F":
        return (value - 32.0) * 5.0 / 9.0 + 273.15
    return value


def _from_kelvin(value: float, unit: str) -> float:
    """Convert a temperature in Kelvin to the requested unit."""
    if unit == "C":
        return value - 273.15
    if unit == "F":
        return (value - 273.15) * 9.0 / 5.0 + 32.0
    return value


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a temperature between Celsius, Fahrenheit, and Kelvin.

    Args:
        value: Temperature value to convert.
        from_unit: Input unit: ``C``, ``F``, or ``K``.
        to_unit: Output unit: ``C``, ``F``, or ``K``.

    Returns:
        The converted temperature.

    Raises:
        ValueError: If a unit is unsupported or the temperature is below
            absolute zero.
    """
    source = from_unit.upper()
    target = to_unit.upper()

    if source not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if target not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    kelvin = _to_kelvin(value, source)
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero")

    return _from_kelvin(kelvin, target)


def _parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius, Fahrenheit, and Kelvin."
    )
    parser.add_argument("value", type=float, help="temperature value")
    parser.add_argument("from_unit", choices=sorted(SUPPORTED_UNITS))
    parser.add_argument("to_unit", choices=sorted(SUPPORTED_UNITS))
    return parser.parse_args()


def main() -> None:
    """Run the command-line interface."""
    args = _parse_args()

    try:
        result = convert_temperature(args.value, args.from_unit, args.to_unit)
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

    print(
        f"{args.value:.2f} °{args.from_unit} = "
        f"{result:.2f} °{args.to_unit}"
    )


if __name__ == "__main__":
    main()

