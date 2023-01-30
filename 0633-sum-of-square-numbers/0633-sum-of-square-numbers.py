class Solution:
    def judgeSquareSum(self, c: int) -> bool:        
        left=0
        right=int(sqrt(c))
        while left <= right:
            result=(left**2)+(right**2)
            if result==c:
                return True
            elif result > c:
                right-=1
            else:
                left+=1
        return False
        