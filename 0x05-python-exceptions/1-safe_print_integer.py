#!/usr/bin/python3

def safe_print_integer(value):
    """Prints integer with "{:d}".format().

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
        return (False)
