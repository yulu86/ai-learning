numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

# sort方法影响源list
numbers.sort(reverse=True)
print(numbers)

# sorted方法返回新的list，不影响源list
print(sorted(numbers))
print(numbers)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
items.sort()
print(items)


# 比较方法
def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


# 简洁的实现lambda
items.sort(key=lambda item:item[1], reverse=True)
print(items)