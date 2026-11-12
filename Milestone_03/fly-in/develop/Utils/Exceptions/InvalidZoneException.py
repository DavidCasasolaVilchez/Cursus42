class InvalidZoneException(Exception):
    def __init__(self, msg: str = "Invalid Zone") -> None:
        super().__init__(msg)
