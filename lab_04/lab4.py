import math

DIGITS = "0123456789"

OPERATORS = {"+": 1, "-": 1, "*": 2, "/": 2, "u-": 3, "^": 4}
RIGHT_ASSOCIATIVE = ["u-", "^"]


def isUnaryPosition(tokens):
    
    return len(tokens) == 0 or tokens[-1] in OPERATORS or tokens[-1] == "("


def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch.isspace():
            i += 1
        elif ch in DIGITS or ch == ".":
            start = i
            while i < len(expression) and (expression[i] in DIGITS or expression[i] == "."):
                i += 1
            number = expression[start:i]
            if number.count(".") > 1 or number == ".":
                raise ValueError("Wrong number: " + number)
            tokens.append(number)
        elif ch in "+-":
            if isUnaryPosition(tokens):
                if ch == "-":
                    tokens.append("u-")
                # unary plus does not change the value, so it is skipped
            else:
                tokens.append(ch)
            i += 1
        elif ch in "*/^()":
            tokens.append(ch)
            i += 1
        else:
            raise ValueError("Unknown symbol: " + ch)
    return tokens


def mustPopBefore(top, current):
    if OPERATORS[top] > OPERATORS[current]:
        return True
    return OPERATORS[top] == OPERATORS[current] and current not in RIGHT_ASSOCIATIVE


def toRpn(tokens):
    output = []
    stack = []
    for token in tokens:
        if token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Brackets are not balanced")
            stack.pop()
        elif token == "u-":
            stack.append(token)
        elif token in OPERATORS:
            while stack and stack[-1] != "(" and mustPopBefore(stack[-1], token):
                output.append(stack.pop())
            stack.append(token)
        else:
            output.append(token)
    while stack:
        top = stack.pop()
        if top == "(":
            raise ValueError("Brackets are not balanced")
        output.append(top)
    return output


def applyOperator(operator, left, right):
    try:
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left * right
        if operator == "/":
            return left / right
        return math.pow(left, right)
    except ZeroDivisionError:
        raise ValueError("Division by zero")
    except OverflowError:
        raise ValueError("Number is too large")
    except ValueError:
        raise ValueError("Power operation is not possible")


def checkNumber(value):
    if math.isinf(value):
        raise ValueError("Number is too large")
    return value


def calculateRpn(rpn):
    stack = []
    for token in rpn:
        if token == "u-":
            if len(stack) < 1:
                raise ValueError("Not enough operands")
            stack.append(-stack.pop())
        elif token in OPERATORS:
            if len(stack) < 2:
                raise ValueError("Not enough operands")
            right = stack.pop()
            left = stack.pop()
            stack.append(checkNumber(applyOperator(token, left, right)))
        else:
            stack.append(checkNumber(float(token)))
    if len(stack) != 1:
        raise ValueError("Wrong expression")
    return stack[0]


def expressionToRpn(expression):
    return toRpn(tokenize(expression))


def calculate(expression):
    return calculateRpn(expressionToRpn(expression))


def formatNumber(value):
    value = round(value, 10)
    if value == int(value) and abs(value) < 1e15:
        return str(int(value))
    return str(value)


def main():
    while True:
        expression = input("Please enter the expression (empty line to exit): ")
        if expression.strip() == "":
            print("Exit()")
            break
        try:
            rpn = expressionToRpn(expression)
            print("RPN: " + " ".join(rpn))
            print("Result: " + formatNumber(calculateRpn(rpn)))
        except ValueError as error:
            print("Error: " + str(error))
    return


if __name__ == "__main__":
    main()