from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex0.creature_types import Pyrodon, Flameling, Torragon, Aquabub
from ex1.capability_fact import Bloomelle, Sproutling, Shiftling, Morphagon
from ex1.capability_fact import HealCapability, TransformCapability
from typing import cast


class BattleStrategy(ABC):
    def __init__(self):
        self.s_name: str
        """self.cr_name: str"""

    @abstractmethod
    def act(self, cr: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self):
        self.s_name = "Normal"

    def act(self, cr: Creature) -> None:
        if (self.is_valid(cr)):
            print(cr.attack())
        else:
            pass

    def is_valid(self, creature: Creature) -> bool:
        if (isinstance(creature, (Pyrodon, Flameling, Torragon, Aquabub))):
            return True
        else:
            return False


class AggressiveStrategy(BattleStrategy):
    def __init__(self):
        self.s_name = "Agressive"

    def act(self, cr: Creature) -> None:
        if (self.is_valid(cr)):
            print(cast(TransformCapability, cr).transform())
            print(cr.attack())
            print(cast(TransformCapability, cr).revert())
        else:
            msg = "Battle error, aborting tournament: Invalid Creature"
            msg += "\'{}\' ".format(cr.name)
            msg += "for this {} strategy".format(self.s_name.lower())
            raise Exception(msg)

    def is_valid(self, creature: Creature) -> bool:
        if (isinstance(creature, (Shiftling, Morphagon))):
            return True
        else:
            return False


class DefensiveStrategy(BattleStrategy):
    def __init__(self):
        self.s_name = "Defensive"

    def act(self, cr: Creature) -> None:
        if (self.is_valid(cr)):
            print(cr.attack())
            print(cast(HealCapability, cr).heal())
        else:
            msg = "Battle error, aborting tournament: Invalid Creature"
            msg += "\'{}\' ".format(cr.name)
            msg += "for this {} strategy".format(self.s_name.lower())
            raise Exception(msg)

    def is_valid(self, creature: Creature) -> bool:
        if (isinstance(creature, (Bloomelle, Sproutling))):
            return True
        else:
            return False
