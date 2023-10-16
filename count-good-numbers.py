class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=(10**9)+7
        odds=n//2
        evens=ceil(n/2)
        return (pow(4,odds,mod) * pow(5,evens,mod))%mod