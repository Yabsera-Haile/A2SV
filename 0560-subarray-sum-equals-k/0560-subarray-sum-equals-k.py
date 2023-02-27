class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        freq={0:1}
        result=0
        for num in nums:
            prefix+=num
            
            if prefix-k in freq:
                result+=freq[prefix-k]
            
            if prefix in freq:
                freq[prefix]+=1
            else:
                freq[prefix]=1
            
        return result
            
            
        
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # dic = {0:1}
        # res = 0
        # curr = 0
        # for i in range(len(nums)):
        #     curr += nums[i]
        #     res += dic.get(curr-k, 0)
        #     dic[curr] = dic.get(curr, 0) +1
        # return res 
        