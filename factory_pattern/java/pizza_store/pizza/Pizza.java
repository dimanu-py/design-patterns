package pizza_store.pizza;
import java.util.ArrayList;

abstract public class Pizza {
	String name;
    Dough dough;
    Sauce sauce;
    Cheese cheese;
    Vegies veggies[];
    Pepperoni pepperoni;
    Clams clams;

    public abstract void prepare();

    public void bake() {
        System.out.println("Bake for 25 minutes at 350");
    }

    public void cut() {
        System.out.println("Cutting the pizza into diagonal slices");
    }

    public void box() {
        System.out.println("Place pizza in official PizzaStore box");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
	public String toString() {
		StringBuffer display = new StringBuffer();
		display.append("---- " + name + " ----\n");
		display.append(dough + "\n");
		display.append(sauce + "\n");
		for (int i = 0; i < veggies.size(); i++) {
			display.append((String )veggies.get(i) + "\n");
		}
		return display.toString();
	}
}