#!/usr/bin/python3
"""
my_list.
Creates  class inheriting from  list class.
"""
class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Print the list in sorted order (ascending)."""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
