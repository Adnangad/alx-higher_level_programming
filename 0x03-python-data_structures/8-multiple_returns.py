#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return (0, None)
    tup = (len(sentence), sentence[0])
    return tup
