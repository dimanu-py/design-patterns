from pizza import Pizza, CheesePizza, PepperoniPizza, GreekPizza


class PizzaStore:

    @classmethod
    def order_pizza(cls, pizza_type):
        pizza: Pizza = None

        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'greek':
            pizza = GreekPizza()

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
