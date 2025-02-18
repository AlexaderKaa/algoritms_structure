"""Функции is_correct_bracket_seq(), которая принимает на вход скобочную
последовательность и возвращает True, если последовательность правильная,
и False — в остальных случаях."""


def is_correct_bracket_seq(bracket_seq):
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in bracket_seq:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map.keys():
            if not stack or stack[-1] != brackets_map[char]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        bracket_sequence = file_in.readline()
        res = is_correct_bracket_seq(bracket_sequence)
    print(res)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(res))
