def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire import light_validator as lv
    s: str = (
        f"Spell recorded: {spell_name} {lv.validate_ingredients(ingredients)}"
    )
    return s
