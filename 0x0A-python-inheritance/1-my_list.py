#!/usr/bin/python3
"""
This is a module that contains a subclass.
"""


class MyList(list):
    """
    This is a subclass that inherits from a list.
    """
    def print_sorted(self):
        if not all(isinstance(i, int)for i in self):
            raise TypeError("List should contain integers only")
        print(sorted(self))
