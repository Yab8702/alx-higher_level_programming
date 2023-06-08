#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    a = sys.argv[1:]
    if len(a) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a[0] = int(a[0])
        a[2] = int(a[2])
    if a[1] == '+':
        print("{} {} {} = {}".format(a[0], a[1], a[2], add(a[0], a[2])))
    elif a[1] == '-':
        print("{} {} {} = {}".format(a[0], a[1], a[2], sub(a[0], a[2])))
    elif a[1] == '*':
        print("{} {} {} = {}".format(a[0], a[1], a[2], mul(a[0], a[2])))
    elif a[1] == '/':
        print("{} {} {} = {}".format(a[0], a[1], a[2], div(a[0], a[2])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
