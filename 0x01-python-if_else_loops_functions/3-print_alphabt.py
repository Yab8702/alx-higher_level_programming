#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if chr(alphabet) == 'e' or chr(alphabet) == 'q':
        continue
    print("{:s}".format(chr(alphabet)), end="")
