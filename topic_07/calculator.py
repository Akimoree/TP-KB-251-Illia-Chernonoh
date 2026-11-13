from operations import Add, Subtract, Multiply, Divide


class Calculator:
    def __init__(self):
        self._operations = {}
        for operation in [Add(), Subtract(), Multiply(), Divide()]:
            self.add_operation(operation)

    def add_operation(self, operation):
        self._operations[operation.symbol] = operation

    def get_symbols(self):
        return list(self._operations.keys())

    def calculate(self, symbol, a, b):
        if symbol not in self._operations:
            raise ValueError(f"Unknown operation: {symbol}")
        return self._operations[symbol].calculate(a, b)