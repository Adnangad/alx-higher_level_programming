#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    rez = 0
    for i in range(list_length):
        try:
            rez = my_list_1[i] / my_list_2[i]            
        except TypeError:
            print("wrong type")
            rez = 0
        except ZeroDivisionError:
            print("division by 0")
            rez = 0
        except IndexError:
            print("out of range")
            rez = 0
        finally:
            new.append(rez)
    return new
