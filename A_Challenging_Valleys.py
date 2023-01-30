t=int(input())

for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    up=0
    count=0
    for index in range(len(nums)-1):
        if nums[index]>nums[index+1]:
            up+=1
        if nums[index]<nums[index+1]:
            if up!=0:
                count+=1
                up=0
    if up==0 and count<=1:
        print("YES")
    else:
        print("NO")
            