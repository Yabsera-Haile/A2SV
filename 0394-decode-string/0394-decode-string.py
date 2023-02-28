class Solution:
    def decodeString(self, s: str) -> str:
        end = {}
        start = []
        for index,char in enumerate(s):
            if char == '[':
                start.append(index)
            elif char == ']':
                end[start.pop()] = index
                
        def helperFunc(left,right):
            result=[]
            count=0
            
            while left<=right:
                curr=s[left]
                if curr.isdigit():
                    count=count*10+int(curr)
                elif curr=="[":
                    result.append(helperFunc(left+1,end[left]-1)*count)
                    count=0
                    left=end[left]
                else:
                    result.append(curr)
                left+=1
                
            return "".join(result)
        
        return helperFunc(0,len(s)-1)
                  
            
            
            
            
            
            
            
            
            
   
            
            
