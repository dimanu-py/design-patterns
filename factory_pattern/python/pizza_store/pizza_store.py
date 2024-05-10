from pizza import Pizza, CheesePizza, PepperoniPizza, VeggiePizza, ClamPizza
from simple_pizza_factory import SimplePizzaFactory


class PizzaStore:

    def __init__(self, factory: SimplePizzaFactory) -> None:
        self.factory = factory

    def order_pizza(self, pizza_type):
        pizza: Pizza = self.factory.order_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
