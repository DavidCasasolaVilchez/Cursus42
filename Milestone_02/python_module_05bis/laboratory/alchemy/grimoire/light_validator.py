from alchemy.grimoire import light_spellbook as ls


def validate_ingredients(ingredients: str) -> str:
    valids: list[str] = ls.light_spell_allowed_ingredients()
    for w in valids:
        if ingredients.lower().find(w.lower()) == -1:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
