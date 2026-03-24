

def calculate_sum(n: int | float) -> int | float:

    if not isinstance(n, int) or not isinstance(n, float):

        raise TypeError("n must be int or float")

    if n < 0:

        raise ValueError("n must be >= 0")


    summa = 0

    for i in range (1, n + 1):

        summa += i

    return summa



