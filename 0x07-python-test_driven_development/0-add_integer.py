#!/usr/bin/python3
# 0-add_integer.py

"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if ((not isinstance(a, int) and not isinstance(a, bool))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, bool))):
        raise TypeError("b must be an integer")
    return (a + b)
