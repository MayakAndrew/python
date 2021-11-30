"""Блок расчета заработной платы при заданной тарифной ставке и заданной величине премии"""
from inpt import inp
c = inp()
def payment(bid = int(15)):
    if c >= 160:
        bonus = 10000
    else:
        print('Премия не начисляется')
        bonus = 0
    res = c * bid + bonus
    return res





