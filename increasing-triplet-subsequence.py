class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        lower={}
        upper={}
        _min=nums[0]
        for i,num in enumerate(nums):
            _min=min(_min,num)
            lower[i]=_min

        _max=nums[-1]
        for i in range(len(nums)-1,-1,-1):
            _max=max(_max,nums[i])
            upper[i]=_max

        for i,num in enumerate(nums):
            if lower[i]!=num and upper[i]!=num:
                return True
        
        return False