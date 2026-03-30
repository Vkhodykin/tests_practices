
class Temperature:

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

