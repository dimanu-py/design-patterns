from abc import ABC, abstractmethod

from .types import BuildingType, WindowType, DoorType


class Builder(ABC):
    """Steps to follow to construct an object."""

    @abstractmethod
    def set_building_type(self, _type: BuildingType) -> None:
        """Sets building type."""

    @abstractmethod
    def set_number_walls(self, number_walls: int) -> None:
        """Sets number walls of the house"""

    @abstractmethod
    def set_number_windows(self, number_windows: int) -> None:
        """Sets number of windows of the house"""

    @abstractmethod
    def set_window_type(self, _type: WindowType) -> None:
        """Sets the material of the window"""

    @abstractmethod
    def set_number_doors(self, number_doors: int) -> None:
        """Sets the number of doors of the house"""

    @abstractmethod
    def set_door_type(self, _type: DoorType) -> None:
        """Sets the material of the door"""
