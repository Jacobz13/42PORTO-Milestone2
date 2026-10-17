from ex0 import CreatureFactory, FlameFactory, AquaFactory


def factory(creture: CreatureFactory) -> None:
    base = creture.create_base()
    evolved = creture.create_evolved()
    print("Testing factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print("")


def battle(cr1: CreatureFactory, cr2: CreatureFactory) -> None:
    print("Testing battle")
    creature1 = cr1.create_base()
    creature2 = cr2.create_base()
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


flame = FlameFactory()
aqua = AquaFactory()
factory(flame)
factory(aqua)
battle(aqua, flame)
