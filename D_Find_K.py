t = int(input())

for _ in range(t):
    [n, k] = list(map(int, input().split()))
    nums = list(set(map(int, input().split())))
    
    nums.sort()
    left = 0
    right = len(nums)-1
    found = False
    while left < right :
        if nums[right]-nums[left] == k:
            print("YES")
            found = True
            break
        elif nums[right]-nums[left] > k:
            right -= 1
        else:
            left += 1
    if not found:
        print("NO")
