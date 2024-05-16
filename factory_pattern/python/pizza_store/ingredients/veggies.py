from abc import ABC, abstractmethod


class Veggies(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class BlackOlives(Veggies):

    def __str__(self) -> str:
        return "Black Olives"


class EggPlant(Veggies):

    def __str__(self) -> str:
        return "Egg Plant"


class Spinach(Veggies):

    def __str__(self) -> str:
        return "Spinach"


class Mushroom(Veggies):

    def __str__(self) -> str:
        return "Mushroom"


class RedPepper(Veggies):

    def __str__(self) -> str:
        return "Red Pepper"


class Onion(Veggies):

    def __str__(self) -> str:
        return "Onion"


class Garlic(Veggies):

    def __str__(self) -> str:
        return "Garlic"
