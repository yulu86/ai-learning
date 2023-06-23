items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item:item[1], items))
print(prices)

prices = [item[1] for item in items]
print(prices)

prices.sort(reverse=True)
print(prices)

filteredItems = list(filter(lambda item: item[1] >= 10, items))
print(filteredItems)

filteredItems = [item for item in items if item[1] >= 10]
print(filteredItems)

list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))