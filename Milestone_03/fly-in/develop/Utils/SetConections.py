from Utils.Exceptions.InvalidZoneException import InvalidZoneException
from Models.Connection import Connection
from Models.Network import Network


def link_connection(connection: Connection, network: Network) -> Connection:
    nodeA: int = -1
    nodeB: int = -1
    for i, zone in enumerate(network.zones):
        if zone.name == connection.zone_name1:
            nodeA = i
        elif zone.name == connection.zone_name2:
            nodeB = i
    if nodeA == -1 or nodeB == -1:
        raise InvalidZoneException
    connection.zone1 = network.zones[nodeA]
    connection.zone2 = network.zones[nodeB]
    network.zones[nodeA].connections.append(connection)
    network.zones[nodeB].connections.append(connection)
    return connection


def set_connection(network: Network) -> Network:
    for i, connection in enumerate(network.connection):
        network.connection[i] = link_connection(connection, network)
    return network
