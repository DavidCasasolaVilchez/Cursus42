class InvalidNextMoveException(Exception):
    def __init__(self, msg: str = "Invalid next move") -> None:
        super().__init__(msg)
