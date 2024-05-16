from abc import ABC, abstractmethod


class Dough(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


class ThinCrustDough(Dough):

    def __str__(self) -> str:
        return "Thin Crust Dough"


class ThickCrustDough(Dough):

    def __str__(self) -> str:
        return "Thick Crust Dough"
