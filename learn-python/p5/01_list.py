def printClass(obj):
    thisType = type(obj)
    print(f"class is {thisType}")


letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters

numbers = list(range(20))
chars = list("Hello World")

printClass(letters)
printClass(zeros)
printClass(combined)
print(combined)
print(numbers)
print(chars)
