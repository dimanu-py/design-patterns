package pizza_store.pizza;

public class VeggiePizza extends Pizza {
    ingredientPizzaFactory ingredientFactory;

    public VeggiePizza(ingredientPizzaFactory ingredientFactory) {
        this.ingredientFactory = ingredientFactory;
    }

    void prepare() {
        System.out.println("Preparing " + name);
        dough = ingredientFactory.createDough();
        sauce = ingredientFactory.createSauce();
        veggies = ingredientFactory.createVeggies();
    }
}