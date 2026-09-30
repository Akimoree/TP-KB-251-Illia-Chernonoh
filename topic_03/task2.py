numbers = [5, 2, 9]
print("Start list:", numbers)

numbers.extend([7, 1, 3])
print("extend:", numbers)

numbers.append(8)
print("append:", numbers)

numbers.insert(2, 100)
print("insert:", numbers)

numbers.remove(100)
print("remove:", numbers)

numbers.clear()
print("clear:", numbers)

numbers = [4, 10, 1, 7, 3]
print("New list:", numbers)

numbers.sort()
print("sort:", numbers)

numbers.reverse()
print("reverse:", numbers)

new_numbers = numbers.copy()
print("copy:", new_numbers)