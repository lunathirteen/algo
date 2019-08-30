"""
Покрыть отрезки точками


По данным n отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков.
Каждая из последующих n строк содержит по два числа 0≤l≤r≤109,
задающих начало и конец отрезка.

Выведите оптимальное число m точек и сами m точек.
Если таких множеств точек несколько, выведите любое из них.
"""


def coverpoint(segments):
    segments.sort(key=lambda s: s[1])

    return segments


def main():

    n = int(input())
    segments = []
    for i in range(n):
        segment = tuple(map(int, input().split()))
        segments.append(segment)

    print(coverpoint(segments))


if __name__ == "__main__":
    main()
