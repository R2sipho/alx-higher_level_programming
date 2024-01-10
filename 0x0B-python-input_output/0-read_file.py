#!/usr/bin/python3
"""
Module 0-read_file.
Reads from a file and prints its contents to stdout.
"""
def read_file(filename=""):
    """
    Reads from filename and prints
    its contents to stdout.
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
