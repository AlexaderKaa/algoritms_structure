from array import array


def valid_mountain_array(arr):
    arr = list(map(int, arr.split()))
    arr = map(int, list(arr))
    arr = array('B', arr)
    up = down = 0
    if not arr or len(arr) == 1:
        return False
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
        peaks = file_in.readline()
        res = valid_mountain_array(peaks)
    print(res)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(res))
