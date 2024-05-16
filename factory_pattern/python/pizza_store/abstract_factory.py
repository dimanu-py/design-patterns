from abc import ABC, abstractmethod


class PizzaIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> list[Veggies]:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass

    @abstractmethod
    def create_clam(self) -> Clams:
        pass
