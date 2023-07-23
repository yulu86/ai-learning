class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 静态工厂方法
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()

another = Point(3, 4)
another.draw()

zeroPoint = Point.zero()
zeroPoint.draw()
