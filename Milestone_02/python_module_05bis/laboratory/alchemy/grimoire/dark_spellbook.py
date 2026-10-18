from .dark_validator import validate_ingredients as lv


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    s: str = (
        f"Spell recorded: {spell_name} {lv(ingredients)}"
    )
    return s
