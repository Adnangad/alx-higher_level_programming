#!/usr/bin/python3
def element_at(my_list, idx):
    pd = my_list.pop(idx)
    leng = len(my_list)
    if idx < 0:
        return None
    elif idx >= leng:
        return None
    else:
        return pd
