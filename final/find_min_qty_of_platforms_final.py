""" ID Yandex Contest = 116943291
    Googel doc link = https://docs.google.com/document/d/1q41WsnzYpYfn1EgRjLdmcEkG6POdrXIe5-gF7FqWEoQ/edit?usp=sharing
"""

from typing import List


def find_min_qty_of_platforms(weights: List[int], limit: int) -> int:
    # Сортировка.
    weights.sort()

    i, j = 0, len(weights) - 1
    platforms = 0

    while i <= j:
        # Проверка на ограничение по весу для платформы.
        if weights[i] + weights[j] <= limit:
            i += 1
        j -= 1
        platforms += 1

    return platforms


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        # Обработка входных данных.
        weights_input = list(map(int, file_in.readline().split()))
        limit_input = int(file_in.readline())
        RES = find_min_qty_of_platforms(weights_input, limit_input)
    print(RES)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(RES))
