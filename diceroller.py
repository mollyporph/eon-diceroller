import re
import random
def roll_dices(dices):
    res = re.findall(r"(?:ob)?(\d{1,2})t(\d{1,3})(?:\+(\d{1,2}))?",dices)
    diceAmount = int(res[0][0])
    diceType = int(res[0][1])
    diceMod = int(res[0][2] or '0')
    if(diceType == 6 and dices.startswith("ob")):
        return roll_obthrow(diceAmount) + (diceMod,)
    return roll_normalthrow(diceAmount,diceType) + (diceMod,)

def roll_obthrow(diceAmount):
    diceType = 6
    return solve_ob(diceType,  [roll_dice(diceType) for x in range(diceAmount)])

def roll_normalthrow(diceAmount, diceType):
    return([roll_dice(diceType) for x in range(diceAmount)],0)


def solve_ob(t,dices):
    obCount = 0
    while 6 in dices:
        sixes = [i for i, x in enumerate(dices) if x == 6]
        obCount += len(sixes)
        for six in sixes:
            dices.extend([roll_dice(t),roll_dice(t)])
        dices = [i for j, i in enumerate(dices) if j not in sixes]
    return (dices,obCount)

def roll_dice(t):
    return random.randint(1,t)
