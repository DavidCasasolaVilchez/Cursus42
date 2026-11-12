class InvalidArgumentException(Exception):
    def __init__(
            self, msg: str = "The argument introduced is not valid") -> None:
        super.__init__(msg)
