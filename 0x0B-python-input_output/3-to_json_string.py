#!/usr/bin/python3
"""Defines string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON of a string object."""
    return json.dumps(my_obj)
