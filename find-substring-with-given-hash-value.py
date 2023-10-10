class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n=len(s)
        val={}
        pk=pow(power,k,modulo)
        for i in range(26):
            val[chr(i+ord('a'))]=i+1
            
        window=0
        result=0
        for i in range(n-1,-1,-1):
            window = (window * power + val[s[i]]) % modulo

            if i+k<n:
                window = (window - val[s[i+k]]*pk) % modulo
   
            if window == hashValue:
                result=i
        
        return s[result:result+k]