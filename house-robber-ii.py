class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}

        def chooseHouse(house,nums):
            if house==0:
                return nums[0]
            if house==1:
                return max(nums[0],nums[1])
            if house not in memo:
                memo[house]=max(chooseHouse(house-1,nums),(chooseHouse(house-2,nums)+nums[house]))
            
            return memo[house]
        
        if len(nums)<4:
            return max(nums)
        
        result1=chooseHouse(len(nums)-2,nums[:-1])
        nums.reverse()
        memo.clear()
        result2=chooseHouse(len(nums)-2,nums[:-1])
        return max(result1,result2)