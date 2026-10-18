import ex3.creature as c
import abc as a


class TransformCapability(a.ABC):
    def __init__(self) -> None:
        self._transform = False

    @a.abstractmethod
    def transform(self) -> None:
        pass

    @a.abstractmethod
    def revert(self) -> None:
        pass

    @a.abstractmethod
    def attack(self) -> str:
        pass


class Shiftling(c.Creature, TransformCapability):
    def __init__(self):
        c.Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transform:
            return f"{self._name} performs a boosted strike."
        return f"{self._name} attacks normally."

    def transform(self) -> None:
        print(f"{self._name} shifts into a sharper form!")
        self._transform = True

    def revert(self) -> None:
        print(f"{self._name} returns to normal.")
        self._transform = False


class Morphagon(c.Creature, TransformCapability):
    def __init__(self):
        c.Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transform:
            return f"{self._name} unleashes a devastating morph strike!."
        return f"{self._name} attacks normally."

    def transform(self) -> None:
        print(f"{self._name} morphs into a dragonic battle form!")
        self._transform = True

    def revert(self) -> None:
        print(f"{self._name} stabilizes its form.")
        self._transform = False
