from . import elements as e
import elements as r


def healing_potion() -> str:
    hp: str = "Healing potion brewed with "
    return f"{hp}{e.create_earth()} and {e.create_air()}"


def strength_potion() -> str:
    hp: str = "Strength potion brewed with "
    return f"{hp}{r.create_fire()} and {r.create_water()}"
