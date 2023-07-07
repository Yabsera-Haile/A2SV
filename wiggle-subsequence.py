class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        if n< 2:
            return n

        result = 1
        flag = None
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and flag != 1) or (diff < 0 and flag != -1):
                result += 1
                flag = 1 if diff > 0 else -1
                
        return result