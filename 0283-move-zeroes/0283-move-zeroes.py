class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        no_zeroes=0
        size=0
        for i in range(len(nums)):
            if nums[i-size]==0:
                no_zeroes+=1
                nums.pop(i-size)
                size+=1
        nums.extend([0]*no_zeroes)
        