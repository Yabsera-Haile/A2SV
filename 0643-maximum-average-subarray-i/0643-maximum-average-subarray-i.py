class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=k-1
        
        result=0
        
        for i in range(k):
            result+=nums[i]
        
        
        temp=result 
        while right<len(nums)-1:
            
            temp-=nums[left]
            temp+=nums[right+1]
            result=max(temp,result)
            
            left+=1
            right+=1
            
        return float(result)/k
            
            
        