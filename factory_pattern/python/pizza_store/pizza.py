from abc import ABC, abstractmethod

from ingredients.dough import Dough
from ingredients.sauce import Sauce
from ingredients.cheese import Cheese
from ingredients.veggies import Veggies
from ingredients.pepperoni import Pepperoni
from ingredients.clams import Clams

from abstract_factory import PizzaIngredientFactory


class Pizza(ABC):

    def __init__(self) -> None:
        self.name: str = None
        self.dough: Dough = None
        self.sauce: Sauce = None
        self.cheese: Cheese = None
        self.veggies: list[Veggies] = []
        self.pepperoni: Pepperoni = None
        self.clams: Clams = None

    @abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        print("Baking for 25 minutes at 350")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("Place pizza in official PizzaStore box")

    def __str__(self) -> str:
        return f"""
            Name: {self.name}
            Dough: {self.dough}
            Sauce: {self.sauce}
            Veggies: {self.veggies}
            Cheese: {self.cheese}
            Pepperoni: {self.pepperoni}
            Clams: {self.clams}
        """


class CheesePizza(Pizza):

    def __init__(self, ingredients_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredients_factory = ingredients_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredients_factory.create_dough()
        self.sauce = self.ingredients_factory.create_sauce()
        self.cheese = self.ingredients_factory.create_cheese()


class PepperoniPizza(Pizza):

    def __init__(self, ingredients_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredients_factory = ingredients_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredients_factory.create_dough()
        self.sauce = self.ingredients_factory.create_sauce()
        self.cheese = self.ingredients_factory.create_cheese()
        self.pepperoni = self.ingredients_factory.create_pepperoni()


class VeggiePizza(Pizza):

    def __init__(self, ingredients_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredients_factory = ingredients_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredients_factory.create_dough()
        self.sauce = self.ingredients_factory.create_sauce()
        self.veggies = self.ingredients_factory.create_veggies()


class ClamPizza(Pizza):

    def __init__(self, ingredients_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredients_factory = ingredients_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredients_factory.create_dough()
        self.sauce = self.ingredients_factory.create_sauce()
        self.cheese = self.ingredients_factory.create_cheese()
        self.clams = self.ingredients_factory.create_clam()


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Deep Dish Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese", "Black Olives", "Spinach", "Eggplant"]


class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Clam Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese", "Frozen Clams from Chesapeake Bay"]


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese", "Black Olives", "Spinach", "Eggplant", "Sliced Pepperoni"]


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese"]


class NewYorkStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese"]


class NewYorkStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Clam Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese", "Fresh Clams from Long Island Sound"]


class NewYorkStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese", "Sliced Pepperoni", "Garlic", "Onion", "Mushrooms", "Red Pepper"]


class NewYorkStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Veggie Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese", "Garlic", "Onion", "Mushrooms", "Red Pepper"]
