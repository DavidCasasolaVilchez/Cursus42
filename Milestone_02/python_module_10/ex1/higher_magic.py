from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (
        spell1(target, power) + ", " + spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (
        spell("Spell fizzled", power)
        if condition(target, power)
        else spell(target, power)
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [
        spell(target, power) for spell in spells
    ]


def main() -> None:
    def fireball(target, power):
        return f"Fireball hits {target}"

    def heal(target, power):
        return f"Heals {target}"

    def power_spell(target, power):
        return power

    print("\nTesting spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined_spell('Dragon', 10)}")

    print("\nTesting power amplifier...")
    amplified_spell = power_amplifier(power_spell, 3)
    print(f"Original: 10, Amplified: {amplified_spell('Dragon', 10)}")


if __name__ == "__main__":
    main()
