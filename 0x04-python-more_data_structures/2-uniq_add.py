#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_uniq = 0
    new_uniq = set(my_list)
    for uniq in new_uniq:
        sum_uniq += uniq
    return sum_uniq
