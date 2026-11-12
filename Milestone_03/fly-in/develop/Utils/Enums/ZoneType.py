from enum import Enum


class ZoneType(Enum):
    BLOCKED = (0, 0)
    NORMAL = (1, 1)
    RESTRICTED = (2, 2)
    PRIORITY = (3, 1)
