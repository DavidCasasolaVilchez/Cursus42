import sys
import typing


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
            new_file_name: str = input("Enter new file name (or empty): ")
            if len(new_file_name) != 0:
                with open(new_file_name, "w") as f:
                    print(f"Saving data to '{new_file_name}'")
                    f.write(new_text)
                    print(f"Data saved in file '{new_file_name}'.")
            else:
                print("Not saving data.")
        except (FileNotFoundError, PermissionError, IsADirectoryError,
                OSError) as e:
            print(f"Error opening file '{args[1]}': {e}")
    else:
        print(f"Usage: {args[0]} <file>")


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation  ===")
    cat()


if __name__ == "__main__":
    main()
