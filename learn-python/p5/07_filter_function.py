items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filteredItems = list(filter(lambda item: item[1] >= 10, items))
print(filteredItems)