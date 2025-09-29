# tests/test_operations.py

import pytest
from app.operations import (
    AddOperation, SubtractOperation, MultiplyOperation,
    DivideOperation, PowerOperation, RootOperation
)

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 8),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert AddOperation().execute(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (3, 5, -2),
])
def test_subtract(a, b, expected):
    assert SubtractOperation().execute(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 15),
    (0, 5, 0),
])
def test_multiply(a, b, expected):
    assert MultiplyOperation().execute(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2),
    (10, 2, 5),
])
def test_divide(a, b, expected):
    assert DivideOperation().execute(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        DivideOperation().execute(5, 0)

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 8),
    (4, 0.5, 2),
])
def test_power(a, b, expected):
    assert PowerOperation().execute(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (9, 2, 3),
    (27, 3, 3),
])
def test_root(a, b, expected):
    assert RootOperation().execute(a, b) == expected

def test_root_with_zero():
    with pytest.raises(ValueError, match="Cannot take root with zero"):
        RootOperation().execute(9, 0)
