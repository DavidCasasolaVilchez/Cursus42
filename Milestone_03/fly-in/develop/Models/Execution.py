from Utils.CalculatePath import select_lighter_path
from Models.Network import Network
from Utils.Movement import move
from Models.Dron import Dron
from Models.Zone import Zone


class Execution():
    def __init__(self, network: Network) -> None:
        self.network_base: Network = network
        self.log: list[Network] = [network]

    def run(self) -> None:
        index: int = 0
        while (len(self.network_base.end_zone.drones_in) <
               self.network_base.dron_number):
            movements: list[str] = self.new_turn(index)
            if len(movements) == 0:
                raise RuntimeError(
                    "La ejecución no puede avanzar: ningún dron se ha movido."
                )
            else:
                print(f"Turn {index} [{len(movements)} drons moved]: ",
                      end="", flush=True)
                for i in movements:
                    print(f"{i}", end=" ", flush=True)
                print("\n")
            index += 1

    def new_turn(self, i: int) -> list[Dron]:
        move_drons: list[str] = list()

        self.network_base.clean_waiters()
        self.network_base.clean_cons()
        for d in self.network_base.drones:
            if d.node == self.network_base.end_zone:
                continue
            path = select_lighter_path(self.network_base, d.node)
            next_zone: Zone = path.get_next(d.node)

            connection = next(
                con for con in self.network_base.connection
                if con.zone1 is d.node and con.zone2 is next_zone
            )

            has_capacity = (
                next_zone is self.network_base.end_zone or
                len(next_zone.drones_in) < next_zone.max_drones
            )

            if (has_capacity and
               connection.drones_poblation <
               connection.max_link_capacity):
                move_drons.append(
                    move(self.network_base, d, connection, next_zone))
                connection.drones_poblation += 1
            else:
                next_zone.drones_waiting.append(d)

        return move_drons
