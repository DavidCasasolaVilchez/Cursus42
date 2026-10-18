import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._rank: int = 0
        self._count: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        """Return whether data can be ingested by this processor."""
        raise NotImplementedError

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        """Convert and store data for later output."""
        raise NotImplementedError

    def output(self) -> tuple[int, str]:
        self._count -= 1
        return self._data.pop(0)

    def consume(self, num: int) -> None:
        del self._data[:num]
        self._count -= 1

    def _store(self, data: str) -> None:
        self._rank += 1
        self._count += 1
        self._data.append((self._rank, data))


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(type(item) in (int, float) for item in data)
        return type(data) in (int, float)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        values = data if isinstance(data, list) else [data]
        for value in values:
            self._store(str(value))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("TextProcessor accepts str or lists of strings")
        values = data if isinstance(data, list) else [data]
        for value in values:
            self._store(value)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        def is_log(value: typing.Any) -> bool:
            return (
                isinstance(value, dict)
                and all(
                    isinstance(key, str) and isinstance(item, str)
                    for key, item in value.items()
                )
            )

        if isinstance(data, list):
            return all(is_log(item) for item in data)
        return is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError(
                "LogProcessor accepts dicts with string keys and values"
            )
        values = data if isinstance(data, list) else [data]
        for value in values:
            if "log_level" in value and "log_message" in value:
                self._store(f"{value['log_level']}: {value['log_message']}")
            else:
                self._store(str(value))


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print("Trying to validate input '42':", numeric.validate(42))
    print("Trying to validate input 'Hello':", numeric.validate("Hello"))
    print("Test invalid ingestion of string 'foo'without prior validation:")
    try:
        # Debe fallar el mypy
        numeric.ingest("foo")
    except TypeError as error:
        print(f"Got exception: {error}")

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for index in range(3):
        print(f"Numeric value {index}: {numeric.output()[1]}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print("Trying to validate input '42':", text.validate(42))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    print(f"Text value 0: {text.output()[1]}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print("Trying to validate input 'Hello':", log.validate("Hello"))
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    print("Extracting 2 values...")
    for index in range(2):
        print(f"Log entry {index}: {log.output()[1]}")


if __name__ == "__main__":
    main()
