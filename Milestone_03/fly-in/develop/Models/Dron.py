from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Models.Zone import Zone


class Dron():
    def __init__(self, id: int, zone: Zone) -> None:
        self.id: int = id
        self.node: Zone = zone
        self.blocked: bool = False

    def __str__(self) -> str:
        return f"D{self.id}"

    def __repr__(self) -> str:
        return self.__str__()
