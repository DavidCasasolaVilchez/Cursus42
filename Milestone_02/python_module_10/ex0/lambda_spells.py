from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts,
        key=lambda artifact: int(artifact["power"]),
        reverse=True,
    )


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda mage: int(mage["power"]) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return [f"* {spell} *" for spell in spells]


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, float]:
    powers = [int(mage["power"]) for mage in mages]
    return {"max_power": float(max(powers)),
            "min_power": float(min(powers)),
            "avg_power": sum(powers) / len(powers)}


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )
    print("\nTesting spell transformer...")
    spells = spell_transformer(["fireball", "heal", "shield"])
    print(" ".join(spells))


if __name__ == "__main__":
    main()
