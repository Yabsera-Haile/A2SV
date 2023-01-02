from collections import Counter
class Solution:
    def findSum(self,num:int)->int:
        result=0
        for i in range(num):
            result+=i
        return result
    def similarPairs(self, words: List[str]) -> int:
        #change to set
        words=["".join(sorted(set(word))) for word in words]
        hashmap=dict(Counter(words))
      
        #iterate
        result=0
        for key,value in hashmap.items():
                result+=self.findSum(value)
        return result
        