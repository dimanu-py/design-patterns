from abc import ABC, abstractmethod


class Pepperoni(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class SlicedPepperoni(Pepperoni):

    def __str__(self) -> str:
        return "Sliced Pepperoni"
