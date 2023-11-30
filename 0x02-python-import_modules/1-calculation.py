#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    read = calc.add(a, b)
    resub = calc.sub(a, b)
    rediv = calc.div(a, b)
    remul = calc.mul(a, b)
    print("{} + {} = {}".format(a, b, read))
    print("{} - {} = {}".format(a, b, resub))
    print("{} * {} = {}".format(a, b, remul))
    print("{} / {} = {}".format(a, b, rediv))
