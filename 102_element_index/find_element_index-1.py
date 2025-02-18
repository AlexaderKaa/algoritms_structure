def find_element_index(arr, desired_element):
    arr = arr.split()
    r_index = None
    print(arr)
    for i, item in enumerate(arr):
        if int(item) == desired_element:
            r_index = i
            #break
        elif int(item) < desired_element:
            r_index = i
            result = (f"'{desired_element}' aka {r_index - 1}")
            #break
        """elif int(item) > desired_element:
            r_index = i
            result = (f"'{desired_element}' kak {r_index + 1}")
            #break"""
        result = r_index
    return result


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        arr = file_in.readline()
        desired_element = int(file_in.readline())
        res = find_element_index(arr, desired_element)
    print(res)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(res))
