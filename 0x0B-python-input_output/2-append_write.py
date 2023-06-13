#!/usr/bin/python3
"""Defines a fie appending function."""


def append_write(filename="", text=""):
    """Appends the a string to the end of UTF8 a text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The name of the characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
