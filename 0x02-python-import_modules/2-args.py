#!/usr/bin/python3
from sys import argv

# Remove the script name from the arguments
arguments = argv[1:]

num_arguments = len(arguments)

print("{} argument{}:".format(num_arguments, 's' if num_arguments != 1 else ''), end='')

if num_arguments == 0:
    print('.')
else:
    print('')
    for i, arg in enumerate(arguments, 1):
        print("{}: {}".format(i, arg))

