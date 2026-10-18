import sys


def check_args(args: list[str]) -> list[int]:
    ls: list[int] = []
    for i in args:
        try:
            if i != args[0]:
                ls.append(int(i))
        except ValueError:
            print(f"Invalid parameter: '{i}'")
        except TypeError:
            print(f"Invalid parameter: '{i}'")
    return ls


def display(lst: list[int]):
    if len(lst) <= 0:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
    else:
        print(
            f"\nScores processed: {lst}"
            f"\nTotal players: {len(lst)}"
            f"\nTotal score: {sum(lst)}"
            f"\nAverage score: {sum(lst) / len(lst)}"
            f"\nHigh score: {max(lst)}"
            f"\nLow score: {min(lst)}"
            f"\nScore range: {max(lst) - min(lst)}"
        )


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    display(check_args(sys.argv))
