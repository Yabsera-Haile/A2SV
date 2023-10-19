class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        goal=sum(nums)
        if goal%2!=0:
            return False

        @cache
        def findPartition(index,goal):
            if goal==0:
                return True
            if index==n-1:
                return goal == nums[index]

            return findPartition(index+1,goal) or findPartition(index+1,goal-nums[index])
        
        return findPartition(0,goal//2)