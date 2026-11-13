from abc import ABC, abstractmethod


class Operation(ABC):
    symbol = ""

    @abstractmethod
    def calculate(self, a, b):
        pass


class Add(Operation):
    symbol = "+"

    def calculate(self, a, b):
        return a + b


class Subtract(Operation):
    symbol = "-"

    def calculate(self, a, b):
        return a - b


class Multiply(Operation):
    symbol = "*"

    def calculate(self, a, b):
        return a * b


class Divide(Operation):
    symbol = "/"

    def calculate(self, a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b