class InvalidArgsException(Exception):
    def __init__(self, msg: str = "The arguments must be valids") -> None:
        super().__init__(msg)
