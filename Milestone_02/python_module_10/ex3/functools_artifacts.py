from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    we = partial(base_enchantment, 50, "water")
    fe = partial(base_enchantment, 50, "fire")
    ee = partial(base_enchantment, 50, "earth")
    return {
        "water": we,
        "fire": fe,
        "earth": ee
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher(spell: Any) -> Callable[[Any], str]:
    def result(unknown_spell: Any) -> str:
        return "Unknown spell type"
    return result


@spell_dispatcher.register
def _(damage_spell: int) -> Callable[[Any], str]:
    def result(ds: int) -> str:
        return f"Damage spell: {ds} damage"
    return result


@spell_dispatcher.register
def _(enchantment: str) -> Callable[[Any], str]:
    def result(e: str) -> str:
        return f"Enchantment: {e}"
    return result


@spell_dispatcher.register
def _(multicast: list) -> Callable[[Any], str]:
    def result(mc: list) -> str:
        return f"Multi-cast: {len(mc)} spells"
    return result


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized Fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    print(spell_dispatcher(42)(42))
    print(spell_dispatcher("fireball")("fireball"))
    print(spell_dispatcher(["fireball", "heal", "shield"])([
        "fireball", "heal", "shield"
    ]))
    print(spell_dispatcher(None)(None))


if __name__ == "__main__":
    main()
