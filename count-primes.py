class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[True for _ in range(n)]
        for i in range(0,min(2,len(prime))):
            prime[i]=False
        i=2
        while i*i<n:
            if prime[i]:
                j=i*i
                while j<n:
                    prime[j]=False
                    j+=i
            i+=1
        
        result=0

        for val in prime:
            if val:
                result+=1
        
        return result