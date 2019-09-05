"""
Различные слагаемые

По данному числу 1≤n≤10^9 найдите максимальное число k,
для которого n можно представить как сумму k различных натуральных слагаемых.

Выведите в первой строке число k, во второй — k слагаемых.
"""


def addends(n):
    array = []
    i = 1
    while n - i >= 0:
        n -= i
        array.append(i)
        i += 1
    if n % array[-1] >= 0:
        array[-1] += n

    return array


def main():

    n = int(input())

    result = addends(n)
    print(result)


if __name__ == "__main__":
    main()
