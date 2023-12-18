#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    i = 0
    try:
        while printed_integers < x:
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end="")
                printed_integers += 1
            i += 1
    except IndexError:
        pass
    finally:
        print()
    return printed_integers
