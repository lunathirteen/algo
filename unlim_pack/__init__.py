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
    while W is not 0 and i < n:
        w_i = items[i][1]
        c_i = items[i][0]
        if w_i <= W:
            W -= w_i
            total_cost += c_i
        else:
            total_cost += c_i * W / w_i
        i += 1

    return total_cost


def main():

    n, W = (map(int, input().split()))
    items = []
    for i in range(n):
        item = tuple(map(int, input().split()))
        items.append(item)

    result = unlim_pack(W, items)
    print(round(result, 3))


if __name__ == "__main__":
    main()
