from Utils.Exceptions.InvalidNextMoveException import InvalidNextMoveException
from Utils.Enums.ZoneType import ZoneType
from Models.Zone import Zone


class Route():
    def __init__(self, actual: Zone) -> None:
        self.route: list[Zone] = [actual]
        self.actual: Zone = actual
        self.priority: int = 0
        self.weight: int = 0

    @staticmethod
    def constructor(last: "Route", node_new: Zone, extra_turn: int) -> "Route":
        new: "Route" = Route(node_new)
        new.route = last.route.copy()
        new.route.append(node_new)
        for _ in range(extra_turn):
            new.route.append(node_new)
        new.actual = node_new
        new.priority += last.priority
        new.weight += node_new.get_weigth(last.weight) + extra_turn
        if node_new.zone_type == ZoneType.PRIORITY:
            new.priority += 1
        return new

    def get_next(self, node: Zone) -> Zone:
        for i, n in enumerate(self.route):
            if n == node:
                return self.route[i + 1]
        raise InvalidNextMoveException()

    def __str__(self) -> str:
        s: str = "["
        for i, zone in enumerate(self.route):
            s += f"{zone.name}" + (" -> " if i < (len(self.route)-1) else "]")
        return (
                f"Route: {s}\n" +
                f"  -Weight = {self.weight}\n" +
                f"  -Priority = {self.priority}"
            )

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Route):
            return False
        return (
            self.actual == other.actual and
            self.route == other.route and
            self.priority == other.priority and
            self.weight == other.weight
        )
