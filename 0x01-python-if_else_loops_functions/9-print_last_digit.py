#!/usr/bin/python3

def print_last_digit(num):
    if num < 0:
        num *= -1
    result = num % 10
    print('{}'.format(result), end="")
    return result
