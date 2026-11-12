import logging
import os

import functions
import operations

log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calc.log")
logging.basicConfig(filename=log_file, level=logging.INFO, encoding="utf-8",
                    format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

logger.info("Program started")

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

    logger.info(f"Operation: {a} {operation} {b}")
    if operation == "/" and b == 0:
        print("Error: division by zero")
        logger.error(f"Division by zero: {a} / {b}")
        continue

    if operation == "+":
        result = functions.add(a, b)
    elif operation == "-":
        result = functions.subtract(a, b)
    elif operation == "*":
        result = functions.multiply(a, b)
    else:
        result = functions.divide(a, b)

    print("Result =", result)
    logger.info(f"Result: {result}")

logger.info("Program finished")
print("Program finished")