from abc import ABC, abstractmethod

from ingredients import dough, sauce, cheese, veggies, pepperoni, clams


class PizzaIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self) -> dough.Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> sauce.Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> cheese.Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> list[veggies.Veggies]:
        pass

    @abstractmethod
    def create_pepperoni(self) -> pepperoni.Pepperoni:
        pass

    @abstractmethod
    def create_clam(self) -> clams.Clams:
        pass


class NewYorkPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self) -> dough.Dough:
        return dough.ThinCrustDough()

    def create_sauce(self) -> sauce.Sauce:
        return sauce.MarinaraSauce()

    def create_cheese(self) -> cheese.Cheese:
        return cheese.ReggianoCheese()

    def create_veggies(self) -> list[veggies.Veggies]:
        pizza_veggies = [
            veggies.Garlic(),
            veggies.Onion(),
            veggies.Mushroom(),
            veggies.RedPepper()
        ]
        return pizza_veggies

    def create_pepperoni(self) -> pepperoni.Pepperoni:
        return pepperoni.SlicedPepperoni()

    def create_clam(self) -> clams.Clams:
        return clams.FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self) -> dough.Dough:
        return dough.ThickCrustDough()

    def create_sauce(self) -> sauce.Sauce:
        return sauce.PlumTomatoSauce()

    def create_cheese(self) -> cheese.Cheese:
        return cheese.MozzarellaCheese()

    def create_veggies(self) -> list[veggies.Veggies]:
        pizza_veggies = [
            veggies.BlackOlives(),
            veggies.Spinach(),
            veggies.EggPlant()
        ]
        return pizza_veggies

    def create_pepperoni(self) -> pepperoni.Pepperoni:
        return pepperoni.SlicedPepperoni()

    def create_clam(self) -> clams.Clams:
        return clams.FrozenClams()