class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left=0
        right=1
        while right<len(nums):
            if nums[right]!=0 and nums[left]==0:
                nums[right],nums[left]=nums[left],nums[right]
                left+=1
                right+=1
            elif nums[right]==0 and nums[left]==0:
                right+=1        
            else:
                right+=1
                left+=1

        return nums
        
        # no_zeroes=0
        # size=0
        # for i in range(len(nums)):
        #     if nums[i-size]==0:
        #         no_zeroes+=1
        #         nums.pop(i-size)
        #         size+=1
        # nums.extend([0]*no_zeroes)
        