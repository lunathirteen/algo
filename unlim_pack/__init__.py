"""
Первая строка содержит количество предметов 1≤n≤10^3 и
вместимость рюкзака 0≤W≤2⋅10^6.

Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅10^6
и объём 0<wi≤2⋅10^6 предмета (n, W, ci, wi — целые числа).

Выведите максимальную стоимость частей предметов (от каждого предмета
можно отделить любую часть, стоимость и объём при этом
пропорционально уменьшатся), помещающихся в данный рюкзак,
с точностью не менее трёх знаков после запятой.

"""
from typing import List


def unlim_pack(W: int, items: List[int]) -> float:
    items.sort(key=lambda i: i[0]/i[1], reverse=True)
    i = 0
    n = len(items)
    total_cost = 0.0
    while W is not 0 and i <= n:
        total_cost += items[i][0]
        W -= items[i][1]

    return items


def main():

    n, W = (map(int, input().split()))
    items = []
    for i in range(n):
        item = tuple(map(int, input().split()))
        items.append(item)

    result = unlim_pack(W, items)
    print(result)


if __name__ == "__main__":
    main()
