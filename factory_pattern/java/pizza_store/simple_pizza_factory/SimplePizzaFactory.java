package pizza_store.simple_pizza_factory;

import pizza_store.pizza.Pizza;


public class SimplePizzaFactory {
    public Pizza orderPizza(String type) {
        Pizza pizza = null;

        if (type.equals("cheese")) {
            pizza = new CheesePizza();
        } else if (type.equals("pepperoni")) {
            pizza = new PepperoniPizza();
        } else if (type.equals("veggie")) {
            pizza = new VeggiePizza();
        } else if (type.equals("clam")) {
            pizza = new ClamPizza();
        }

        return pizza;
    }
}