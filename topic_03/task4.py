def find_position(sorted_list, value):
    for i in range(len(sorted_list)):
        if value <= sorted_list[i]:
            return i
    return len(sorted_list)


numbers = [1, 3, 5, 7, 9, 11]
print("Sorted list:", numbers)

try:
    value = int(input("Enter new value: "))
except ValueError:
    print("Error: enter an integer")
else:
    position = find_position(numbers, value)
    print("Position:", position)
    numbers.insert(position, value)
    print("New list:", numbers)
