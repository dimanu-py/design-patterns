from abc import ABC, abstractmethod


class Sauce(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class MarinaraSauce(Sauce):

    def __str__(self) -> str:
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):

    def __str__(self) -> str:
        return "Plum Tomato Sauce"
