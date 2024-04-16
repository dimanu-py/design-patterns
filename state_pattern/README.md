# State Pattern

> The State Pattern is a behavioral pattern that allows us to change the behavior of an object when its internal state changes.

By moving this behavior and state transition from our main class to different classes we achieve the following benefits:
1. Isolate behaviors and improve the code maintainability and extensibility, following the Open/Close principle and encapsulating the behavior that changes.
2. If we model in different classes the different state actions, we follow the Separation of Concerns principle, making each concrete state care only about its action and how to go to another state.
3. Our main object reduces its complexity and by delegating the responsibility of state transition to other classes we favor composition over inheritance. 

## Class diagram & Collaborators

![State Pattern class diagram](/assets/images/state_pattern_class_diagram.png "Extracted from Head First Design Patterns book")

In the image we can see the Command Pattern is composed of two main components:
1. **Context**: the object whose state is changing. It has the methods to perform the state transitions but delegates this behavior to other classes.
2. **State**: defines what methods each concrete state will need to overwrite.

A simple example is thinking about any video game. The game can have different states: playing, paused, winner, lost, etc. Each one of these states may have different behaviors and go from one state to another.

The main idea is that the `Context` class delegates the work of acting and moving from one state to another while the client just uses a simple interface. The client doesn't need to know the internal state of our class.

## Strategy and State Patterns related

The Strategy and State patterns are said to be brothers. This is because its class diagrams and functionality are very similar. However, there are small details that make the difference between them:

| | Strategy | State |
| ---- | ----- | ----- |
| Use | An object can use different algorithms without affecting itself | An object can have different behaviors that are based on its internal state |
| Client | Tends to specify what algorithm or strategy to follow | The client doesn't know anything about the internal state |

## Code examples

The first example uploaded for this pattern is the _Gumbell Machine_. Like previous design patterns, this example allowed me to understand pretty well the concept behind the pattern.

I've implemented two versions: one for [Python](https://github.com/dimanu-py/design-patterns/tree/main/state_pattern/python/1-gumball-machine) and another one for [Java](https://github.com/dimanu-py/design-patterns/tree/main/state_pattern/java/1-gumball-machine)

To see in more detail the structure and the collaborators' implementation in each language, you can go through the files or browse the commits from the following links:

- [Initial context code](https://github.com/dimanu-py/design-patterns/commit/9c1d258a49cf02bc2f1bc57e7b2862e5c8aded5b): typical code we could find ourselves working with where adding new features gets messy.
- [State interface](https://github.com/dimanu-py/design-patterns/commit/36a2256a3d31e205c5a0f67e0fdb991673047da8) and [Concrete States](https://github.com/dimanu-py/design-patterns/commit/27aa904ad37b5b9bb267279b48efcbed96bcd204)
- [Context refactor to use states](https://github.com/dimanu-py/design-patterns/commit/53560233dea9e6026243c6328d6027e9475df13c)
- [Introducing a new feature](https://github.com/dimanu-py/design-patterns/commit/637d78dd2c56a36307507a06dd275d0d2f9ab84c)
