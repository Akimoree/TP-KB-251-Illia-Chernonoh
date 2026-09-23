def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = float(input("Введіть перше число: "))
op = input("Введіть операцію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

match op:
    case "+":
        result = add(num1, num2)
    case "-":
        result = subtract(num1, num2)
    case "*":
        result = multiply(num1, num2)
    case "/":
        result = divide(num1, num2)

print("Результат: " + str(result))