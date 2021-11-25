import pytest
from main import additions, subtraction, multiply, division

def test_positive_additions():
    assert additions(4,2) == 6

def test_positive_subtraction():
    assert subtraction(4,2) == 2

def test_positive_multiply():
    assert multiply(4,2) == 8

def test_positive_division():
    assert division(4,0) == "На ноль делить нельзя"


def test_negative_additions():
    assert additions(4,2) != 2

def test_negative_subtraction():
    assert subtraction(4,2) != 12

def test_negative_multiply():
    assert multiply(4,2) != 19

def test_negative_division():
    assert division(4,0) != 2