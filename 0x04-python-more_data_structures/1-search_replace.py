#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for i, el in enumerate(my_list):
        if el == search:
            new.append(replace)
        else:
            new.append(el)
    return new
