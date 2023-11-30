#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hd
    for i in dir(hd):
        if i[0:2] != "__":
            print("{}".format(i))
