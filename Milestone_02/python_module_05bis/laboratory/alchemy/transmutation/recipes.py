from alchemy import elements as e2
from alchemy import potions as p
import elements as e1


def lead_to_gold() -> str:
    lg: str
    lg = (
        f"Recipe transmuting Lead to Gold: brew {e2.create_air()}"
        f"and ’{p.strength_potion()}’ mixed with ’{e1.create_fire()}’"
    )
    return lg
