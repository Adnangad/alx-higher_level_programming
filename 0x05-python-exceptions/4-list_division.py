#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new = []
        for i in range(list_length):
            try:
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    if my_list_2[i] == 0:
                        raise ZeroDivisionError
                    rez = my_list_1[i] / my_list_2[i]
                    new.append(rez)
                else:
                    print("wrong type")
                    new.append(0)
            except ZeroDivisionError:
                print("division by 0")
                new.append(0)
            except TypeError:
                print("wrong type")
                new.append(0)
            except IndexError:
                print("out of range")
                new.append(0)
    except TypeError:
        print("iterable")
        return []
    else:
        return new
