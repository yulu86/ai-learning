class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        nonsensitiveTag = tag.lower()
        self.__tags[nonsensitiveTag] = self.__tags.get(nonsensitiveTag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower())

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")

print(cloud["python"])
cloud["python"] = 10
print(cloud["python"])

# len
print(len(cloud))

# iterator
for item in cloud:
    print(f"{item}={cloud[item]}")
