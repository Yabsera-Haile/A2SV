class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums=list(set(nums))
        nums.sort()

        result= n 
        curr=0
        for i in range(len(nums)):
            while curr < len(nums) and nums[curr] - nums[i] <= n-1:
                curr+=1
            result= min(result,n-(curr - i))

        return result