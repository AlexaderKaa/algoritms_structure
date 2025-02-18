Есть и ещё один вариант:
результаты сложения, полученные на каждой итерации, добавлять в массив output_numbers;
напечатать распакованный массив, разделив элементы символами перевода строки.
Чтобы распаковать список на отдельные элементы, перед именем списка указывается звёздочка:

Этот способ будет работать только с print(), тогда как вариант с методом join() более универсален: его можно использовать не только при печати, но и при выводе данных в файл.

import sys


def main():
    num_lines = int(sys.stdin.readline().rstrip())  
    output_numbers = [None] * num_lines
    for i in range(num_lines):
        line = sys.stdin.readline().rstrip()
        first, second = line.split()  
        first = int(first)  
        second = int(second)
        # Записываем результат в массив без преобразования в строку.
        output_numbers[i] = first + second
    # В конце печатаем распакованный список, 
    # добавляя между значениями символы перевода строки.
    print(*output_numbers, sep='\n')
    

if __name__ == '__main__':
    main()