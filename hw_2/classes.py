
class Temperature:
    """
    Возможные тесты для класса Temperature:
    1) Значение температуры при 0 градусов;
    2) Значение температуры при кипении воды;
    3) Значение температуры при замерзании спирта (этанола);
    4) Значение температуры при 0 градусов для Фаренгейта;
    5) Значение температуры при 0 градусов для Кельвина;
    6) Значение температуры при кипении воды для Фаренгейта;
    7) Значение температуры при кипении воды для Кельвина;
    8) Значение температуры при замерзании спирта (этанола) для Фаренгейта;
    9) Значение температуры при замерзании спирта (этанола) для Кельвина;
    10) Положительная температура;
    11) Отрицательная температура;
    12) Нулевая температура;
    13) Сравнение температур, первая выше;
    14) Сравнение температур, первая ниже;
    15) Сравнение температур, обе равны.
    """

    def __init__(self, celsius: int):

        self.__celsius = celsius


    def get_value(self) -> int:

        return self.__celsius


    def to_fahrenheit(self) -> float:

        fahrenheit = (self.__celsius * 9) / 5 + 32

        return fahrenheit


    def to_calvin(self) -> int:

        calvin = self.__celsius + 273

        return calvin


    def is_positive(self) -> bool:

        if self.__celsius > 0:

            return True

        return False


    @staticmethod
    def compare(t1: int, t2: int) -> int:

        if t1.get_value() > t2.get_value():

            return -1

        elif t1.get_value() < t2.get_value():

            return 1

        else:

            return 0

