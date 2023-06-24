point = {"x": 1, "y": 2}
point = dict(x = 1, y = 2)

print(type(point))
print(point)

print(point["x"])
print(point["y"])

point["x"] = 10
print(point["x"])

# 报错
# print(point["z"])

if "z" in point:
    print(point["z"])

print(point.get("z", 0))
print(point)

del point["x"]
print(point)


for key in point:
    print(key, point[key])

for item in point.items():
    print(type(item), item)

for key, value in point.items():
    print(key, value)