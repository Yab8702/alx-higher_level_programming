#!/usr/bin/python3
delm = ", "
for number in range(1, 100):
    if number < 10:
        num_str = '0' + str(number)
        print("{}".format(num_str), end=delm)
    else:
        number1 = number
        while number1 > 0:
            rem = number1 % 10
            number1 /= 10
            if rem <= int(number1):
                eq_ch = 0
                break
            else:
                eq_ch = 1
                number1 = number
                break
        if number == 89:
            delm = "\n"
        if eq_ch == 1:
            print("{}".format(number1), end=delm)
