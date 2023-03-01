class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result=0
        freq={0:1}
        prefix=0
        
        for num in nums:
            prefix+=num
            if (prefix % k) in freq:
                result+=freq[prefix%k]
            freq[prefix%k]=freq.get(prefix%k,0)+1         
        
        return result
        