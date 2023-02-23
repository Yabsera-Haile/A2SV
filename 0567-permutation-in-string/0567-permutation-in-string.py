class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s1.sort()
        left=0
        right=len(s1)-1
        
        while right<len(s2):
            current=list(s2[left:right+1])
            current.sort()
            if current == s1:
                return True
            left+=1
            right+=1
        return False
            
        