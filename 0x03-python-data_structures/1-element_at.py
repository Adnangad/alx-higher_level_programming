#!/usr/bin/python3
def element_at(my_list, idx):
    leng = len(my_list)
    if idx < 0:
        return None
    if idx >= leng:
        return None
    else:
        return my_list[idx]
