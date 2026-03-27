import pytest
from functions import calculate_sum
from functions import count_words
from functions import is_number
from functions import unique


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


def test_is_number_positive_integer():
    assert is_number("7532") == True

def test_is_number_negative_integer():
    assert is_number("-385") == True

def test_is_number_zero():
    assert is_number("0") == True

def test_is_number_fractional_number():
    assert is_number("456.54") == False

def test_is_number_leading_zeros():
    assert is_number("00054") == True

def test_is_number_mixed_letters_and_numbers():
    assert is_number("45sdf") == False

def test_is_number_with_spaces():
    assert is_number(" 346 ") == True

def test_is_number_empty_string():
    assert is_number(" ") == False


def test_unique_unique_numbers():
    assert unique([2, 2, 2, 2]) == [2]

def test_unique_all_unique_numbers():
    assert unique([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_unique_single_element():
    assert unique([4]) == [4]
    assert unique(["q"]) == ["q"]
    assert unique([None]) == [None]

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_strings():
    assert unique(["a", "a", "b", "b", "c", "c"]) == ["a", "b", "c"]

def test_unique_mixed_types():
    assert unique([1, "1", "1", 2, False, "2"]) == [1, "1", 2, False, "2"]

def test_unique_integer():
    with pytest.raises(TypeError):
        unique(247)

def test_unique_none():
    with pytest.raises(TypeError):
        unique(None)
