"""
Даны целые числа 1≤n≤10^18 и 2≤m≤10^5,
необходимо найти остаток от деления n-го числа Фибоначчи на m
"""


def fib_mod(n, m):
    estimates = [0, 1]

    a, b = 0, 1
    for i in range(2, 6*m + 1):
        a, b = b, (a + b) % m
        estimates.append(b)
        if estimates[len(estimates) - 1] == 1\
                and estimates[len(estimates) - 2] == 0:

            break

    return estimates[:-2][n % len(estimates[:-2])]
