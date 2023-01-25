from collections import Counter
t=int(input())

for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    count = Counter(nums)
    for index,num in enumerate(nums):
        num1=count.get(num,0)
        num2=count.get(num+1,0)
        if num1 > 1:
            count[num]=num1-1
            nums[index]=-1
        elif num2!=0:
            count[num]=0
            nums[index]=-1
    nums=list(filter(lambda num: num != -1, nums))
    if len(nums) == 1:
        print("YES")
    else:
        print("NO")
