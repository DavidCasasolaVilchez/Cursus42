from .dark_spellbook import dark_spell_allowed_ingredients as ls


def validate_ingredients(ingredients: str) -> str:
    valids: list[str] = ls()
    for w in valids:
        if ingredients.lower().find(w.lower()) == -1:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
