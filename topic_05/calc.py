import functions
import operations

while True:
    operation = operations.input_operation()
    if operation is None:
        break

    a = operations.input_number("Enter first number (or 'exit'): ")
    if a is None:
        break

    b = operations.input_number("Enter second number (or 'exit'): ")
    if b is None:
        break

    if operation == "+":
        print("Result =", functions.add(a, b))
    elif operation == "-":
        print("Result =", functions.subtract(a, b))
    elif operation == "*":
        print("Result =", functions.multiply(a, b))
    elif operation == "/":
        if b == 0:
            print("Error: division by zero")
        else:
            print("Result =", functions.divide(a, b))

print("Program finished")