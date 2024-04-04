from abc import abstractmethod, ABC


class Flyable(ABC):

    @abstractmethod
    def fly(self) -> None:
        pass


class Quackable(ABC):

    @abstractmethod
    def quack(self) -> None:
        pass


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


class MallardDuck(Duck, Flyable, Quackable):

    def display(self) -> None:
        print("I'm a Mallard Duck")

    def fly(self) -> None:
        print("I'm flying")

    def quack(self) -> None:
        print("Quack")


class RedheadDuck(Duck, Flyable, Quackable):

    def display(self) -> None:
        print("I'm a Redhead Duck")

    def fly(self) -> None:
        print("I'm flying")

    def quack(self) -> None:
        print("Quack")


class RubberDuck(Duck, Quackable):

    def quack(self) -> None:
        print("Squeak")

    def display(self) -> None:
        print("I'm a Rubber Duck")


class DecoyDuck(Duck):

    def display(self) -> None:
        print("I'm a Decoy Duck")
