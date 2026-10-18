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
        data = f"{round(self._height, 1)}cm, {self._age} days old"
        print(f"{self.name.capitalize()}: {data}")

    def grow(self, times: float):
        self._height += (self.growth_rate * times)

    def age(self, days: int):
        self._age += days


class Flower(Plant):
    def __init__(self, nm: str, h: float, a: int, c: str,
                 gr: float = 0.8, bl: bool = False):
        super().__init__(nm, h, a, gr)
        self.color = c
        self._bloomed = bl

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, nm: str, h: float, a: int, td: float, gr: float = 0.8):
        super().__init__(nm, h, a, gr)
        self.trunk_diameter = td

    def produce_shade(self):
        data = f"{self._height}cm long and {self.trunk_diameter}cm wide."
        print(f"Tree {self.name} now produces a shade of {data}")

    def show(self):
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, nm: str, h: float, a: int, hs: str, nv: float,
                 gr: float = 0.8):
        super().__init__(nm, h, a, gr)
        self.harvest_season = hs
        self.nutritional_value = nv

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self, days: int):
        super().grow(days)
        self.nutritional_value += days


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    fl = Flower("Rose", 15.0, 10, "red")
    fl.show()
    print(f"[asking the {fl.name} to bloom]")
    fl.bloom()
    fl.show()
    print("\n=== Tree")
    tr = Tree("oak", 200.0, 365, 5.0)
    tr.show()
    print(f"[asking the {tr.name} to produce shade]")
    tr.produce_shade()
    print("\n=== Vegetable")
    ve = Vegetable("tomato", 5.0, 10, "Abril", 0, 2.1)
    ve.show()
    print(f"[make {ve.name} grow and age for 20 days]")
    ve.grow(20)
    ve.age(20)
    ve.show()
