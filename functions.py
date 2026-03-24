

def calculate_sum(n: int | float) -> int | float:

    if not isinstance(n, int) or not isinstance(n, float):

        raise TypeError("n must be int or float")

    summa = 0

    for i in range (1, n + 1):

        summa += i

    return summa


