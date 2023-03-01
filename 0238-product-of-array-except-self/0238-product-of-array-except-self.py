class Solution:
    def productExceptSelf(self, nums):
        curr=1
        result=[]        
        for num in nums:
            result.append(curr)
            curr*=num
        curr=1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=curr
            curr*=nums[i]
        return result
            
            
        
        
        
        
        
        
        # n, ans, suffix_prod = len(nums), [1]*len(nums), 1
        # for i in range(1,n):
        #     ans[i] = ans[i-1] * nums[i-1]
        # for i in range(n-1,-1,-1):
        #     ans[i] *= suffix_prod
        #     suffix_prod *= nums[i]
        # return ans
        