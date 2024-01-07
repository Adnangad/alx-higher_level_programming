#!/usr/bin/python3
"""This module prints texts."""


def text_indentation(text):
    """This adds new lines after symbols.

    Args:
    text (str):the string to be printed

    Return:
    None.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sp = ['.', '?', ':']
    rez = []
    hp = ''
    for i in text:
        hp += i
        if i in sp:
            rez.append(hp.strip())
            rez.append('')
            hp =''
    if hp:
        rez.append(hp.strip())
    for hp in rez:
        print(hp)
