# Command Pattern

> [!IMPORTANT]
> The Command Pattern is a behavioral pattern that allows us to encapsulate an action or a request inside a separate object.

By extracting the request into a single object we achieve the following benefits:
1. Decouple the object that is making the request, from the object that is capable of performing that request. We favor composition to manage collaboration between classes
2. Make each class responsible for its actions, following the Separation of Concerns principle.
3. We program to an interface rather to concrete implementations, favouring the use of polymorphism.

## Class diagram & Collaborators

![Command Pattern class diagram](/assets/images/command_pattern_class_diagram.png "Extracted from Head First Design Patterns book")

In the image we can see the Command Pattern is composed of three main collaborators:

1. **Receiver**: the object that knows how to act. It has the method that will be called to do that action.
2. **Invoker**: the object that stores what command is going to be executed. This object only knows that it has a command, it doesn't care how it performs the action.
3. **Command**: it's defined as an interface that every concrete command must implement. This object needs to have a receiver that knows how to act.

To understand these three elements and gain a deeper understanding of the pattern we are going to think of a dinner. How it works?

1. A person enters the diner -> This is the client
2. A waitress or waiter takes the order of the client -> The waitress is the invoker
3. The order will have the info of what the client wants to eat -> The order is the command
4. The waitress gives the order to the chef who cooks the food -> The chef is the receiver

So we can see here how the objects work and communicate: 
- The invoker only needs to know what command is needed. It doesn't matter which command is it as far as it has its `execute` method
- The command only needs to know which receiver knows what to do. It doesn't care about who is the invoker.
- The receiver only gets orders to do what it knows. It doesn't need to know what other commands are doing or who is the invoker that wants that command.

## Additional features of the Command Pattern

One of the advantages of the Command Pattern is that allows us to implement an undo operation, so we can roll back the command we've executed.

If our client wants to execute a bunch of commands altogether we can create a _Meta Command_. This would be a new type of command that stores a group of commands,
so we can execute them directly only by calling our _Meta Command_.

## Command vs Strategy Pattern

As we've seen in other states patterns, the Command pattern and Strategy have a very similar class diagram, making confusing when to use each.

> [!IMPORTANT]
> The difference between the patterns is in the intention and the behavior of the objects

The Command pattern turns requests to do actions into objects, decoupling the object that invokes the operation from the one that knows how to perform it.

The Strategy pattern is intended to choose different ways of performing an action within a single interface context. This pattern decouples 
the implementation of the algorithm from the code that uses it.

## Code examples

The first example I've uploaded is the _Remote Controller_. This is because it was an example where I could understand and visualize easily this pattern. Feel free
to visit any other example you find more useful.

For the _Remote Controller_ example I've made two versions, one for [Python](https://github.com/dimanu-py/design-patterns/tree/main/command_pattern/python/1-remote-controller) and the other
for [Java](https://github.com/dimanu-py/design-patterns/tree/main/command_pattern/java/1-remote-controller)

To see in more detail how all the collaborators are implemented in each language you can go through the files or browse the commits directly from the following links:

- [Receiver explanation](https://github.com/dimanu-py/design-patterns/commit/c58273449ce83c87d40e52681f2edc712d9b50f9)
- [Command explanation](https://github.com/dimanu-py/design-patterns/commit/4f1455ccd580f4e21a57ed0ef0361443efe88ccb)
- [Invoker explanation](https://github.com/dimanu-py/design-patterns/commit/14a831d0330eae4aae7efcf047e5783799f0561d)
- [Undo operation for commands](https://github.com/dimanu-py/design-patterns/commit/de57831d6e8e6cc8c3a6941f3ef047710ce1675c)
- [How invoker uses undo](https://github.com/dimanu-py/design-patterns/commit/6e21548813a867c7000b4668ae85ebd02da62248)
- [How to implement macro-command](https://github.com/dimanu-py/design-patterns/commit/21bd3bdc872030be234ff562650d6f9e4fb08e46)
- [Add undo operation to macro-command](https://github.com/dimanu-py/design-patterns/commit/aa19cd634c149d5a0f8e060a0bfb985951d69480)
