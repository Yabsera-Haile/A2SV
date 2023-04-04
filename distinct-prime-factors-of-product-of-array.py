class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primeFactorize(n):
            result=set()
            d=2
            while d*d<=n:
                while n%d==0:
                    result.add(d)
                    n//=d
                d+=1
            if n>1:
                result.add(n)
            return result

        result=set()
        for num in nums:
            factor=primeFactorize(num)
            result=result.union(factor)
        
        return len(result)