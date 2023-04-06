class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime=[True for _ in range(right+1)]
        prime[0]=prime[1]=False
        i=2
        while i*i<=right:
            if prime[i]:
                j=i*i
                while j<=right:
                    prime[j]=False
                    j+=i
            i+=1

        _min=right-left+1
        result=[-1,-1]
        prev=curr=-1

        for i in range(left,right+1):
            if prime[i]:
                if prev==-1:
                    prev=i
                else:
                    curr=i
                    if curr-prev<_min:
                        _min=curr-prev
                        result=[prev,curr]
                    prev=i
        
        return result