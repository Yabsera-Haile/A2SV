class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}

        def findWays(_sum,index):
            state=(_sum,index)
            if index==len(nums):
                if _sum==target:
                    return 1
                else:
                    return 0
            if state not in memo:
                memo[state] = findWays(_sum+nums[index],index+1) + findWays(_sum-nums[index],index+1)
            
            return memo[state]
        
        return findWays(0,0)