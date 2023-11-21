import pytest
import src.my_function as my_function
import math

def test_add():
    result = my_function.add(1, 4)
    assert result == 5

def test_divide():
    result = my_function.divide(10, 5)
    assert result == 2

def test_add_strings():
    result = my_function.add("iam salman ", "nizamani")
    assert result == "iam salman nizamani"
    def test_divide_by_zero():
        with pytest.raises(ValueError):
            result = my_function.divide(10, 0)
        