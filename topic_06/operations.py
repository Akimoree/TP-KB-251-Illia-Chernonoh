import logging

logger = logging.getLogger(__name__)


def input_operation():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        if operation.lower() == "exit":
            logger.info("User entered: exit")
            return None
        if operation in ["+", "-", "*", "/"]:
            logger.info(f"Entered operation: {operation}")
            return operation
        print("Unknown operation")
        logger.warning(f"Unknown operation: {operation}")


def input_number(text):
    while True:
        value = input(text)
        if value.lower() == "exit":
            logger.info("User entered: exit")
            return None
        try:
            number = float(value)
        except ValueError:
            print("Error: enter a number")
            logger.warning(f"Wrong number: {value}")
            continue
        logger.info(f"Entered number: {number}")
        return number