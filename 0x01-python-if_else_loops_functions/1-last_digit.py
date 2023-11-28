#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_int = abs(number) % 10
if last_int < 0:
    number = -number
if last_int > 5:
    print(f"Last digit of {number} is {last_int:d} and is greater than 5")
elif last_int == 0:
    print(f"Last digit of {number} is {last_int:d} and is 0")
else:
    print(f"Last digit of {number} is {last_int:d} and is less than 6 and not 0")