def garden_operations(operation_number: int) -> int:
    match operation_number:
        case 0:
            int("adc")
        case 1:
            10 / 0
        case 2:
            open("/non/existent/file")
        case 3:
            "hola" + 123
    return operation_number


def test_error_types() -> None:
    i = 0
    try:
        print(f"Testing operation {i}...")
        garden_operations(i)
        print("Operation completed successfully")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")
    i += 1
    try:
        print(f"Testing operation {i}...")
        garden_operations(i)
        print("Operation completed successfully")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")
    i += 1
    try:
        print(f"Testing operation {i}...")
        garden_operations(i)
        print("Operation completed successfully")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")
    i += 1
    try:
        print(f"Testing operation {i}...")
        garden_operations(i)
        print("Operation completed successfully")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")
    i += 1
    try:
        print(f"Testing operation {i}...")
        garden_operations(i)
        print("Operation completed successfully")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")
    i += 1


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
