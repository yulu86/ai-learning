items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filteredItems = list(filter(lambda item: item[1] >= 10, items))
print(filteredItems)

prices = list(map(lambda item:item[1], items))
print(prices)

prices = [item[1] for item in items]
print(prices)

prices.sort(reverse=True)
print(prices)