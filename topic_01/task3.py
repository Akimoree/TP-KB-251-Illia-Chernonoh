import math

def discriminant(a, b, c):
    d = b * b - 4 * a * c
    return d

a = input("Enter coefficient a: ")
b = input("Enter coefficient b: ")
c = input("Enter coefficient c: ")

a = float(a)
b = float(b)
c = float(c)

d = discriminant(a, b, c)
print("Discriminant D = " + str(d))

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
elif d == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    print("No real roots")