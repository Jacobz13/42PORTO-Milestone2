from abc import ABC, abstractmethod
from . import creature_types as ct


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> ct.Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> ct.Creature:
        pass


class AquaFactory(CreatureFactory):
    def create_base(self) -> ct.Aquabub:
        return ct.Aquabub()

    def create_evolved(self) -> ct.Torragon:
        return ct.Torragon()


class FlameFactory(CreatureFactory):
    def create_base(self) -> ct.Creature:
        return ct.Flameling()

    def create_evolved(self) -> ct.Creature:
        return ct.Pyrodon()
