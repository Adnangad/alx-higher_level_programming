#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    rez = 0
    try:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end='')
                    rez += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        pass
    print()
    return rez
