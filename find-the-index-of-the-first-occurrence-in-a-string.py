class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1

        mod = 10**9+7
        a = []
        for i in range(m-1,-1,-1):
            a.append(26**i)
        
        window = 0
        result = 0
        for i in range(m):
            window+=((ord(haystack[i])-ord('a'))*a[i])
            window%=mod
            result+=((ord(needle[i])-ord('a'))*a[i])
            result%=mod
        if result == window:
            return 0

        for i in range(m,n):
            window -= ((ord(haystack[i-m])-ord('a'))*a[0])
            window *= 26 
            window += (ord(haystack[i])-ord('a'))
            window %= mod
            if window == result:
                return i - m + 1
                         
        return -1