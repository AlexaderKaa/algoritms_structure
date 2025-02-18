"""На Марс заброшена партия стационарных роботов-исследователей.
Марсоход должен перевезти их на определённые точки планеты.
Для перевозки роботов есть неограниченное количество транспортных платформ,
каждая из которых способна выдерживать определённый вес limit.
На одной платформе можно перевезти либо одного робота, либо двух — при условии,
что их совокупный вес не превышает limit. Роботы имеют разный вес.
Программа должна получить на вход массив, каждый элемент которого — вес робота.
Второй параметр, который должна принять программа, — это значение limit,
грузоподъёмность одной платформы.
Определите минимальное количество транспортных платформ, необходимое
для перевозки всех роботов, описанных в массиве.
Количество платформ неограниченно.
Каждая платформа выдерживает максимальный вес limit.
На каждой платформе можно перевезти не более двух роботов при условии,
что их совокупный вес не превышает limit.
Вес отдельного робота не может превышать limit.

Формат ввода
В первой строке записан массив целых чисел через пробел — вес каждого робота.
Во второй строке записан лимит — предельная грузоподъёмность платформы.
Формат вывода
Целое число, указывающее на нужное количество платформ для транспортировки."""

from typing import List


def find_min_qty_of_platforms(weights: List[int], limit: int) -> int:
    # Сортировка
    weights.sort()

    i, j = 0, len(weights) - 1
    platforms = 0

    while i <= j:
        # Проверка на ограничение по весу для платформы
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
