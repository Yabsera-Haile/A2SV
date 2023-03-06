class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=result=max(nums)

        while left<=right:
            mid=(left+right)//2
            curr=0
            for num in nums:
                curr+=(math.ceil(num/mid))
            
            if curr<=threshold:
                result=min(result,mid)
                right=mid-1
            else:
                left=mid+1
        return result