from sys import getsizeof

# generator
values = (x * 2 for x in range(50))
print(type(values))  # <class 'generator'>

for x in values:
    print(type(x), x)

# getsizeof获取内存占用大小
print("gen:", getsizeof(values))

# list
values = [x * 2 for x in range(50)]
print(type(values))
print("gen:", getsizeof(values))
