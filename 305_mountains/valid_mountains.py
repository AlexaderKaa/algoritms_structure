from array import array


def valid_mountain_array(arr):
    arr = arr.split()
    arr = array('u', arr)
    if not arr or len(arr) == 1:
        return False
    up = down = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i + 1]:
            if down:
                return False
            up += 1
        elif arr[i] > arr[i + 1]:
            if not up:
                return False
            down += 1
        else:
            return False
    return bool(up and down)


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        map = file_in.readline()
        res = valid_mountain_array(map)
    print(res)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(res))
