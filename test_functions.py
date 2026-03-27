import pytest
from functions import calculate_sum
from functions import count_words


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


def test_count_words_single_spaces():
    assert count_words("HELLO, MR. RAK!") == 3

def test_count_words_void():
    with pytest.raises(TypeError):
        count_words(None)

def test_count_words_only_spaces():
    assert count_words("     ") == 0

def test_count_words_spaces_front_behind():
    assert count_words("  HELLO, MR. RAK!  ") == 3

def test_count_words_multiple_spaces():
    assert count_words("HELLO,   MR.   RAK!") == 3

def test_single_word():
    assert count_words("HELLO") == 1

def test_count_words_single_letters():
    assert count_words("d s g e") == 4

def test_count_words_hyphenated_words():
    assert count_words("python-cool") == 1