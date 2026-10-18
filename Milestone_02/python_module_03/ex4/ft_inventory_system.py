import sys


def set_inventory() -> None:
    args = sys.argv
    args.pop(0)
    if len(args) != 0:
        inventory: dict[str, int] = dict()
        for s in args:
            try:
                kv = s.split(":")
                if kv[0] != s:
                    if inventory.keys().isdisjoint(kv):
                        inventory.update({kv[0]: int(kv[1])})
                    else:
                        print(f"Redundant item '{kv[0]}'- discarding")
                else:
                    print(f"Error - invalid parameter '{s}'")
            except ValueError as error:
                print(f"Quantity error for '{kv[1]}': {error}")
        display(inventory)
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
    else:
        print("Error: Arguments invalids!")


def biggest_item(inventory: dict) -> None:
    big = 0
    bigs = " "
    lit = 100000000
    lits = " "
    for k, v in inventory.items():
        if v >= big:
            big = v
            bigs = k
        if v <= lit:
            lit = v
            lits = k
    print(f"Item most abundant: {bigs} with quantity {big}")
    print(f"Item least abundant: {lits} with quantity {lit}")


def display(inventory: dict) -> None:
    print("=== Inventory System Analysis ===")
    total = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.keys()}")
    print(
        f"Total quantity of the {len(inventory.keys())} "
        f"items: {total}")
    for k, v in inventory.items():
        print(f"Item {k} represents {round(((v/total) * 100), 1)}%")
    biggest_item(inventory)


def main() -> None:
    set_inventory()


if __name__ == "__main__":
    main()
