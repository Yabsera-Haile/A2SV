class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helperFunc(x,n):
            if n==1 or n==0 or n==-1:
                return x**n
            else:
                if n%2==0:
                    return helperFunc(x,n//2) **2
                else:
                    return helperFunc(x,n//2) **2*x


        return helperFunc(x,n)