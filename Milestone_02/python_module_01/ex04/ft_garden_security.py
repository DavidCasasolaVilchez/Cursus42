class Plant:
    def __init__(self, nm: str, h: float, a: int, growth_rate: float = 0.8):
        self.name = nm
        self._height = h
        self._age = a
        self.growth_rate = growth_rate

    def set_height(self, height: float):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Age updated: {self._height}cm")

    def set_age(self, age: int):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Height updated: {self._age} days")

    def show(self):
        print(f"{p.name}: {round(p._height, 1)}cm, {p._age} days old")

    def grow(self):
        self._height += self.growth_rate

    def age(self):
        self._age += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    p.show()
    print()
    p.set_height(25.0)
    p.set_age(30)
    print()
    p.set_height(-25.0)
    p.set_age(-30)
    print()
    print("Current state:", end=" ")
    p.show()
