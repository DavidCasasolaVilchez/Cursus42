class Plant:
    def __init__(self, nm: str, h: float, a: int, growth_rate: float = 0.8):
        self.name = nm
        self.height = h
        self._age = a
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self._age} days old")

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self._age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25.0, 30)
    p2 = Plant("Oak", 200.0, 365)
    p3 = Plant("Cactus", 5.0, 90)
    p4 = Plant("Sunflower", 80.0, 45)
    p5 = Plant("Fern", 15.0, 120)
    plants = {p1, p2, p3, p4, p5}
    for p in plants:
        print("Created:", end=" ")
        p.show()
