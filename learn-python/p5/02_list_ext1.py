letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters)
print(letters[0:3])
print(letters[:3])
print(letters[:])
print(letters[::2])

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])

numbers = [1, 2, 3]
# unpack
first, second, third = numbers
print(first)
print(second)
print(third)

# unpack, 其中others是packing
firstNum, secondNum, *others = numbers
print(firstNum)
print(secondNum)
print(others)

def multiply(*numbers):
    print(numbers)

multiply(1, 2, 3, 4, 5)


firstItem, *otherItems, lastItem = numbers
print(firstItem, lastItem)
print(otherItems)