

def main():
    print(
        "=== Kaboom 1 ===\n"
        "Access to alchemy/grimoire/dark_spellbook.py directly\n"
        "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION"
    )
    from alchemy.grimoire import dark_spellbook as d
    d.dark_spell_allowed_ingredients()


if __name__ == "__main__":
    main()
