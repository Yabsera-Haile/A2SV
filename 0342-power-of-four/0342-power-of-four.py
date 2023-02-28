class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        result=False
        if n>1:
            result=self.isPowerOfFour(n/4)
        elif n==1:
            result= True
        else:
            result= False
        return result
            
        