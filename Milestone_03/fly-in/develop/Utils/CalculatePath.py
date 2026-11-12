from __future__ import annotations

from Utils.Exceptions.RouteNotFoundException import RouteNotFoundException
from Utils.Enums.ZoneType import ZoneType
from Models.Network import Network
from typing import TYPE_CHECKING
from Models.Route import Route

if TYPE_CHECKING:
    from Models.Zone import Zone


def select_lighter_path(network: Network, start: Zone) -> Route:
    all_paths: list[Route] = []
    pending: list[Route] = [Route(start)]
    path: Route
    while pending:
        path = pending.pop(0)
        if path.actual == network.end_zone:
            all_paths.append(path)
            continue
        extra: int = 0
        for con in path.actual.connections:
            if con.drones_poblation == con.max_link_capacity:
                extra += 1
            if (con.zone2.zone_type != ZoneType.BLOCKED and
                    con.zone2 not in path.route):
                pending.append(Route.constructor(path, con.zone2, extra))
        pending = sorted(pending, key=lambda route: route.weight)
    all_paths = sorted(
        all_paths, key=lambda route: (route.weight, -route.priority))
    if not all_paths:
        raise RouteNotFoundException
    return all_paths[0]
