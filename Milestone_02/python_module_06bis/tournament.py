from typing import List, Tuple

from ex3 import factory as f
from ex3.creature import Creature
from ex4.battle_error import BattleError
from ex4 import battle_strategy as b


def battle(
    opponents: List[Tuple[Creature, b.BattleStrategy]]
) -> None:
    entities: List[Tuple[Creature, b.BattleStrategy]] = []
    try:
        for creature, strategy in opponents:
            entity = creature
            entities.append((entity, strategy))
        for index, (entity_a, strategy_a) in enumerate(entities):
            for entity_b, strategy_b in entities[index + 1:]:
                print("* Battle *")
                entity_a.to_print()
                print(" vs.")
                entity_b.to_print()
                print(" now fight!")
                strategy_a.act()
                strategy_b.act()
    except BattleError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    ff = f.FlameFactory()
    tcf = f.TransformCreatureFactory()
    t0: List[Tuple[Creature, b.BattleStrategy]]
    e00 = ff.create_base()
    e01 = tcf.create_base()
    e10 = tcf.create_base()
    e11 = ff.create_base()
    t0 = [
        (e00, b.NormalStrategy(e00)),
        (e01, b.AggressiveStrategy(e01))]
    t1: list[tuple[Creature, b.BattleStrategy]] = [
        (e10, b.AggressiveStrategy(e10)),
        (e11, b.AggressiveStrategy(e11))]
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]\n")
    print(f"*** Tournament ***\n{len(t0)} oponents involved\n")
    battle(t0)
    print("Tournament 1 (error)")
    print("[ Shiftling+Aggressive), (Flameling+Aggressive) ]\n")
    print(f"*** Tournament ***\n{len(t1)} oponents involved\n")
    battle(t1)


if __name__ == "__main__":
    main()
