from abc import abstractmethod


class Duck:

    def quack(self) -> None:
        print("Quack")

    def swim(self) -> None:
        print("Swim")

    @abstractmethod
    def display(self) -> None:
        pass


class MallardDuck(Duck):

    def display(self) -> None:
        print("I'm a Mallard Duck")


class RedheadDuck(Duck):

    def display(self) -> None:
        print("I'm a Redhead Duck")
