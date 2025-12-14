# pytest_basic.py
# Basic pytest example

def multiply(a, b):
    return a * b

def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_zero():
    assert multiply(5, 0) == 0
