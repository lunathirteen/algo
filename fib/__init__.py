"""
Дано целое число 1 ≤ n ≤ 40,
необходимо вычислить n-е число Фибоначчи
(напомним, что F0=0, F1=1 и Fn=Fn−1+Fn−2 при n≥2)
"""


def fib(n):
    fib_list = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n]
