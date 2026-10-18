class Plant:
    class Stadistics:
        def __init__(self):
            self.gc = 0
            self.ac = 0
            self.sc = 0

    def __init__(self, nm: str, h: float, a: int, gr: float = 0.8,
                 s: Stadistics = Stadistics()):
        self.name = nm
        self._height = h
        self._age = a
        self.growth_rate = gr
        self.stats = s

    def display_stats(self):
        print(f"[stadistics for {self.name}]")
        data = f", {self.stats.ac} age, {self.stats.sc} show"
        print(f"Stats: {self.stats.gc} grow{data}")

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
        self.stats.sc += 1
        data = f"{round(self._height, 1)}cm, {self._age} days old"
        print(f"{self.name.capitalize()}: {data}")

    def grow(self, times: float):
        self.stats.gc += 1
        self._height += (self.growth_rate * times)

    def age(self, days: int):
        self.stats.ac += 1
        self._age += days

    @staticmethod
    def ft_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(Plant):
        return Plant("Unknown plant", 0.0, 0, 0.0, Plant.Stadistics())


class Flower(Plant):
    def __init__(self, nm: str, h: float, a: int, c: str,
                 gr: float = 0.8, bl: bool = False):
        super().__init__(nm, h, a, gr, s=Plant.Stadistics())
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
    class Tree_Stadistics(Plant.Stadistics):
        def __init__(self):
            super().__init__()
            self.shadec = 0

    def __init__(self, nm: str, h: float, a: int, td: float, gr: float = 0.8):
        super().__init__(nm, h, a, gr, s=Tree.Tree_Stadistics())
        self.trunk_diameter = td

    def display_stats(self):
        super().display_stats()
        print(f"{self.stats.shadec} shade")

    def produce_shade(self):
        self.stats.shadec += 1
        data = f"{self._height}cm long and {self.trunk_diameter}cm wide."
        print(f"Tree {self.name} now produces a shade of {data}")

    def show(self):
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self,  nm: str, h: float, a: int, hs: str,
                 nv: float, gr: float = 0.8):
        super().__init__(nm, h, a, gr, s=Plant.Stadistics())
        self.harvest_season = hs
        self.nutritional_value = nv

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self, days: int):
        super().grow(days)
        self.nutritional_value += days


class Seed(Flower):
    def __init__(self, nm: str, h: float, a: int, c: str,
                 s: int = 0, sa: int = 42, gr=0.8, bl=False):
        super().__init__(nm, h, a, c, gr, bl)
        self.seeds = s
        self.seeds_added = sa

    def bloom(self):
        super().bloom()
        self.seeds += self.seeds_added

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")


def display_stadistics(plant: Plant):
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.ft_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.ft_older_than_year(400)}")
    print("\n=== Flower")
    fl = Flower("Rose", 15.0, 10, "red", gr=8)
    fl.show()
    display_stadistics(fl)
    print(f"[asking the {fl.name} to grow and bloom]")
    fl.grow(1)
    fl.bloom()
    fl.show()
    display_stadistics(fl)
    print("\n=== Tree")
    tr = Tree("oak", 200.0, 365, 5.0)
    tr.show()
    display_stadistics(tr)
    tr.produce_shade()
    display_stadistics(tr)
    print("\n=== Seed")
    sd = Seed("Sunflower", 80.0, 45, "Yellow", gr=1.5)
    sd.show()
    print("[make sunflower grow, age and bloom]")
    sd.grow(20)
    sd.age(20)
    sd.bloom()
    sd.show()
    display_stadistics(sd)
    print("\n=== Anonymous")
    un = Plant.create_anonymous()
    un.show()
    display_stadistics(un)
