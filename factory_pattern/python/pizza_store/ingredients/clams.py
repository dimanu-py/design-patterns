from abc import ABC, abstractmethod


class Clams(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class FreshClams(Clams):

    def __str__(self) -> str:
        return "Fresh Clams from Long Island Sound"


class FrozenClams(Clams):

    def __str__(self) -> str:
        return "Frozen Clams from Chesapeake Bay"
