numbers = [1, 2, 3]
print(numbers)
print(*numbers)
print(1, 2, 3)

values = list(range(5))

# unpack
values = [*range(5), *"Hello"]
print(values)

first = [1, 2]
second = [3]
# unpack
values = [*first, "a", *second, *"Hello"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)