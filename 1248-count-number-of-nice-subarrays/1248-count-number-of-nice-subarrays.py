class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        result=0
        count=0
        
        for right in range(len(nums)): 
            if nums[right]%2==1:
                k-=1
                count=0
            while k==0:
                if nums[left]%2==1:
                    k+=1
                left+=1
                count+=1
            result+=count
        
        return result