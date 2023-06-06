#!/usr/bin/python3
delm = ", "
for number in range(0, 100):
    if number < 10:
        print("{}".format(0), end="")
    if number == 99:
        delm = "\n"
    print("{}".format(number), end=delm)
