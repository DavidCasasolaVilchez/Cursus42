from typing import TYPE_CHECKING
from Models.Dron import Dron

if TYPE_CHECKING:
    from Models.Zone import Zone


class Connection():
    def __init__(self, z1: str, z2: str, mlc: int = 1) -> None:
        self.drones_in: list[Dron] = list()
        self.drones_poblation: int = 0
        self.max_link_capacity: int = mlc
        self.zone_name1: str = z1
        self.zone_name2: str = z2
        self.zone1: Zone
        self.zone2: Zone

    def __str__(self) -> str:
        return (f"{self.zone_name1}-{self.zone_name2}")

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash((self.zone1, self.zone2))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Connection):
            return False
        return (
            self.zone_name1 == other.zone_name1 and
            self.zone_name2 == other.zone_name2
        )
