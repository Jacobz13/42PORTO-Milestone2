from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self):
        self.name: str
        self.type: str

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        msg = self.name + " is a " + self.type + " type Creature"
        return msg
