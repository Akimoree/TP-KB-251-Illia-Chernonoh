def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None


def get_user_data():

    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        if operation.lower() == "exit":
            return None

        if operation not in ["+", "-", "*", "/"]:
            print("Unknown operation")
            continue

        first = input("Enter first number (or 'exit'): ")
        if first.lower() == "exit":
            return None

        second = input("Enter second number (or 'exit'): ")
        if second.lower() == "exit":
            return None

        try:
            a = float(first)
            b = float(second)
        except ValueError:
            print("Error: enter a number")
            continue

        return operation, a, b


while True:
    try:
        data = get_user_data()
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted")
        break

    if data is None:
        print("Program finished")
        break

    operation, a, b = data

    if operation == "+":
        print("Result =", add(a, b))
    elif operation == "-":
        print("Result =", subtract(a, b))
    elif operation == "*":
        print("Result =", multiply(a, b))
    elif operation == "/":
        result = divide(a, b)
        if result is not None:
            print("Result =", result)