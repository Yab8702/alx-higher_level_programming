#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        new_tuple_a = (tuple_a + (0,) * (2 - len(tuple_a)))
    else:
        new_tuple_a = tuple_a[:2]
    if len(tuple_b) < 2:
        new_tuple_b = (tuple_b + (0,) * (2 - len(tuple_b)))
    else:
        new_tuple_b = tuple_b[:2]
    return tuple(a + b for a, b in zip(new_tuple_a, new_tuple_b))
