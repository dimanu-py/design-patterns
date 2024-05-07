from enum import StrEnum


class BuildingType(StrEnum):
    """Types of buildings available."""

    HOUSE = "house"
    IGLOO = "igloo"
    CASTLE = "castle"


class WindowType(StrEnum):
    """Materials of windows"""

    WOODEN = "wooden"
    SNOW = "snow"
    ALUMINUM = "aluminum"


class DoorType(StrEnum):
    """Materials of doors"""

    WOODEN = "wooden"
    SNOW = "snow"
    TIMBER = "timber"
