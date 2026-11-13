from calculator import Calculator
from console import ConsoleInput


def main():
    calculator = Calculator()
    console = ConsoleInput()

    while True:
        operation = console.input_operation(calculator.get_symbols())
        if operation is None:
            break

        a = console.input_number("Enter first number (or 'exit'): ")
        if a is None:
            break

        b = console.input_number("Enter second number (or 'exit'): ")
        if b is None:
            break

        try:
            result = calculator.calculate(operation, a, b)
        except ZeroDivisionError:
            print("Error: division by zero")
            continue
        print("Result =", result)

    print("Program finished")


if __name__ == "__main__":
    main()