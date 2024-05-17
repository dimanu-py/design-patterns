from abc import ABC, abstractmethod

from ingredients import dough, sauce, cheese, veggies, pepperoni, clams
from pizza import Pizza, CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza
from pizza_store import PizzaStore


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


class NewYorkPizzaStore(PizzaStore):

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self.ingredient_factory = ingredient_factory


    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            pizza = CheesePizza(self.ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif pizza_type == "clam":
            pizza = ClamPizza(self.ingredient_factory)
            pizza.name = "New York Style Clam Pizza"
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(self.ingredient_factory)
            pizza.name = "New York Style Pepperoni Pizza"
        elif pizza_type == "veggie":
            pizza = VeggiePizza(self.ingredient_factory)
            pizza.name = "New York Style Veggie Pizza"
        else:
            raise ValueError(f"Invalid pizza type: {pizza_type}")

        return pizza


class ChicagoPizzaStore(PizzaStore):

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self.ingredient_factory = ingredient_factory

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            pizza = CheesePizza(self.ingredient_factory)
            pizza.name = "Chicago Style Cheese Pizza"
        elif pizza_type == "clam":
            pizza = ClamPizza(self.ingredient_factory)
            pizza.name = "Chicago Style Clam Pizza"
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(self.ingredient_factory)
            pizza.name = "Chicago Style Pepperoni Pizza"
        elif pizza_type == "veggie":
            pizza = VeggiePizza(self.ingredient_factory)
            pizza.name = "Chicago Style Veggie Pizza"
        else:
            raise ValueError(f"Invalid pizza type: {pizza_type}")

        return pizza