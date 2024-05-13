from pizza_factory_method import NewYorkPizzaStore, ChicagoPizzaStore


def main():
    new_york_store = NewYorkPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = new_york_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.name}\n")

    pizza = chicago_store.order_pizza("pepperoni")
    print(f"Joel ordered a {pizza.name}\n")


if __name__ == '__main__':
    main()