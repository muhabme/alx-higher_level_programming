#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints integer with "{:d}".format().

    if a ValueError message is caught, a message is 
    printed to standard error.

    args:
        value (int): integer to print.

    returns:
        if a TypeError or ValueError occurs - false.
        otherwise - true.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
