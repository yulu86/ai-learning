class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    # 静态工厂方法
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(3, 4)
other = Point(1, 2)

print(point)
print(other)

print(point > other)
print(point < other)

print(point + other)
