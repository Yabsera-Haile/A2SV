class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Binary Exponentiation
        neg=n>0
        n=abs(n)
        result=1
        while n>0:
            if n & 1:
                result*=x
            x*=x
            n>>=1
        return result if neg else 1/result

        # Recursive
        # def helperFunc(x,n):
        #     if n==1 or n==0 or n==-1:
        #         return x**n
        #     else:
        #         if n%2==0:
        #             return helperFunc(x,n//2) **2
        #         else:
        #             return helperFunc(x,n//2) **2*x


        # return helperFunc(x,n)