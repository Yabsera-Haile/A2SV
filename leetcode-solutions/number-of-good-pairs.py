from collections import Counter
class Solution:
    def findSum(self,num:int)->int:
        result=0
        for i in range(num):
            result+=i
        return result
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #define a hashmap of frequency
        hashmap=dict(Counter(nums))
        
        #iterate
        result=0
        for key,value in hashmap.items():
            result+=self.findSum(value)
            
        return result
            
        
        