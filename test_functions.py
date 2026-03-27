import pytest
from functions import calculate_sum


def test_calculate_sum_str():
    with pytest.raises(TypeError):
        calculate_sum("HELLO, MR. RAK!")

def test_calculate_sum_one_element():
    with pytest.raises(TypeError):
        calculate_sum(1)

def test_calculate_sum_two_element():
    with pytest.raises(TypeError):
        calculate_sum(3)

def test_calculate_sum_one_hundred_element():
    with pytest.raises(TypeError):
        calculate_sum(5050)

def test_calculate_sum_zero():
    with pytest.raises(TypeError):
        calculate_sum(0)

def test_calculate_sum_void():
    with pytest.raises(TypeError):
        calculate_sum(" ")

def test_calculate_sum_negative():
    with pytest.raises(TypeError):
        calculate_sum(-5)

def test_calculate_sum_positive():
    with pytest.raises(TypeError):
        calculate_sum(10)