from array import array


def count_smaller_elements(nums):
    nums = list(map(int, nums.split()))
    nums = array('B', nums)
    result = array('B')
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)
    return (" ".join(map(str, result)))


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        nums = file_in.readline()
        res = count_smaller_elements(nums)
    print(res)

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(str(res))
