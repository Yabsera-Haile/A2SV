class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)


        count=list(Counter(deck).values())

        if min(count)==1:
            return False
            
        for i in range(1,len(count)):
            if gcd(count[i],count[i-1])<=1:
                return False
        
        return True