class Solution:
    def minSteps(self, n: int) -> int:
        result=0
        num=2

        while n>1:
            while n%num==0:
                result+=num
                n//=num 
            num+=1
        
        return result