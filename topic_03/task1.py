def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:
    operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")

    if operation.lower() == "exit":
        print("Program finished")
        break

    if operation not in ["+", "-", "*", "/"]:
        print("Unknown operation")
        continue

    first = input("Enter first number (or 'exit'): ")
    if first.lower() == "exit":
        print("Program finished")
        break

    second = input("Enter second number (or 'exit'): ")
    if second.lower() == "exit":
        print("Program finished")
        break

    try:
        a = float(first)
        b = float(second)
    except ValueError:
        print("Error: enter a number")
        continue

    if operation == "+":
        print("Result =", add(a, b))
    elif operation == "-":
        print("Result =", subtract(a, b))
    elif operation == "*":
        print("Result =", multiply(a, b))
    elif operation == "/":
        if b == 0:
            print("Error: division by zero")
        else:
            print("Result =", divide(a, b))