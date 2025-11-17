# https://github.com/angelicatang07/lab11-AT-IE.git
#Partner 1: Angelica Tang
#Partner 2: Isabel Espinoza

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("Value can't be negative")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("The base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("The argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b

