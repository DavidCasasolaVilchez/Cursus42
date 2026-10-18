import alchemy.grimoire.light_spellbook as ls


def main() -> None:
    s: str = ls.light_spell_record("Fantasy", "Earth, wind and fire")
    print(
        "=== Kaboom 0 ===\n"
        "Using grimoire module directly\n"
        f"Testing record light spell: {s}"
    )


if __name__ == "__main__":
    main()
