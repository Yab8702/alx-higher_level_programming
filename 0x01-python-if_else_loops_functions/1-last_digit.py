#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = (number % 10, (-((number * -1) % 10)))[number < 0]
if rem > 5:
    print(f"Last digit of {number} is {rem} and is greater than 5")
elif rem < 6 and rem != 0:
    print(f"Last digit of {number} is {rem} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {rem} and is 0")
