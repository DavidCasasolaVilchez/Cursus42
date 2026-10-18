def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        num = input_temperature("25")
        print(f"Temperature is now {num}ºC")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    try:
        print("\nInput data is 'abc'")
        num = input_temperature("abc")
        print(f"Temperature is now {num}ºC")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    try:
        print("\nInput data is '100'")
        num = input_temperature("100")
        print(f"Temperature is now {num}ºC")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    try:
        print("\nInput data is '-50'")
        num = input_temperature("-50")
        print(f"Temperature is now {num}ºC")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
