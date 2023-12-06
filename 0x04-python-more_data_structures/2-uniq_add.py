#!/usr/bin/python3
def uniq_add(my_list=[]):
    rez = 0
    i = 0
    new = len(my_list) - 1
    while i  < new:
        if my_list[i] == my_list[i + 1]:
            my_list.pop(i)
        else:
            i += 1
    for k in my_list:
        rez += k
    return rez
