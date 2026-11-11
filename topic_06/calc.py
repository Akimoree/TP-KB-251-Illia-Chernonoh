import logging

import functions
import operations

logging.basicConfig(filename="calc.log", level=logging.INFO, encoding="utf-8",
                    format="%(asctime)s [%(levelname)s] %(message)s")
logging.info("Program started")

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

    logging.info("Operation: " + str(a) + " " + operation + " " + str(b))
    if operation == "+":
        result = functions.add(a, b)
    elif operation == "-":
        result = functions.subtract(a, b)
    elif operation == "*":
        result = functions.multiply(a, b)
    elif operation == "/":
        if b == 0:
            print("Error: division by zero")
            logging.error("Division by zero: " + str(a) + " / " + str(b))
            continue
        result = functions.divide(a, b)

    print("Result =", result)
    logging.info("Result: " + str(result))

logging.info("Program finished")
print("Program finished")