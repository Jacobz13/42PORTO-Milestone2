from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy


def s_error(ops: list[tuple[CreatureFactory, BattleStrategy]]) -> bool:
    for op in ops:
        temp = op[0].create_base()
        if not op[1].is_valid(temp):
            return False
    return True


def aux_type(ops: list[tuple[CreatureFactory, BattleStrategy]]):
    res: str = "[ "
    for i in range(len(ops)):
        if (isinstance(ops[i][0], HealingCreatureFactory)):
            res += f"(Healing+{ops[i][1].s_name}), "
        elif (isinstance(ops[i][0], TransformCreatureFactory)):
            res += f"(Transform+{ops[i][1].s_name}), "
        else:
            res += f"({ops[i][0].create_base().name}+{ops[i][1].s_name}), "
            pass
        pass
    mask = list(res)
    while (mask[-1] in [" ", ","]):
        mask.pop()
    res = ""
    for ii in mask:
        res += ii
    res += " ]"
    print(res)


def s_battle(oponents: list[tuple[CreatureFactory, BattleStrategy]]):
    aux_type(oponents)
    print("*** Tournament ***")
    print(f"{len(oponents)} opponents involved\n\n* Battle *")
    for i in range(0, len(oponents)):
        for j in range(i, len(oponents)):
            if (oponents[i] != oponents[j]):
                op1 = oponents[i][0].create_base()
                op2 = oponents[j][0].create_base()
                print(f"{op1.describe()}\nvs\n{op2.describe()}\n now fight!")
                try:
                    oponents[i][1].act(op1)
                    oponents[j][1].act(op2)
                except Exception as e:
                    print(e)


flame = FlameFactory()
aqua = AquaFactory()
heal = HealingCreatureFactory()
trans = TransformCreatureFactory()
agr = AggressiveStrategy()
defe = DefensiveStrategy()
norm = NormalStrategy()
oponents1 = [(flame, norm), (heal, defe)]
oponents2 = [(flame, agr), (heal, defe)]
oponents3 = [(aqua, norm), (heal, defe), (trans, agr)]
ops = [oponents1, oponents2, oponents3]
i = 0

for op in [oponents1, oponents2, oponents3]:
    aux: str
    if (len(op) == 2 and s_error(op)):
        aux = "(Basic)"
    elif (len(op) > 2 and s_error(op)):
        aux = "(Multiple)"
    else:
        aux = "(error)"
    s_error(op)
    print(f"Tournament {i}", aux)
    s_battle(op)
    print("")
    i = i + 1
