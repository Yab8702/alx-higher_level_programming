#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_sen = tuple(sentence)
    if len(tuple_sen) == 0:
        return 0, None
    return len(tuple_sen), tuple_sen[0]
