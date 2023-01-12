class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result=[]
        for index in range(len(nums)):
            result.append(nums[nums[index]])
        return result
        