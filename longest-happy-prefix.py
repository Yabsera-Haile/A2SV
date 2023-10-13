class Solution:
    def longestPrefix(self, s: str) -> str:
        n=len(s)
        prev,i = 0,1
        lps=[0]*n

        while i<n:
            if s[i]==s[prev]:
                lps[i]=prev+1
                prev+=1
                i+=1
            else:
                if prev==0:
                    i+=1
                else:
                    prev=lps[prev-1]
        
        l=lps[-1]
        
        return s[:l]