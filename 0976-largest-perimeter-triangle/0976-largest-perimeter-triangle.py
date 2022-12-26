class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #Sort nums
        nums.sort()
        
        #initialize three pointers
        side1=len(nums)-1
        side2=side1-1
        side3=side2-1
        
        #
        while side3>=0:
            if nums[side3]+nums[side2] > nums[side1]:
                
                return sum(nums[side3:side1+1])
            else:
                side3-=1
                side2-=1
                side1-=1
                
        return 0

                