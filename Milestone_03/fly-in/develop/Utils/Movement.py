from Utils.CalculatePath import select_lighter_path
from Utils.Colors import COLOURS, draw_rainbow
from Utils.Enums.ZoneType import ZoneType
from Models.Connection import Connection
from Models.Network import Network
from Models.Route import Route
from Models.Dron import Dron
from Models.Zone import Zone


def move(network: Network, dron: Dron,
         con: Connection, next: Zone | None = None) -> str:
    if next is None:
        shortest_path: Route = select_lighter_path(network, dron.node)
        next = shortest_path.get_next(dron.node)
    if next.zone_type == ZoneType.RESTRICTED:
        dron.blocked = True
        if (network.zones[network.zones.index(dron.node)]
                .drones_in.__contains__(dron)):
            network.zones[network.zones.index(dron.node
                                              )].drones_in.remove(dron)
        if (network.zones[network.zones.index(next)]
                .drones_waiting.__contains__(dron)):
            network.zones[network.zones.index(
                next)].drones_waiting.remove(dron)
        dron.node = next
        con.drones_in.append(dron)
        dron.node.drones_in.append(dron)
        if next.color == "":
            return draw_rainbow(f"{dron}-{con}")
        else:
            return f"{next.color}{dron}-{con}{COLOURS['reset']}"
    else:
        if dron.node == network.end_zone:
            return 0
        if (dron.blocked):
            dron.blocked = False
            for c in network.connection:
                if c.drones_in.__contains__(dron):
                    c.drones_in.remove(dron)
        else:
            if (network.zones[network.zones.index(dron.node)]
                    .drones_in.__contains__(dron)):
                network.zones[network.zones.index(dron.node
                                                  )].drones_in.remove(dron)
            if (network.zones[network.zones.index(next)]
                    .drones_waiting.__contains__(dron)):
                network.zones[network.zones.index(
                    next)].drones_waiting.remove(dron)
            network.zones[network.zones.index(next)].drones_in.append(dron)
            dron.node = next
        if next.color == "r":
            return draw_rainbow(f"{dron}-{dron.node}")
        else:
            return f"{next.color}{dron}-{dron.node}{COLOURS['reset']}"

    return ""
