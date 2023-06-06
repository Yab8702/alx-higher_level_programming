#!/usr/bin/python3
for i, rev_alph in zip(range(1, 27), range(ord('z'), ord('a') - 1, -1)):
    if i % 2 == 0:
        rev_alph -= 32
    print("{}".format(chr(rev_alph)), end="")
