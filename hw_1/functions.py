from typing import Any


def calculate_sum(n: float) -> float:
    """
    Возможные тесты для функции calculate_sum:
    1) Строковый (не числовой) тип данных;
    2) Список с одним элементом;
    3) Список с двумя элементами;
    4) Список со ста элементами;
    5) Нулевой список;
    6) Пустой список;
    7) Отрицательное число элементов;
    8) Положительное число элементов.
    """

    if not isinstance(n, float):

        raise TypeError("n must be float")

    if n < 1:

        raise AssertionError("n must be >= 1")

    if not n:

        return 0


    summa = 0

    for i in range (1, n + 1):

        summa += i

    return summa


def count_words(line: str) -> int:
    """
    Возможные тесты для функции count_words:
    1) Обычная строка из нескольких слов;
    2) Пустая строка;
    3) Строка из пробелов;
    4) Пробелы в начале строки и в конце;
    5) Много пробелов между словами;
    6) Одно слово;
    7) Одиночные буквы;
    8) Слова через дефис.
    """

    if not isinstance(line, str):

        raise TypeError("line must be str")

    if not line:

        return 0


    length = len(line.split())

    return length


def is_number(string: str) -> bool:
    """
    Возможные тесты для функции is_number:
    1) Положительное число;
    2) Отрицательное число;
    3) Ноль;
    4) Дробное число;
    5) Нули перед числом;
    6) Строка с буквами и цифрами;
    7) Строка с пробелами;
    8) Пустая строка.
    """

    if not isinstance(string, str):

        raise TypeError("string must be str")

    if not string:

        return False


    try:

        int(string)

        return True

    except ValueError:

        return False


def unique(lst: list[Any]) -> list[Any]:
    """
    Возможные тесты для функции unique:
    1) Есть уникальные элементы;
    2) Все элементы уникальные;
    3) Один элемент в списке;
    4) Пустой список;
    5) Список из строк
    6) Смешанный тип элементов;
    7) Число вместо списка;
    8) Нет элементов.
    """

    if not isinstance(lst, list):

        raise TypeError("lst must be list")

    if not lst:

        return []


    unique_list = []

    for item in lst:

        if item not in unique_list:

            unique_list.append(item)

    return unique_list
