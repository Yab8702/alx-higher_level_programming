#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    summ = 0
    for argument in arg:
        summ += int(argument)
    print(summ)
