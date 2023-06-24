numbers = [1, 1, 2, 2, 3, 4]
# set去重
first = set(numbers)
print(first)

second = {1, 5}
print(type(second)) #  <class 'set'>
second.add(7)
second.remove(5)
print(len(second))

print(first | second)  # first和second求并集
print(first & second)  # first和second求交集
print(first - second)  # 在first中存在，在second中不存在
print(first ^ second)  # 在first或second中存在，但不在两个里面同时存在

# set是无序的，不能用索引访问
# print(first[0])

if 1 in first:
    print("yes")