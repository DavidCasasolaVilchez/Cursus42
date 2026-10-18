from typing import Callable


def mage_counter() -> Callable:
    count: int = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


def spell_accumulator(initial_power: int) -> Callable:
    power: int = initial_power

    def increment(npower: int) -> int:
        nonlocal power
        power += npower
        return power
    return increment


def enchantment_factory(enchantment_type: str) -> Callable:
    enchantment: str = enchantment_type

    def enchant(item_name: str) -> str:
        return f"{enchantment} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[int, str] = dict()

    def store(key: int, value: str) -> None:
        memory[key] = value

    def recall(key: int) -> str:
        return memory.get(key, "Memory not found")
    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    print("Testing mage counter...")
    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator: Callable = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flaming: Callable = enchantment_factory("Flaming")
    frozen: Callable = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault: dict[str, Callable] = memory_vault()
    vault["store"]("secret", "42")
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
