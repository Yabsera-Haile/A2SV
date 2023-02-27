class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # distinct=set(s)
        
        result=0
        
        for d in set(s):
            count=0
            left=0
            for right,letter in enumerate(s):
                if letter!=d:
                    count+=1
                while left<=right and count>k:
                    if s[left]!=d:
                        count-=1
                    left+=1
                result=max(result,right-left+1)
        return result
                    
        