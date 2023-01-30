t=int(input())

for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    index=0
    sums=0
    key=nums[0]
    while index < len(nums):
        if index<len(nums)-1 and nums[index] * nums[index+1] > 0:
            key=max(key,nums[index])
            index+=1
        else:
            sums+=key
            key=nums[index]
            index+=1
            flag=0

    sums+=key
    print(sums)


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     right = 0
#     flag = 1 if nums[0] > 0 else 0
#     sums = 0
#     key = nums[0]
#     while right < len(nums):
#         if flag == 1 and nums[right] > 0:
#             key = max(key, nums[right])
#             right += 1
#         elif flag == 1 and nums[right] < 0:
#             sums += key
#             key = nums[right]
#             right += 1
#             flag = 0
#         elif flag == 0 and nums[right] < 0:
#             key = max(key, nums[right])
#             right += 1
#         elif flag == 0 and nums[right] > 0:
#             sums += key
#             key = nums[right]
#             right += 1
#             flag = 1
#     sums += key
#     print(sums)
