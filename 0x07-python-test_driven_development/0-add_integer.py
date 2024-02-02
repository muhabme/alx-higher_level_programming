#!/usr/bin/python3
"""Defines an addition function for integers."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Floats are converted to ints before addition is performed.

    Raises:
        TypeError: If a or b is a non-integer or a non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
