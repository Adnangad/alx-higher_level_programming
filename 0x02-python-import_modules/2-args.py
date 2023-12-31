#!/usr/bin/python3
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='displays arg')
    parser.add_argument('string', nargs='*')
    args = parser.parse_args()
    num = len(args.string)
    if num < 1:
        print("{} arguments.".format(num))
    elif num > 1:
        print("{} arguments:".format(num))
    else:
        print("{} argument:".format(num))
    for i in range(1, num + 1):
        print("{}: {}".format(i, args.string[i - 1]))
