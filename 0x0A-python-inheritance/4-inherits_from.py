#!/usr/bin/python3
"""Inherits from method"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of
    a class that inherited directly/indirectly from specified class;
    Otherwise False"""
    return isinstance(obj, a_class) and type(obj) != a_class
