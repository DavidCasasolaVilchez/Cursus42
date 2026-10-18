import ex3.creature as c
import ex3.transform_capability as t
from ex4.battle_error import BattleError
from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    def __init__(self, entity: c.Creature):
        self.entity = entity

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def act(self) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self, entity: c.Creature):
        super().__init__(entity)

    def is_valid(self) -> bool:
        if isinstance(self.entity, c.Creature):
            return True
        return False

    def act(self) -> None:
        if self.is_valid():
            print(self.entity.attack())
        else:
            raise BattleError(
                f"Invalid Creature '{self.entity._name}'"
                "for this normal strategy"
            )


class AggressiveStrategy(BattleStrategy):
    def __init__(self, entity: c.Creature):
        super().__init__(entity)

    def is_valid(self) -> bool:
        if isinstance(self.entity, t.TransformCapability):
            return True
        return False

    def act(self) -> None:
        if self.is_valid():
            entity = self.entity
            if isinstance(entity, t.TransformCapability):
                entity.transform()
                print(entity.attack())
                entity.revert()
            else:
                raise BattleError(
                    f"Invalid Creature '{entity._name}'"
                    "for this aggressive strategy"
                )
        else:
            raise BattleError(
                f"Invalid Creature '{self.entity._name}'"
                "for this aggressive strategy"
            )
