class Solution:
    def findBigger(self, num1, num2):
        return str(num1) + str(num2) > str(num2) + str(num1)
    
    
    def largestNumber(self, nums):
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if not self.findBigger(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    
        return str(int("".join(map(str, nums))))


        