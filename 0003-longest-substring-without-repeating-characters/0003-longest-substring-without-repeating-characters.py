class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=left=right=0
        
        while right<len(s):
            distinct=len(set(s[left:right+1]))
            if distinct==len(s[left:right+1]):
                result=max(distinct,result)
                right+=1
            else:
                left+=1
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # seen = {}
        # l = 0
        # output = 0
        # for r in range(len(s)):
        #     if s[r] not in seen:
        #         output = max(output,r-l+1)
        #     else:
        #         if seen[s[r]] < l:
        #             output = max(output,r-l+1)
        #         else:
        #             l = seen[s[r]] + 1
        #     seen[s[r]] = r
        # return output
        