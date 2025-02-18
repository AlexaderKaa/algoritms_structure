def rem_duplicates(nums, arr):
    arr = tuple(arr.split())
    res = []
    res1 = []
    res2 = []
    for i in arr:
        if i not in res1:
            res1.append(i)
        elif i in res1:
            i = i.replace(i, '_')
            res2.append(i)
    res = ' '.join(res1) + ' ' + ' '.join(res2)
    return res


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        nums = int(file_in.readline())
        arr = file_in.readline()
        result = rem_duplicates(nums, arr)
    print(result)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(result))
