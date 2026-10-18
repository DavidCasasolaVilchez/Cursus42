from alchemy import potions as p


def main():
    print(
        "=== Distillation 0 ==="
        "\nDirect access to alchemy/potions.py"
        f"\nTesting strength_potion: {p.strength_potion()}"
        f"\nTesting healing_potion: {p.healing_potion()}"
    )


if __name__ == "__main__":
    main()
