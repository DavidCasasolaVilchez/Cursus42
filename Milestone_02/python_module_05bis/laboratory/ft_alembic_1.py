import alchemy


if __name__ == "__main__":
    print(
        "=== Alembic 1 ===\n"
        "Accessing the alchemy module using 'import alchemy'\n"
        f"Testing create_air: {alchemy.create_air()}\n"
        "Now show that not all functions can be reached\n"
        "This will raise an exception!\n"
        "Testing the hidden create_earth: ",
        end="", flush=True
    )
    alchemy.create_earth()
