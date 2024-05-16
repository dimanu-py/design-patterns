from abc import ABC, abstractmethod


class Dough(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class Sauce(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class Cheese(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class Veggies(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class Pepperoni(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class Clams(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass