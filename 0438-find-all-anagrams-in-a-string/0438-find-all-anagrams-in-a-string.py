class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=list(p)
        p.sort()
        
        result=[]
        left=0
        right=len(p)
        
        while right<=len(s):
            curr=list(s[left:right])
            curr.sort()
            if curr==p:
                result.append(left)
            
            left+=1
            right+=1
            
        return result

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # const=[0 for i in range(0,26)]
        # var=[0 for i in range(0,26)]
        # ans=[]
        # for i in p:
        #     index=ord(i)-97
        #     const[index]+=1
        # left=0
        # for right in range(len(s)):
        #     while right-left+1>len(p):
        #         remindex=ord(s[left])-97
        #         var[remindex]-=1
        #         left+=1
        #     var[ord(s[right])-97]+=1
        #     if var==const:
        #         ans.append(left)
        # return ans
        