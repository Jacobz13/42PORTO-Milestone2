from .capabilities import TransformCapability, HealCapability
from ex0.creature import Creature
from ex0.factory import CreatureFactory


class Sproutling(HealCapability, Creature):
    def __init__(self):
        self.name: str = "Sproutling"
        self.type: str = "Grass"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(HealCapability, Creature):
    def __init__(self):
        self.name: str = "Blomelle"
        self.type: str = "Grass/Fairy"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(TransformCapability, Creature):
    def __init__(self):
        self.name: str = "Shiftling"
        self.type: str = "Normal"
        self.state: int = 0

    def attack(self) -> str:
        if (self.state == 0):
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        self.state = 1
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.state = 0
        return "Shiftling returns to normal."


class Morphagon(TransformCapability, Creature):
    def __init__(self):
        self.name: str = "Morphagon"
        self.type: str = "Normal/Dragon"
        self.state: int = 0

    def attack(self) -> str:
        if (self.state == 0):
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.state = 1
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.state = 0
        return "Morphagon stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
