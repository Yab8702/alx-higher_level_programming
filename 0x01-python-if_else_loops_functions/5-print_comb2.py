#!/usr/bin/python3
delm = ", "
for num in range(0, 100):
    if num < 10:
        print(f"{0}", end="")
    if num == 99:
        delm = "\n"
    print(f"{num}", end=delm)
