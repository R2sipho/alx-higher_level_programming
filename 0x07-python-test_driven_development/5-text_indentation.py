#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""

def text_indentation(text):
    """
    Print text with two newlines added after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    
    for delimiter in ".:?":
        lines = [line.strip() for line in text.split(delimiter)]
        text = (delimiter + "\n\n").join(lines)

    print("{}".format(text), end="")
