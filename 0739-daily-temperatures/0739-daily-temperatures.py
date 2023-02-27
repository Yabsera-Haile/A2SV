class Solution:
    def dailyTemperatures(self, T):
        stack=deque()
        result=[0]*len(T)
        
        for index,temp in enumerate(T):
            while stack and T[stack[-1]]<temp:
                result[stack[-1]]=index-stack[-1]
                stack.pop()
                
            stack.append(index)

        return result
            
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      