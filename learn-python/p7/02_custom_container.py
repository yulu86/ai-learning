class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        nonsensitiveTag = tag.lower()
        self.tags[nonsensitiveTag] = self.tags.get(nonsensitiveTag, 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower())

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

print(cloud["python"])
cloud["python"] = 10
print(cloud["python"])

# len
print(len(cloud))

# iterator
for item in cloud:
    print(f"{item}={cloud[item]}")
