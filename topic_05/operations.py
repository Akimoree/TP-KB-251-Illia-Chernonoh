def input_operation():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        if operation.lower() == "exit":
            return None
        if operation in ["+", "-", "*", "/"]:
            return operation
        print("Unknown operation")


def input_number(text):
    while True:
        value = input(text)
        if value.lower() == "exit":
            return None
        try:
            return float(value)
        except ValueError:
            print("Error: enter a number")