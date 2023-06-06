#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    for i, s in zip(range(len(str)), str):
        if i == n:
            continue
        str_cpy += s
    return str_cpy
