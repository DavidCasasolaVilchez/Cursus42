import math


def get_player_pos() -> tuple:
    while True:
        inpt: str = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        values: list[str] = inpt.split(",")

        if len(values) != 3:
            print("Invalid syntax")
            continue

        try:
            return tuple(float(value.strip()) for value in values)
        except ValueError as error:
            parameter = next(
                value.strip()
                for value in values
                if _is_invalid_float(value.strip())
            )
            print(f"Error on parameter '{parameter}': {error}")


def _is_invalid_float(value: str) -> bool:
    try:
        float(value)
        return False
    except ValueError:
        return True


def distance_between(first: tuple, second: tuple) -> float:
    return math.sqrt(
        sum((value - origin) ** 2 for value, origin in zip(second, first)))


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")
    print(f"Distance to center: {distance_between((0, 0, 0), first_pos):.4f}")

    print("\nGet a second set of coordinates")
    second_pos = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{distance_between(first_pos, second_pos):.4f}"
    )
