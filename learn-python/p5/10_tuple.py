def printTuple(thisTuple):
    thisType = type(thisTuple)
    print(thisType, thisTuple)

point = 1, 2
printTuple(point) # <class 'tuple'>

point = (1, 2) + (3, 4)
printTuple(point)

point = (1, 2) * 3
printTuple(point)

# list转换为tuple
point = tuple([1, 2])
printTuple(point)

# String是Iterable类型，可以转换成tuple
point = tuple("Hello World")
printTuple(point)

print(point[0:2])

x, y, *z = point
print(x, y, z)

if "e" in point:
    print("Exists")

# tuple不支持修改
# point[0] = "abc"