class Solution:
    def interpret(self, command: str) -> str:
        #initialize stack
        stack=[]
        
        #initailize two pointers left and right
        left=0
        right=left+1
        
        #iterate the pointers and check each value
        while left< len(command):
            if command[left]=="G":
                stack.append("G")
                left+=1
                right+=1
            elif command[right]==")":
                stack.append("o")
                left+=2
                right=left+1
            else:
                stack.append("al")
                left+=4
                right=left+1
            if right >=len(command):
                right-=1
        
        return "".join(stack)
                
                
                
    