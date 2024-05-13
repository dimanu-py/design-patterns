from factory_pattern.python.pizza_store.pizza import (
    ChicagoStyleCheesePizza,
    ChicagoStyleClamPizza,
    ChicagoStylePepperoniPizza,
    ChicagoStyleVeggiePizza,
    NewYorkStyleCheesePizza,
    NewYorkStyleClamPizza,
    NewYorkStylePepperoniPizza,
    NewYorkStyleVeggiePizza,
    Pizza
)
from pizza_store import PizzaStore


class NewYorkPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            return NewYorkStyleCheesePizza()
        elif pizza_type == "clam":
            return NewYorkStyleClamPizza()
        elif pizza_type == "pepperoni":
            return NewYorkStylePepperoniPizza()
        elif pizza_type == "veggie":
            return NewYorkStyleVeggiePizza()
        else:
            return None


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "clam":
            return ChicagoStyleClamPizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        elif pizza_type == "veggie":
            return ChicagoStyleVeggiePizza()
        else:
            return None