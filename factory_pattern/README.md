# Factory Pattern

> [!IMPORTANT]
> The Factory Pattern is a creational pattern that let us separate the object creation from its use, providing a way to create objects without specifying the concrete class to create.

By encapsulating the behavior that changes:
1. We are able to isolate the client code from the changes in the concrete classes, reducing the coupling between the client and the concrete classes
2. We use abstractions to decouple the client from the concrete classes, applying the Program to an Interface and Dependency Inversion principles.
3. We separate the responsibilities of use and creation, following the Separation of Concerns principle
4. We are able to add new concrete classes without changing the client code because our code only knows the interface of the objects, not its internals. We are open
for extension and closed for modification.

## Simple Factory

> [!IMPORTANT]
> The Simple Factory isn't actually a design pattern, it is more of a programming idiom, however it is commonly used and is worth mentioning

The main objective of the Simple Factory is to encapsulate the object creation logic. This way, the client code doesn't need to know how the object is created, it just needs to know the interface of the object.

### Class diagram & Collaborators

![Simple Factory class diagram](/assets/images/simple_factory_class_diagram.png "Extracted from Head First Design Patterns book")

In the image we see that Simple Factory is composed of the following classes:

- **SimpleFactory**: This class is responsible for creating the objects. It is the object that encapsulates the knowledge of the different concrete classes
- **ConcreteProduct**: These are the concrete classes that implement the interface of the product. They are the objects that will be created by the SimpleFactory
- **Product**: This is the interface that the concrete classes implement. Every class that implements this interface can be created by the SimpleFactory
- **Client**: This is the class that uses the SimpleFactory to create the objects. For the client, it doesn't matter how the object is created, it just needs to know the interface of the object

## Factory Method

> [!IMPORTANT]
> The Factory Method is a design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects will be created

Again, the main objective is to encapsulate the object creation logic from its use. However, the Factory Method allow us to have more flexibility and is 
more suitable for more complex hierarchies.

### Class diagram & Collaborators

![Factory Method class diagram](/assets/images/factory_method_class_diagram.png "Extracted from Head First Design Patterns book")

In the image we see that Factory Method is composed of the following classes:

- **Creator**: Implements the operations to all Products and defines the abstract factory method. The Creator never really knows which concrete Product was produced.
- **ConcreteCreator**: Implements the factory method to create the concrete Product. It is the only class that knows how to create concrete Product.
- **Product**: This is the interface that the concrete classes implement. Every class that implements this interface can be created by the ConcreteCreator
- **ConcreteProduct**: These are the concrete classes that implement the interface of the product. They are the objects that will be created by the ConcreteCreator

> [!NOTE]
> The Factory Method lets subclasses decide which class to instantiate. But here, "decides" is not because the pattern allow the subclasses
> to decide at runtime, but because the Creator is written without the knowledge of the actual Product that will be created, which is decided
> purely by the choice of the ConcreteCreator that is used.

A common question is if the ConcreteCreator always need to make multiple Products or can sometimes just make one. The answer is NO,
the ConcreteCreator can make just one Product. Both ways, parametrized and not parametrized are valid forms.

### Factory Method vs Simple Factory

- The ConcreteCreators extends the behavior of the Creator by creating the ConcreteProduct, while the Simple Factory is just another object
that is composed with the Creator.
- The SimpleFactory gives us a way to encapsulate object creation, but doesn't give us the flexibility that the Factory Method does because
there is no way to vary the Products we're creating.

## Abstract Factory

> [!IMPORTANT]
> The Abstract Factory is a design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.

The main use of the Abstract Factory is to create families of products. This way, the client is decoupled from the concrete products it's creating
and only needs to know the interface to create them.

### Class diagram & Collaborators

![Abstract Factory class diagram](/assets/images/abstract_factory_class_diagram.png "Extracted from Head First Design Patterns book")


## When to use each Factory strategy

- **Simple Factory**: When the object creation logic is simple and doesn't need to be changed. It is a good choice when the number of concrete classes is small and won't change.
- **Factory Method**: When we have a hierarchy of classes. It is a good choice when we have a complex hierarchy of classes, and we want to encapsulate the object creation logic in a single class.
- **Abstract Factory**: When we have families of objects. It is a good choice when we have a family of objects that need to be created together and we want to decouple the client from the concrete classes.