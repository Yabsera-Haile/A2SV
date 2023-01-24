class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        s_nums=sorted(nums)
        for i in range(0,len(s_nums)):
            result.append(s_nums.index(nums[i]))
        return result
            
            
            
        