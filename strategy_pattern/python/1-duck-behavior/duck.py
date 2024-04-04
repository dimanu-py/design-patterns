from abc import abstractmethod, ABC

from fly import FlyBehavior, FlyWithWings, FlyNoWay
from quack import QuackBehavior, Quack, Squeak, MuteQuack


class Duck(ABC):

    def __init__(self) -> None:
        self.fly_behavior = FlyBehavior()
        self.quack_behavior = QuackBehavior()

    def quack(self) -> None:
        self.quack_behavior.quack()

    def swim(self) -> None:
        print("Swim")

    @abstractmethod
    def display(self) -> None:
        pass

    def fly(self) -> None:
        self.fly_behavior.fly()


class MallardDuck(Duck):

    def __init__(self) -> None:
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print("I'm a Mallard Duck")


class RedheadDuck(Duck):

    def __init__(self) -> None:
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print("I'm a Redhead Duck")


class RubberDuck(Duck):

    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self) -> None:
        print("I'm a Rubber Duck")


class DecoyDuck(Duck):

    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self) -> None:
        print("I'm a Decoy Duck")
