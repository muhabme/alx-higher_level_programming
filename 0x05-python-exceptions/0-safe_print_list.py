#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elememts of list.

    args:
        my_list (list): list to print elements from.
        x (int): number of elements in my_list to print.

    returns:
        number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
