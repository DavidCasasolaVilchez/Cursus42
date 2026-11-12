class RouteNotFoundException(Exception):
    def __init__(self, msg: str = "Route not found") -> None:
        super().__init__(msg)
