#!/usr/bin/python3
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='adds arg')
    parser.add_argument('add', type=int, nargs='*')
    args = parser.parse_args()
    num = sum(args.add)
    print("{}".format(num))
