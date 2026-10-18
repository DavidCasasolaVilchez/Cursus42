import random


def gen_player_achievements(achvs: set[str]) -> set:
    s = set()
    for i in range(1, len(achvs)):
        s.add(random.choice(list(achvs)))
    return s


def main():
    achvs = {
            "Boss Slayer",
            "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
            "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
            "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind"}
    alice = gen_player_achievements(achvs)
    bob = gen_player_achievements(achvs)
    charlie = gen_player_achievements(achvs)
    dylan = gen_player_achievements(achvs)
    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"\nAll distinct achievements: {charlie.union(alice, bob, dylan)}")
    print(f"\nCommon achievements: {charlie.intersection(alice, bob, dylan)}")
    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print(f"\nAlice is missing: {achvs.difference(alice)}")
    print(f"Bob is missing: {achvs.difference(bob)}")
    print(f"Charlie is missing: {achvs.difference(charlie)}")
    print(f"Dylan is missing: {achvs.difference(dylan)}")


if __name__ == "__main__":
    main()
