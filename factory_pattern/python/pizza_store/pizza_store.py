from pizza import Pizza, CheesePizza, PepperoniPizza, VeggiePizza, ClamPizza


class PizzaStore:

    @classmethod
    def order_pizza(cls, pizza_type):
        pizza: Pizza = None

        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza()

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
