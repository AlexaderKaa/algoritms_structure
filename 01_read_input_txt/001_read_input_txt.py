""" Sum of 2 """

def main(b, c):
    return b + c


if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    # Открываем для чтения (второй аргумент 'r' - "read")
    # файл input.txt в текущей директории.
    # Для работы с файлом применяем контекстный менеджер with:
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        # Читаем все строки файла:
        # значением переменной lines будет список,
        # каждый элемент которого - строка из файла.
        #lines = file_in.readlines()
        a = int(file_in.readline())
        b = int(file_in.readline())
        c = int(file_in.readline())
    result = main(b, c)
    print(result)
    # Внутри переменной lines будет находиться список со строками.
    # ['3\n', '1 2 3\n', '4 5 6']
    # \n - это символ перевода строки. 
    #main()
    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(result))