def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        num = input_temperature("25")
        print(f"Temperature is now {num}ºC")
        print("\nInput data is 'abc'")
        num = input_temperature("abc")
        print(f"Temperature is now {num}ºC")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
