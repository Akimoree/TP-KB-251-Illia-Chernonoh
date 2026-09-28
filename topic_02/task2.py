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
else:
    print("Unknown operation")