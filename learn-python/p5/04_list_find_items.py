letters = ["a", "b", "c"]
print(letters.index("a"))
print(letters.count("d"))

# 注意，元素找不到会报错
# Traceback (most recent call last):
#   File "e:\code\machine-learning\learn-python\p5\04_list_find_items.py", line 3, in <module>
#     print(letters.index("d"))
# ValueError: 'd' is not in list

# print(letters.index("d"))


if "d" in letters:
    print(letters.index("d"))