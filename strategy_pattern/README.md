# Strategy Pattern

> [!IMPORTANT]
> The Strategy Pattern is a behavioral pattern that allow us to define a family of algorithms and make them interchangeable.
> We encapsulate the different algorithms in separate classes.

We can use this pattern when a class can perform an action in different ways. By encapsulating the different behaviors we get the following benefits:
1. The code is more maintainable and extensible, encapsulating the changes within a single class. We favor the Open/Closed principle
2. We move the responsibility of deciding how to behave to separate classes, following the Separation of Concerns principle
3. We can compose our class with different algorithms and change them at runtime. Using composition instead of inheritance makes our code less coupled.

## Class diagram & Collaborators

![Strategy Pattern class diagram](/assets/images/strategy_pattern_class_diagram.png "Extracted from Baeldung on Computer Science webpage")

In the image we can see the Strategy Pattern is composed of two main components:
1. **Context**: is the object that executes the action and can execute it in different ways. Its interface exposes the action, but it delegates the
   behavior to a `Strategy`
2. **Strategy**: is the interface that every concrete strategy will implement. The different strategies will determine how the `Context` performs the
   desired action.

The main idea is that the `Context` class delegates the decision of how to act to the strategies while it exposes a simple API to the client. 

One of the main features of the Strategy pattern is that allow us to change the strategy at runtime, allowing the `Context` to keep its interface
but changing how it behaves.

## When rises the need of this pattern?

In many applications we have different ways of doing an action. In the example bellow we will see that a `Duck` can fly or quack in different ways
depending on the type of Duck. To model this behavior variability within an object the best approach is to apply the Strategy Pattern.

Other alternatives we could think of are:

- **Apply inheritance**: we define the behavior inside a superclass and let the subclasses inherit it.

> [!CAUTION]
> The problem here is that subclasses that may not need this behavior would have it, causing unwanted behavior and unexpected bugs. At the same 
> time, if we want to change the behavior it will affect all the subclasses

- **Override methods**: instead we could define the behavior as an abstract method in the superclass and let the subclasses implement their own behavior

> [!CAUTION]
> The problem now is that new classes that don't need the behavior and inherit it, must override the method to do nothing. Also, we could be duplicating code
> if some subclasses behave in the same way, this will turn into a headache when we change one behavior and review all subclasses that behave in the same way.

- **Define interfaces**: we could define the behaviors as interfaces and let the subclasses implement them or not depending on their needs.

> [!CAUTION]
> Again, the problem with this approach is that we will be duplicating code and decrease the maintainability if several subclasses behave in the same way.

>[!TIP]
> So we see that, to be able to extend our application and manage different ways of behavior for an object, we need an approach that is not coupled and
> let us extend the functionality without affecting the previous code.

## Code examples

The first example uploaded for this patter in the _Duck Simulator_. This example allowed me to understand the concept and the intention behind the pattern.

I've implemented to versions: one for [Python](https://github.com/dimanu-py/design-patterns/tree/main/strategy_pattern/python/1-duck-behavior) and 
another for [Java](https://github.com/dimanu-py/design-patterns/tree/main/strategy_pattern/java/1-duck-behavior)

To see in more detail the structure and the collaborators' implementation in each language, you can go through the files or browse the commits from the following links:
- [Initial state of the application, when strategy is not need it](https://github.com/dimanu-py/design-patterns/commit/beb155549b9bacbc4a5cb69bdce037af1dd3c723)
- [Why inherit behavior from superclass is bad idea](https://github.com/dimanu-py/design-patterns/commit/6b0e35ca5dc30c9906199d011ed4cecc1c7f7a81)
- [Why overriding superclass method constantly is bad idea](https://github.com/dimanu-py/design-patterns/commit/a810487c154fab060b7c77032257235efc02593c)
- [Why defining interfaces and extend them is bad idea](https://github.com/dimanu-py/design-patterns/commit/5a8caa5ecf953ad1dd6bd502757ec225b939dbad)
- [Encapsulating behavior and implementing concrete strategies](https://github.com/dimanu-py/design-patterns/commit/9d8d9d96b1ab4890f8b4f83f475054d91cf42e16)
- [How the base design changes when we delegate to the strategies](https://github.com/dimanu-py/design-patterns/commit/90c383d5f500ecfb8917e3e9dbb8f96e623551dd)
- [Adding new behavior is now easy](https://github.com/dimanu-py/design-patterns/commit/2c8ff5ff3726d4cb615e325de429d536342fd56d)
- [Allowing to set behavior at runtime](https://github.com/dimanu-py/design-patterns/commit/12fa84708d649a0de3ce06a60fe2cb2db3ab058d)
- [Using the Duck Simulator](https://github.com/dimanu-py/design-patterns/commit/e7c838f48eb2945df3977347ff28ec3ba96426a8)