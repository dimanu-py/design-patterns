from abc import ABC, abstractmethod

from ingredients.dough import Dough
from ingredients.sauce import Sauce
from ingredients.cheese import Cheese
from ingredients.veggies import Veggies
from ingredients.pepperoni import Pepperoni
from ingredients.clams import Clams


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

    def __init__(self) -> None:
        super().__init__()
        self.name = "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")


class PepperoniPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Sliced Onion")
        self.toppings.append("Grated parmesan cheese")


class VeggiePizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Veggie Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings.append("Shredded Mozzarella")
        self.toppings.append("Grated Parmesan")
        self.toppings.append("Diced Onion")
        self.toppings.append("Sliced Mushrooms")
        self.toppings.append("Sliced Red Pepper")
        self.toppings.append("Sliced Black Olives")


class ClamPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Clam Pizza"
        self.dough = "Thin Crust"
        self.sauce = "White Garlic Sauce"
        self.toppings.append("Clams")
        self.toppings.append("Grated Parmesan")


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
