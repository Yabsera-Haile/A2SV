class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)

        @cache
        def checkSub(i,j,flag):
            if i>=n or j>=m:
                return False
            if i==n-1 and s[i]==t[j]:
                return True
            if s[i]!=t[j]:
                return checkSub(i,j+1,False)
            else:
                return checkSub(i+1,j+1,False) or checkSub(i,j+1,True)
        if not n:
            return True

        return checkSub(0,0,False)
        