from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):
    def __init__(self):
        self.state: int

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass
    pass
