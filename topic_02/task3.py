def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

match operation:
    case "+":
        print("Result =", add(a, b))
    case "-":
        print("Result =", subtract(a, b))
    case "*":
        print("Result =", multiply(a, b))
    case "/":
        if b == 0:
            print("Error: division by zero")
        else:
            print("Result =", divide(a, b))
    case _:
        print("Unknown operation")