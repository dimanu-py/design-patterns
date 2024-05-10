# Factory Pattern

> [!IMPORTANT]


## Notes

- Instatiation is an activity that shouldn't always be done in public and can often lead to coupling problems
- When we try to code to an interface we seem to be always needing to create a concrete class
    Duck duck = new MallardDuck();
   Here we want to use the interface Duck, but we need to create the concrete Duck, so we end up with a concrete class in our code
- When we have a bunch of concrete classes and need to decide at runtime which one to instantiate, it is very easy to end up with a lot of if-else statements