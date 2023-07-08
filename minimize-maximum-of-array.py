class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result=0
        _sum=0

        for i in range(len(nums)):
            _sum+=nums[i]
            avg=math.ceil(_sum/(i+1))
            result=max(result,avg)
        
        return result