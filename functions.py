

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

