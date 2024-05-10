from pizza import Pizza, CheesePizza, PepperoniPizza, VeggiePizza, ClamPizza


class SimplePizzaFactory:

    @staticmethod
    def order_pizza(pizza_type: str) -> Pizza:
        pizza: Pizza = None

        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza()

        return pizza
