import sys
import typing


def ft_input() -> str:
    print("Enter new file name (or empty): ", end="", flush=True)
    text: str = sys.stdin.readline()
    text = text.removesuffix("\n")
    return text


def cat() -> None:
    args = sys.argv
    if len(args) > 1:
        try:
            print(f"Accessing file '{args[1]}'")
            file: typing.IO = open(args[1], "r")
            text: str = file.read()
            print(f"---\n\n{text}\n\n---")
            file.close()
            print(f"File '{args[1]}' closed")
            print("\nTransform data:")
            new_text: str = text.replace("\n", "#\n")
            if not new_text.endswith("#"):
                new_text += "#"
            print(f"---\n\n{new_text}\n\n---")
        except (FileNotFoundError, PermissionError, IsADirectoryError,
                OSError) as e:
            sys.stderr.write(f"[STDERR] Error opening file '{args[1]}': {e}")
        new_file_name: str = ft_input()
        if len(new_file_name) != 0:
            try:
                f: typing.IO = open(new_file_name, "w")
                print(f"Saving data to '{new_file_name}'")
                f.write(new_text)
                print(f"Data saved in file '{new_file_name}'.")
                f.close()
            except (FileNotFoundError, PermissionError, IsADirectoryError,
                    OSError) as e:
                sys.stderr.write(
                    f"[STDERR] Error opening file '{args[1]}': {e}\n"
                    "Data not saved.")
        else:
            print("Not saving data.")
    else:
        print(f"Usage: {args[0]} <file>")


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation  ===")
    cat()


if __name__ == "__main__":
    main()
