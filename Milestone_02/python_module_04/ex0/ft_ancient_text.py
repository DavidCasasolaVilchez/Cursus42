import sys
import typing


def cat() -> None:
    args = sys.argv
    if len(args) > 1:
        try:
            print(f"Accessing file '{args[1]}'")
            file: typing.IO = open(args[1], "r")
            text = file.read()
            print(f"---\n\n{text}\n\n---")
            file.close()
            print(f"File '{args[1]}' closed")
        except (FileNotFoundError, PermissionError, IsADirectoryError,
                OSError) as e:
            print(f"Error opening file '{args[1]}': {e}")
    else:
        print(f"Usage: {args[0]} <file>")


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    cat()


if __name__ == "__main__":
    main()
