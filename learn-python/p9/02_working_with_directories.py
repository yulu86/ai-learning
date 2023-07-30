from pathlib import Path

# path = Path("not_exists")
# print(path)
# print(path.absolute())
# print(path.exists())

# path.mkdir()
# path = path.rename("dajiji")


path = Path(r"learn-python")
print(path.iterdir())

for item in path.iterdir():
    print(item)

# 非递归
paths = [item for item in path.iterdir() if item.is_dir()]
print(paths)

# 非递归搜索
pyFiles = [p for p in path.glob("*.py")]


# 递归搜索
pyFiles = [p for p in path.rglob("*.py")]
print(pyFiles)
