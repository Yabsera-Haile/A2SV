class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sums=0
        right=0
        left=0
        result=len(nums)+1
        
        while right<len(nums):
            sums+=nums[right]
            # print(left,right)
            # print(sums)
            if sums<target:
                right+=1
            else:
                result=min(right-left+1,result)
                sums-=nums[left]
                sums-=nums[right]
                left+=1
        if result==len(nums)+1:
            result=0
        return result