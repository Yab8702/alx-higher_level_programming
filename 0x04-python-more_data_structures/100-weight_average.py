#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_score = sum_weight = 0
    for i, lst in zip(range(len(my_list)), my_list):
        (score, weight) = my_list[i]
        sum_score += score * weight
        sum_weight += weight
    return sum_score / sum_weight
