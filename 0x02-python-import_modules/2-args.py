#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    if len(arg) == 0:
        print("{} arguments.".format(0))
    elif len(arg) == 1:
        print("{} argument:".format(1))
        print("{}: {}".format(1, arg[0]))
    else:
        print("{} arguments:".format(len(arg)))
        for i in range(len(arg)):
            print("{}: {}".format(i + 1, arg[i]))
