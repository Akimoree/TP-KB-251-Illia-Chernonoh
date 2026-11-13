import math


class ConsoleInput:
    def input_operation(self, symbols):
        text = "Enter operation (" + ", ".join(symbols) + ") or 'exit' to quit: "
        while True:
            operation = input(text)
            if operation.lower() == "exit":
                return None
            if operation in symbols:
                return operation
            print("Unknown operation")

    def input_number(self, text):
        while True:
            value = input(text)
            if value.lower() == "exit":
                return None
            try:
                number = float(value)
            except ValueError:
                number = None
            if number is not None and math.isfinite(number):
                return number
            print("Error: enter a number")