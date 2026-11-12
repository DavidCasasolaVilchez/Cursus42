from __future__ import annotations
from Utils.Colors import COLOURS, draw_rainbow
from Models.Connection import Connection
from typing import TYPE_CHECKING
from Models.Route import Route
from Models.Dron import Dron

if TYPE_CHECKING:
    from Models.Zone import Zone


class Network():
    routes: list[Route]

    def __init__(self, sz: Zone, ez: Zone, zones: list[Zone],
                 connection: list[Connection], nd: int) -> None:
        self.connection: list[Connection] = connection
        self.drones: list[Dron] = list()
        self.zones: list[Zone] = zones
        self.dron_number: int = nd
        self.start_zone: Zone = sz
        self.end_zone: Zone = ez
        self.end: bool = False
        for i in range(self.dron_number):
            dron: Dron = Dron(i + 1, self.start_zone)
            self.drones.append(dron)
            self.start_zone.drones_in.append(dron)

    def clean_waiters(self) -> None:
        for i in self.zones:
            i.drones_waiting = list()

    def clean_cons(self) -> None:
        for i in self.connection:
            i.drones_poblation = 0

    def __str__(self) -> str:
        s: str = ""
        for zone in self.zones:
            aux: str = ""
            aux += f"{zone.name} -> "
            for d in zone.drones_in:
                aux += f"{d} "
            if zone.color == "":
                s += draw_rainbow(aux)
            else:
                s += (f"{zone.color}{aux}{COLOURS['reset']}")
            s += "\n"
        return s

    def __repr__(self) -> str:
        return self.__str__()
