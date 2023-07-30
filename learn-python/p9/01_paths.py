from pathlib import Path

# Windows
path = Path(r"C:\Program Files")

# mac or linux
# path = Path(r"/usr/local/bin")


print(path.exists())
print(path.is_file())
print(path.is_dir())
print(f"name={path.name}")
print(f"stem={path.stem}")
print(f"suffix={path.suffix}")
print(f"parent={path.parent}")

path = path.with_name("file.txt")
print(path.absolute())
