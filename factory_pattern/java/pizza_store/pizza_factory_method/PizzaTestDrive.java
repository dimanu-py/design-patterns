package pizza_store.pizza_factory_method;


public class PizzaTestDrive {

    public static void main(String[] args) {
        PizzaStore NewYorkStore = new NewYorkPizzaStore();
        PizzaStore ChicagoStore = new ChicagoPizzaStore();

        Pizza pizza = NewYorkStore.orderPizza("cheese");
        System.out.println("Ethan ordered a " + pizza.getName() + "\n");

        pizza = ChicagoStore.orderPizza("pepperoni");
        System.out.println("Joel ordered a " + pizza.getName() + "\n");
    }
}