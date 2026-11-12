from Utils.Exceptions.InvalidArgsException import InvalidArgsException
from re import search, Match, findall, fullmatch
from Utils.SetConections import set_connection
from Utils.Enums.ZoneType import ZoneType
from Models.Connection import Connection
from Models.Network import Network
from Utils.Colors import COLOURS
from Models.Zone import Zone
import sys


class NetworkParser():
    zone_pattern: str = (
        r"(?m)^(hub: [a-zA-Z\d_]+ -?\d+ -?\d+( \[.+\])?)")
    start_zone_pattern: str = (
        r"(?m)^(start_hub: [a-zA-Z\d_]+ -?\d+ -?\d+( \[.+\])?)")
    end_zone_pattern: str = (
        r"(?m)^(end_hub: [a-z_A-Z\d_]+ -?\d+ -?\d+( \[.+\])?)")
    nb_drones_pattern: str = (r"(?m)^(nb_drones: \d+)")
    connection_pattern: str = (r"(?m)^(connection: \w+-\w+( \[.+\])?)")
    comment: str = (r"(?m)^#.*")
    invalid: str = (f"{zone_pattern}|{start_zone_pattern}"
                    f"|{end_zone_pattern}|{nb_drones_pattern}"
                    f"|{connection_pattern}|{comment}")

    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name
        self.network: Network

    def parse_file(self) -> None:
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                connections: list[Connection] = list()
                zones: list[Zone] = list()
                filetxt: str = file.read()

                if (len(findall("start_hub", filetxt)) != 1 or
                   len(findall("end_hub", filetxt)) != 1):
                    raise InvalidArgsException(
                        "start_hub and end_hub must be unique")
                for line in filetxt.splitlines():
                    if len(line) != 0 and not fullmatch(self.invalid, line):
                        raise InvalidArgsException(
                            "There should be no invalid lines.")

                end_match: Match[str] | None = search(self.end_zone_pattern,
                                                      filetxt)
                if end_match is not None:
                    end: Zone = self.parse_zone(end_match.group())
                else:
                    raise InvalidArgsException("Invalid zone")

                start_match: Match[str] | None = search(
                    self.start_zone_pattern, filetxt)
                if start_match is not None:
                    start: Zone = self.parse_zone(start_match.group())
                else:
                    raise InvalidArgsException("Invalid zone")

                zones_match: list[Match[str]] = findall(self.zone_pattern,
                                                        filetxt)
                for zone in zones_match:
                    zones.append(self.parse_zone(zone[0]))
                zones.extend((start, end))

                connections_match: list[Match[str]] = findall(
                    self.connection_pattern, filetxt)
                for con in connections_match:
                    conect: Connection = self.parse_connection(con[0], zones)
                    for obj in connections:
                        if (
                            (obj.zone_name1 == conect.zone_name1 and
                                obj.zone_name2 == conect.zone_name2) or
                            (obj.zone_name1 == conect.zone_name2 and
                                obj.zone_name2 == conect.zone_name1)
                        ):
                            raise InvalidArgsException(
                                "The connections can not be repited")
                    connections.append(conect)

                n_drones_match: Match[str] | None = search(
                    self.nb_drones_pattern, filetxt)
                if n_drones_match is not None:
                    nb_drones: int = int(
                        n_drones_match.group().split(" ", 2)[1])
                else:
                    raise InvalidArgsException(
                        "The number of drones must follow this format: " +
                        "nb_drones: <num>"
                    )

                self.network = Network(
                    ez=end,
                    sz=start,
                    zones=zones,
                    connection=connections,
                    nd=nb_drones
                )
                self.validator()
                self.network = set_connection(self.network)

        except OSError as error:
            print(f"Cannot read file: {error}")
            sys.exit(1)

    def validator(self) -> None:
        names: list[str] = [obj.name for obj in self.network.zones]
        if len(names) != len(self.network.zones):
            raise InvalidArgsException(
                "Zone names cannot be duplicated."
            )

        pos: list[tuple[int, int]] = [obj.pos for obj in self.network.zones]
        if len(pos) != len(self.network.zones):
            raise InvalidArgsException(
                "There cannot be repeated zone positions."
            )

        for con in self.network.connection:
            if not (
                any(obj.name == con.zone_name1
                    for obj in self.network.zones) and
                any(obj.name == con.zone_name2
                    for obj in self.network.zones)
            ):
                raise InvalidArgsException(
                    "The connections must link existing zones."
                )

        for i in self.network.connection:
            if i.max_link_capacity < 0:
                raise InvalidArgsException(
                    "The max_link_capacity must be a positive integer."
                )

        for j in self.network.zones:
            if j.max_drones < 0:
                raise InvalidArgsException(
                    "The max_drones must be a positive integer."
                )

        if self.network.dron_number < 1:
            raise InvalidArgsException(
                "The dron_number must be a positive integer."
            )

    @staticmethod
    def parse_connection(line: str, zones: list[Zone]) -> Connection:
        mlink_pattern: str = r"max_link_capacity=\d"
        line = line.removesuffix("\n")
        mlink_match: Match[str] | None = search(mlink_pattern, line)
        lsplited: list[str] = line.split(" ", 3)
        names: list[str] = lsplited[1].split("-", 2)

        connection: Connection = Connection(
            z1=names[0],
            z2=names[1],
        )
        if mlink_match is not None:
            mlink: str = mlink_match.group()
            connection.max_link_capacity = int(mlink.split("=")[1])
        return connection

    @staticmethod
    def parse_zone(line: str) -> Zone:
        zone_pattern: str = (
            r"zone=(normal|blocked|restricted|priority)")
        color_pattern: str = r"color=[a-zA-Z]+"
        mdrones_pattern: str = r"max_drones=\d"
        line = line.removesuffix("\n")

        lsplited: list[str] = line.split(" ")
        x: int = int(lsplited[2])
        y: int = int(lsplited[3])

        zone_match: Match[str] | None = search(zone_pattern, line)
        color_match: Match[str] | None = search(color_pattern, line)
        mdrones_match: Match[str] | None = search(mdrones_pattern, line)

        zone: Zone = Zone(name=lsplited[1], pos=(x, y))
        if zone_match is not None:
            zone = NetworkParser.parse_data(zone_match.group(), zone)
        if color_match is not None:
            zone = NetworkParser.parse_data(color_match.group(), zone)
        if mdrones_match is not None:
            mdrones_str: str = mdrones_match.group()
            if (mdrones_str.__contains__("end_hub") or
                    mdrones_str.__contains__("start_hub")):
                zone.max_drones = 9999999999999999
            else:
                zone = NetworkParser.parse_data(mdrones_match.group(), zone)
        return zone

    @staticmethod
    def parse_data(match: str, zone: Zone) -> Zone:
        spliteo: list[str] = match.split("=")
        match spliteo[0]:
            case "zone":
                match spliteo[1]:
                    case "normal":
                        zone.zone_type = ZoneType.NORMAL
                        return zone
                    case "blocked":
                        zone.zone_type = ZoneType.BLOCKED
                        return zone
                    case "restricted":
                        zone.zone_type = ZoneType.RESTRICTED
                        return zone
                    case "priority":
                        zone.zone_type = ZoneType.PRIORITY
                        return zone
                    case _:
                        raise InvalidArgsException(
                            "The zone type must be valid")
            case "color":
                md_color: str = spliteo[1].strip()
                zone.color = COLOURS.get(md_color, COLOURS["reset"])
                if md_color == "rainbow":
                    zone.color = "r"
                else:
                    zone.color = COLOURS.get(md_color, COLOURS["reset"])
                return zone
            case "max_drones":
                zone.max_drones = int(spliteo[1])
                return zone
            case _:
                raise InvalidArgsException(
                    "The atribute name must be valid"
                )
