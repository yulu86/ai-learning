values = []
for x in range(5):
    values.append(x * 2)

# list
values = [x * 2 for x in range(5)]
print(type(values), values)

# set
values = {x * 2 for x in range(5)}
print(type(values), values)

# dictionary
values = {x: x * 2 for x in range(5)}
print(type(values), values)