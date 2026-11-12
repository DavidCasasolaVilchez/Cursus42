from Utils.Exceptions.InvalidArgumentException import InvalidArgumentException
from Utils.NetworkParser import NetworkParser
from Models.Execution import Execution
import sys


def main() -> None:
    if len(sys.argv) != 2:
        raise InvalidArgumentException

    file_name: str = sys.argv[1]
    np: NetworkParser = NetworkParser(file_name)
    np.parse_file()
    ex: Execution = Execution(np.network)
    ex.run()


if __name__ == "__main__":
    main()
