import logging


def input_operation():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        logging.info("Entered operation: " + operation)
        if operation.lower() == "exit":
            return None
        if operation in ["+", "-", "*", "/"]:
            return operation
        print("Unknown operation")
        logging.warning("Unknown operation: " + operation)


def input_number(text):
    while True:
        value = input(text)
        logging.info("Entered value: " + value)
        if value.lower() == "exit":
            return None
        try:
            return float(value)
        except ValueError:
            print("Error: enter a number")
            logging.warning("Wrong number: " + value)