class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)   
        @cache
        def findAlternatives(index, even) -> int: 
            if index>=n:
                return 0 
            
            curr = nums[index] if even else -nums[index]
            take = curr + findAlternatives(index+1, not even)

            skip = findAlternatives(index+1, even)
            return max(take, skip)

        return findAlternatives(0, True)