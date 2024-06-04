class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        result=0
        odd=0
        for key,value in count.items():
            if value%2==0:
                result+=value
            else:
                result+=value-1
                odd=1
        result+=odd
        
        return result
        