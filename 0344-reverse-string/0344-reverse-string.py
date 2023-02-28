class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helperFunc(left,right):
            if left<right:
                s[left], s[right] = s[right], s[left]
                helperFunc(left+1,right-1)
            else:
                return s
            
        return helperFunc(0,len(s)-1)

        
        
        
        
        
        
        
        
#         left=0
#         right=len(s)-1
        
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left+=1
#             right-=1
            
#         return s