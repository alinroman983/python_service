"""This file is a simple test for the add function"""

from type_test import add


def test_add():
    """Some random tests"""
    assert add(5, 10) == 15
    assert add("Hello, ", "World!") == "Hello, World!"
