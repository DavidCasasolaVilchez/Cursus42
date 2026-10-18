def secure_archive(fname: str, action: int = 0, txt: str = "") -> tuple:
    try:
        if action == 1:
            with open(fname, "r") as file:
                txt = file.read()
            return (True, txt)
        if action == 0:
            with open(fname, "w") as file:
                file.write(txt)
            return (True, "Content successfully written to file")
        return (False, "Invalid action")
    except (FileNotFoundError, PermissionError) as e:
        return (False, f"[Errno {e.errno}] {e.args[1]}: '{e.filename}'")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 1))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("b.txt", 1))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("a.txt", 1))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new.txt", 0))


if __name__ == "__main__":
    main()
