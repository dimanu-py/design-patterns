from abc import abstractmethod


class Duck:

    def quack(self) -> None:
        print("Quack")

    def swim(self) -> None:
        print("Swim")

    @abstractmethod
    def display(self) -> None:
        pass

    def fly(self) -> None:
        print("I'm flying")


class MallardDuck(Duck):

    def display(self) -> None:
        print("I'm a Mallard Duck")


class RedheadDuck(Duck):

    def display(self) -> None:
        print("I'm a Redhead Duck")


class RubberDuck(Duck):

    def quack(self) -> None:
        print("Squeak")

    def display(self) -> None:
        print("I'm a Rubber Duck")