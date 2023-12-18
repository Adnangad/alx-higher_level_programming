#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
        print()
        return x
    except (IndexError):
        print()
        rez = 0
        for j in my_list:
            rez += 1
        return rez
