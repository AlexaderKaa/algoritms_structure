"""Напишите программу, которая принимает на вход строку и находит в ней
наибольшую длину подстроки,в которой нет повторяющихся символов.
Программа должна вернуть натуральное число — длину этой подстроки.
Используйте метод скользящего окна для решения задачи. Если в строке
встретится дубликат, запомните длину получившейся подстроки
и начинайте строить окно заново."""


def search_substring_length(text: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0
    for end in range(len(text)):
        if text[end] in char_index_map:
            start = max(start, char_index_map[text[end]] + 1)

        char_index_map[text[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        text = file_in.readline()
        res = search_substring_length(text)
    print(res)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(res))
