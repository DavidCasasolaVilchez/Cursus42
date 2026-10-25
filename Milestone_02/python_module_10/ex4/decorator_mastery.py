import time
from functools import wraps
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def result(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        res = func(*args, **kwargs)
        time_used = time.perf_counter() - start
        print(f"Spell completed in {time_used:.3f} seconds")
        return res
    return result


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")
            if power is None and len(args) >= 2:
                power = args[2]
            if power is None or int(power) < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return (
                "Spell casting failed after "
                f"{max_attempts} attempts"
            )
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 3 and (all(c.isalpha() or c == " " for c in name)):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def failing_spell() -> str:
        raise RuntimeError("Spell failed")

    print(failing_spell())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G4ndalf"))

    mage = MageGuild()
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
