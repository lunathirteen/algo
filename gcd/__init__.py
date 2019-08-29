"""
Задача на программирование: наибольший общий делитель


По данным двум числам 1≤a,b≤2⋅10^9
найдите их наибольший общий делитель.
"""


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        a = a % b
        return gcd(a, b)
    elif b >= a:
        b = b % a
        return gcd(a, b)
