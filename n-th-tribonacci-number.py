class Solution:
    memo={0:0,1:1,2:1}
    def tribonacci(self, n: int) -> int:
        if n<3:
            return self.memo[n]
        elif n not in self.memo:
            self.memo[n]=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        
        return self.memo[n]