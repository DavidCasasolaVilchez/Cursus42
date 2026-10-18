class Plant:
    def __init__(self, nm: str, h: float, a: int, growth_rate: float = 0.8):
        self.name = nm
        self.height = h
        self._age = a
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self._age} days old")

    def grow(self) -> float:
        self.height += self.growth_rate

    def age(self):
        self._age += 1


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    initial_height = p1.height
    print("=== Garden Plant Growth ===")
    p1.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        p1.grow()
        p1.age()
        p1.show()
    print(f"Growth this week: {round(p1.height - initial_height, 1)}cm")
