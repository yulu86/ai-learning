from array import array

# 使用list遇到性能问题时再使用array
numbers = array("i", [1, 2, 3])
print(type(numbers))  # <class 'array.array'>
print(numbers)  # array('i', [1, 2, 3])

print(numbers[0])