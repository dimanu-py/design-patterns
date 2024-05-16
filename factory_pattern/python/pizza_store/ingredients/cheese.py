from abc import ABC, abstractmethod


class Cheese(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class MozzarellaCheese(Cheese):

    def __str__(self) -> str:
        return "Mozzarella Cheese"


class ReggianoCheese(Cheese):

    def __str__(self) -> str:
        return "Reggiano Cheese"
