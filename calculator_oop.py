class Calculator(object):

    @classmethod
    def add(cls, num1: int, num2: int) -> int:
        return num1 + num2

    @classmethod
    def sub(cls, num1: int, num2: int) -> int:
        return num1 - num2

    @classmethod
    def div(cls, num1: int, num2: int) -> int:
        return num1 // num2

    @classmethod
    def mul(cls, num1: int, num2: int) -> int:
        return num1 * num2
