#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        characters_written = file.write(text)

    return characters_written
