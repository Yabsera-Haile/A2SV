[n, k] = list(map(int, input().split()))
nums = list(map(int, input().split()))


def solution(index, count):
    if count == 1:
        return [index]

    left_arr = solution(index, count//2)
    right_arr = solution(index+count//2, count//2)

    left_min = nums[left_arr[0]]
    right_min = nums[right_arr[0]]
    i = j = 0
    result = []
    # print(left_arr,right_arr)
    while i < len(left_arr) and j < len(right_arr):
        if nums[left_arr[i]] <= nums[right_arr[j]]:
            if right_min-nums[left_arr[i]] <= k:
                result.append(left_arr[i])
            i += 1
        else:
            if left_min-nums[right_arr[j]] <= k:
                result.append(right_arr[j])
            j += 1
    while i < len(left_arr) and right_min-nums[left_arr[i]] <= k:
        result.append(left_arr[i])
        i += 1
    while j < len(right_arr) and left_min-nums[right_arr[j]] <= k:
        result.append(right_arr[j])
        j += 1

    return result


print(*sorted(map(lambda x: x + 1, solution(0, 2**n))))