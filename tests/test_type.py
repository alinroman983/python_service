import pytest
from type_test import add

def test_add():
    assert add(5, 10) == 15
    assert add("Hello, ", "World!") == "Hello, World!" 
   
    