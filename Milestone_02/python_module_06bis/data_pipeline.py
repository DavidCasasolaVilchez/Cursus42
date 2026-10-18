import data_processor as dp
import typing


class ExportPlugin(typing.Protocol):
    txt: str

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass

    def restart_txt(self) -> None:
        pass


class PluginCSV(ExportPlugin):
    def __init__(self):
        self.txt = "CSV Output\n"

    def restart_txt(self) -> None:
        self.txt = "CSV Output\n"

    def process_output(self, data: list[tuple[int, str]]) -> None:
        for i in data:
            self.txt += f"{i[1]},"
        self.txt = self.txt.removesuffix(",")


class PluginJSON(ExportPlugin):
    def __init__(self):
        self.txt = "JSON Output\n"

    def restart_txt(self) -> None:
        self.txt = "JSON Output\n"

    def process_output(self, data: list[tuple[int, str]]) -> None:
        self.txt += "{"
        for i in data:
            self.txt += f"\"item_{i[0] - 1}\": \"{i[1]}\", "
        self.txt = self.txt.removesuffix(", ")
        self.txt += "}"


def main() -> None:
    import data_stream as ds

    print("=== Code Nexus - Data Pipeline ===")
    stream = ds.DataStream()
    print("\nInitialize Data Stream...\n")
    stream.print_processors_stats()
    csv: PluginCSV = PluginCSV()
    json: PluginJSON = PluginJSON()
    numeric: dp.NumericProcessor = dp.NumericProcessor()
    text: dp.TextProcessor = dp.TextProcessor()
    log: dp.LogProcessor = dp.LogProcessor()
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
    batch2 = [
        21,
        [
            'I love AI',
            'LLMs are wonderful',
            'Stay healthy'
        ],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE', 'log_message':
             'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print("Registering other data processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    print(f"Send first batch of data on stream: {batch}\n")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv)
    stream.print_processors_stats()

    print(f"Send another batch of data: {batch2}\n")
    stream.process_stream(batch2)
    stream.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
