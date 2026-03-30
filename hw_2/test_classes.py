import pytest

from classes import Temperature

@pytest.fixture
def zero_temp():
    return Temperature(0)

@pytest.fixture
def boiling_water_temp():
    return Temperature(100)

@pytest.fixture
def freezing_alcohol_temp():
    return Temperature(-114.15)


def test_get_value_zero(zero_temp):
    assert zero_temp.get_value() == 0

def test_get_value_positive(boiling_water_temp):
    assert boiling_water_temp.get_value() == 100

def test_get_value_negative(freezing_alcohol_temp):
    assert freezing_alcohol_temp.get_value() == -114.15

def test_to_fahrenheit_zero(zero_temp):
    assert zero_temp.to_fahrenheit() == 32

def test_to_calvin_zero(zero_temp):
    assert zero_temp.to_calvin() == 273

def test_to_fahrenheit_boiling_water_temp(boiling_water_temp):
    assert boiling_water_temp.to_fahrenheit() == 212

def test_to_calvin_boiling_water_temp(boiling_water_temp):
    assert boiling_water_temp.to_calvin() == 373

def test_to_fahrenheit_freezing_alcohol(freezing_alcohol_temp):
    assert freezing_alcohol_temp.to_fahrenheit() == -173.47000000000003

def test_to_calvin_freezing_alcohol(freezing_alcohol_temp):
    assert freezing_alcohol_temp.to_calvin() == 158.85

def test_is_positive_boiling_water_temp(boiling_water_temp):
    assert boiling_water_temp.is_positive() == True

def test_is_positive_freezing_alcohol_temp(freezing_alcohol_temp):
    assert freezing_alcohol_temp.is_positive() == False

def test_is_positive_zero_temp(zero_temp):
    assert zero_temp.is_positive() == False

def test_compare_first_greater(boiling_water_temp, freezing_alcohol_temp):
    assert Temperature.compare(boiling_water_temp, freezing_alcohol_temp) == -1

def test_compare_first_below(freezing_alcohol_temp, zero_temp):
    assert Temperature.compare(freezing_alcohol_temp, zero_temp) == 1

def test_compare_equal(zero_temp):
    same_temp = zero_temp
    assert Temperature.compare(zero_temp, same_temp) == 0

