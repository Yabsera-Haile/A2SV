class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        change=[0]*len(s)
        
        for shift in shifts:
            if shift[2]==1:
                change[shift[0]]+=1
                if shift[1]!=len(s)-1:
                    change[shift[1]+1]-=1
            elif shift[2]==0:
                change[shift[0]]-=1
                if shift[1]!=len(s)-1:
                    change[shift[1]+1]+=1  
        preSum = 0
        for i in range(len(s)):
            preSum += change[i]
            
            curr = (((ord(s[i]) + preSum) - 97) % 26) + 97
            s = s[:i] + chr(curr) + s[i+1:]
        
        return s
        
        # for i in range(1,len(change)):
        #     change[i]+=change[i-1]
        
#         result=[]
        
#         for index,value in enumerate(change):
#             curr=ord(s[index])+(value%26)
#             if curr<ord('a'):
#                 result.append(chr(ord('z')-(ord('a')-curr)))
#             elif curr>ord('z'):
#                 result.append(chr(ord('a')+(curr-ord('z'))))
#             else:
#                 result.append(chr(curr))
#         return "".join(result)
            
                
                
        
            
        
        
        
        
        
        
        
    

            
        

            
        