example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


print(bubble_sort(example_array))
