from ex3.creature import Flameling, Pyrodon, Creature
from ex3.transform_capability import Shiftling, Morphagon
import abc as a


class CreatureFactory(a.ABC):
    @a.abstractmethod
    def create_base(self) -> Creature:
        pass

    @a.abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
