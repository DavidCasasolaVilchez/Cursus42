import data_processor as dp
import data_pipeline as dpi
import typing


class DataStream:
    def __init__(self) -> None:
        self.processors: list[dp.DataProcessor] = list()

    def register_processor(self, proc: dp.DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        error_msg: str = "DataStream error - Can't process element in stream:"
        for element in stream:
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print(f"{error_msg} {element}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
            return
        for processor in self.processors:
            name = type(processor).__name__.replace("Processor", " Processor")
            print(
                f"{name}: total {processor._rank} items processed, "
                f"remaining {len(processor._data)} on processor"
            )
        print()

    def output_pipeline(self, nb: int, plugin: dpi.ExportPlugin) -> None:
        ls: list[tuple[int, str]]
        for p in self.processors:
            nbaux: int = nb
            ls = list()
            if nb > p._count:
                nbaux = p._count
            for i in range(0, nbaux):
                ls.append(p.output())
            plugin.process_output(ls)
            print(f"{plugin.txt}")
            plugin.restart_txt()


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    stream = DataStream()
    print("\nInitialize Data Stream...")
    stream.print_processors_stats()

    numeric = dp.NumericProcessor()
    text = dp.TextProcessor()
    log = dp.LogProcessor()
    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message":
             "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("\nRegistering Numeric Processor")
    stream.register_processor(numeric)
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1")
    numeric.consume(3)
    text.consume(2)
    log.consume(1)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
