#!/usr/bin/python3
def best_score(a_dictionary):
    ls = []
    for i, j in a_dictionary.items():
        ls.append(j)
    k = len(ls) - 1
    while k >= 0:
        l = 0
        while l < k:
            if ls[l] > ls[l + 1]:
                temp = ls[l]
                ls[l] = ls[l + 1]
                ls[l + 1] = temp
            l += 1
        k -= 1
    return ls[-1]
