wins = [1, 3, 5, 6]
my_ticket = 10

def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    # Левая граница (левый индекс) рассматриваемого набора элементов. 
    # В начале работы она равна индексу первого элемента в списке - нулю.
    left = 0
    # Правая граница (правый индекс) рассматриваемого набора элементов. 
    # В начале работы она равна индексу последнего элемента в списке.
    right = len(sorted_numbers) - 1
    # Пока левая граница меньше правой или равна ей:
    while left <= right:
        # Находим в наборе элементов индекс среднего элемента.
        mid = (left + right) // 2
        # Если элемент с этим индексом равен искомому, возвращаем его индекс.
        if sorted_numbers[mid] == element:
            return mid
        # Если средний элемент меньше искомого...
        if sorted_numbers[mid] < element:
            # ...то изменяем левую границу поиска:
            left = mid + 1
            result = left
        # Если средний элемент больше искомого...
        else:
            # ...то изменяем правую границу поиска:
            right = mid - 1
            result = right+1
    # Если левая граница оказалась больше правой, 
    # значит, элемент не найден. Возвращаем None.
    return result


print(find_element(wins, my_ticket))

# Проверим, что ваш код успешно находит все значения,
# которые есть в списке wins: в качестве искомого элемента
# поочерёдно передадим в функцию все значения из списка.
#for item in wins:
#    print(find_element(wins, item))