class Animal:
    def __init__(self):
        print("Animal init")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        # super().__init__()
        print("Mammel init")
        self.age = 10
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
