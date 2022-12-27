class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=sum(range(len(nums)+1))
        current=sum(nums)
        return total-current
        