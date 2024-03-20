#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if isinstance(roman_string, str):
        roman_dic = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000
                }
        for s_str, i in zip(roman_string, range(len(roman_string))):
            if roman_dic.get(s_str, 0) == 0:
                return 0
            if i != len(roman_string) - 1 and \
                    roman_dic[s_str] < roman_dic[roman_string[i + 1]]:
                number += roman_dic[roman_string[i]] * -1
            else:
                number += roman_dic[s_str]
        return number
    return 0
