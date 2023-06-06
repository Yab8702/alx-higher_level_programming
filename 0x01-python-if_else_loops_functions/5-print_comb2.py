#!/usr/bin/python3
delm = ", "
for number in range(0, 100):
    if number < 10:
        print("0", end="")
    if number == 99:
        delm = "\n"
    print(f"{number}", end=delm)
