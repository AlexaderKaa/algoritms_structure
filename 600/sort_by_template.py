def sort_containers():
    # Чтение входных данных
    n = int(input().strip())
    containers = list(map(int, input().strip().split()))
    m = int(input().strip())
    template = list(map(int, input().strip().split()))

    # Словарь для подсчета контейнеров
    count = {}
    for container in containers:
        if container in count:
            count[container] += 1
        else:
            count[container] = 1

    result = []

    # Сортировка по шаблону
    for number in template:
        if number in count:
            result.extend([number] * count[number])
            del count[number]  # Удаляем, чтобы не добавлять повторно

    # Добавление оставшихся контейнеров
    remaining_containers = []
    for number, cnt in count.items():
        remaining_containers.extend([number] * cnt)
    
    # Сортировка оставшихся контейнеров
    remaining_containers.sort()
    
    # Объединение результатов
    result.extend(remaining_containers)

    # Вывод результата
    print(" ".join(map(str, result)))

# Вызов функции
sort_containers()