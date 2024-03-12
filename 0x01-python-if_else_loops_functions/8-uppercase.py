#!/usr/bin/python3
def uppercase(stri):
    to_upper = ""
    for char in stri:
        if ord(char) >= 97 and ord(char) <= 122:
            to_upper += chr(ord(char) - 32)
        else:
            to_upper += char
    print("{}".format(to_upper))
