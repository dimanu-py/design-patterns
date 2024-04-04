from abc import ABC, abstractmethod


class QuackBehavior(ABC):

    @abstractmethod
    def quack(self) -> None:
        pass


class Quack(QuackBehavior):

    def quack(self) -> None:
        print("Quack")


class Squeak(QuackBehavior):

    def quack(self) -> None:
        print("Squeak")


class MuteQuack(QuackBehavior):

    def quack(self) -> None:
        print("<< Silence >>")