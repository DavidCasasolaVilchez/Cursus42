import abc as a


class Creature(a.ABC):
    def __init__(self, name: str, type: str) -> None:
        self._name = name
        self._type = type

    def to_print(self) -> None:
        print(f"{self._name} is a {self._type} type Creature")

    @a.abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"
