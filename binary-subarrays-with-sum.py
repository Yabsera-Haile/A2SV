from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ref=defaultdict(int)
        prefix=0
        ref[0]=1
        result=0

        for num in nums:
            prefix+=num
            if prefix - goal in ref:
                result+=ref[prefix-goal]
            
            ref[prefix]+=1
        return result