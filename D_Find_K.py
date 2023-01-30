t = int(input())

for _ in range(t):
    [n, k] = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    diff = 0
    index = 0
    for _ in range(n-1):
        diff += (nums[index]-diff)
        index += 1
    if abs(nums[index]-diff) == k:
        print("YES")
    else:
        print("NO")
