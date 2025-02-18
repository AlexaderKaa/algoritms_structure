def calculate_average(data):
    # Сохраняем длину массива в переменную, чтобы дважды не считать.
    len_data = len(data)
    # Формула суммы арифметической прогрессии.
    data_sum = (data[0] + data[-1]) * len_data / 2
    # Делим сумму на количество элементов.
    average = data_sum / len_data
    return average


print(calculate_average([1, 2, 3, 4, 5])) 