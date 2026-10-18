import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    args = sys.argv
    print(f"Program name: {args[0]}")
    if len(args) <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        for i in range(1, len(args)):
            print(f"Argument {i}: {args[i]}")
    print(f"Total arguments: {len(args)}")
