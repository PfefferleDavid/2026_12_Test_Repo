import math


def circle_area(radius: float) -> float:
    """Return a circle's area in square units for a non-negative radius."""
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return math.pi * radius ** 2