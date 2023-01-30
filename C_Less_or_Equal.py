[n,k]=list(map(int,input().split()))
nums = list(map(int, input().split()))
nums.sort()
num = nums[k-1]

if k==0 and nums[0]>1:
    print(nums[0]-1)       
elif num not in nums[k:] and num >= 1 and num <= 10**9 and k>0:
    print(nums[k-1])
else:
    print(-1)
