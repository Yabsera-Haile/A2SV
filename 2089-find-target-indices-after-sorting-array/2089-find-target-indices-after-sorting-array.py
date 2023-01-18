class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result=[index for index,num in enumerate(nums) if num==target]
        return result
        