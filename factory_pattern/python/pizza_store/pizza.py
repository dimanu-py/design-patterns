


class Pizza:

    def __init__(self) -> None:
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self) -> None:
        print(f"Preparing {self.name}")

    def bake(self) -> None:
        print(f"Baking {self.name}")

    def cut(self) -> None:
        print(f"Cutting {self.name}")

    def box(self) -> None:
        print(f"Boxing {self.name}")

    def __str__(self) -> str:
        return f"""
            Name: {self.name}
            Dough: {self.dough}
            Sauce: {self.sauce}
            Toppings: {self.toppings}
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


class GreekPizza(Pizza):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Greek Pizza"
        self.dough = "Thin Crust"
        self.sauce = "Greek Sauce"
        self.toppings.append("Feta Cheese")
        self.toppings.append("Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Onion")
