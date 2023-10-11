class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        result=0
        total=_sum=nums[0]
        for i in range(n):
            total=total & nums[i]

        for i in range(n):
            _sum=_sum&nums[i]
            if _sum==total:
                result+=1
                if i<n-1:
                    _sum=nums[i+1]
        if result * total > total:
            return 1
        return result