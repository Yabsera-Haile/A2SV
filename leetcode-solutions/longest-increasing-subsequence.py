class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        @cache
        def findSubsequence(index):
            result=1
            for i in range(index+1,n):
                if nums[i]>nums[index]:
                    result=max(result,findSubsequence(i)+1)
            return result
        
        result=0
        for i in range(n):
            result=max(result,findSubsequence(i))
        
        return result
            
        