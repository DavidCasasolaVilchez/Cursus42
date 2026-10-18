import random


def main() -> None:
    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"]
    allcap: list[str] = [n.capitalize() for n in players]
    onlycap: list[str] = [n for n in players if n == n.capitalize()]
    score: dict = dict()
    [score.update({n: random.randint(0, 1000)}) for n in allcap]
    average = sum(score.values()) / len(score.keys())
    hs: dict = dict()
    [hs.update({k: v}) for k, v in score.items() if v > average]
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {allcap}")
    print(f"New list of capitalized names only: {onlycap}")
    print(f"\nScore dict: {score}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {hs}")


if __name__ == "__main__":
    main()
