class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums=deque(sorted(nums))
        if len(nums)<=4:
            return 0
        
        pairs=[(0,-4),(1,-3),(2,-2),(3,-1)]
        result=[nums[j]-nums[i] for i,j in pairs]

        return min(result)