import math

def discriminant(a, b, c):
    d = b * b - 4 * a * c
    return d

def find_roots(a, b, c):
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x, x
    else:
        return None

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("a cannot be 0")
else:
    roots = find_roots(a, b, c)
    if roots is None:
        print("No real roots")
    else:
        print("x1 =", roots[0])
        print("x2 =", roots[1])