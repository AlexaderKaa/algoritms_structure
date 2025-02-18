"""Находит индекс element в отсортированном списке sorted_numbers."""


def find_element_index(sorted_numbers, element):
    arr = sorted_numbers.split()
    # Левая граница (левый индекс) рассматриваемого набора элементов. 
    # В начале работы она равна индексу первого элемента в списке - нулю.
    left = 0
    # Правая граница (правый индекс) рассматриваемого набора элементов. 
    # В начале работы она равна индексу последнего элемента в списке.
    right = len(arr) - 1
    # Пока левая граница меньше правой или равна ей:
    while left <= right:
        # Находим в наборе элементов индекс среднего элемента.
        mid = (left + right) // 2
        # Если элемент с этим индексом равен искомому, возвращаем его индекс.
        #if int(arr[mid]) == element:
        if arr[mid] == element:
            return mid
        # Если средний элемент меньше искомого...
        if int(arr[mid]) < element:
            # ...то изменяем левую границу поиска:
            left = mid + 1
            result = left
        # Если средний элемент больше искомого...
        else:
            # ...то изменяем правую границу поиска:
            right = mid - 1
            result = right + 1
    # Если левая граница оказалась больше правой, 
    # значит, элемент не найден. Возвращаем result.
    return result


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        sorted_numbers = file_in.readline()
        desired_element = int(file_in.readline())
        res = find_element_index(sorted_numbers, desired_element)
    print(res)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(res))
