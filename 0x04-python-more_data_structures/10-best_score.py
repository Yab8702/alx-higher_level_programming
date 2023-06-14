#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        value_list = list(a_dictionary.values())
        value_list.sort(reverse=True)
        for key in a_dictionary.keys():
            if a_dictionary[key] == value_list[0]:
                return key
