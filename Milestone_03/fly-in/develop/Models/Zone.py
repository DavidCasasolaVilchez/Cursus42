from Utils.Enums.ZoneType import ZoneType
from Models.Connection import Connection
from Models.Dron import Dron


class Zone():
    def __init__(self, name: str, pos: tuple[int, int],
                 zone_type: ZoneType = ZoneType.NORMAL,
                 max_drones: int = 1,
                 color: str = "none") -> None:
        self.connections: list[Connection] = list()
        self.drones_waiting: list[Dron] = list()
        self.zone_type: ZoneType = zone_type
        self.drones_in: list[Dron] = list()
        self.max_drones: int = max_drones
        self.pos: tuple[int, int] = pos
        self.color: str = color
        self.name: str = name

    def get_weigth(self, num: int) -> int:
        weigth: int = num
        for _ in self.drones_waiting:
            weigth += 1
        if len(self.drones_in) == self.max_drones:
            weigth += 1
        weigth += self.zone_type.value[1]
        return weigth

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash((self.name, self.pos))

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Zone):
            return False
        return (
            self.zone_type == other.zone_type and
            self.pos == other.pos and
            self.name == other.name
        )
