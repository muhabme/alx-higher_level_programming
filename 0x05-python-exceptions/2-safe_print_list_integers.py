#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print first x integer elements of a list.

    args:
        my_list (list): list to print elements from.
        x (int): number of elements in my_list to print.

    returns:
        number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
