class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result=[]
        flag=False
        for line in source:
            if flag==False:
                current=""
            left=0
            while left <len(line):
                if flag and line[left:left+2]=="*/":
                    left+=1
                    flag=False
                elif flag==False and line[left:left+2]=="//":
                    break
                elif flag==False and line[left:left+2]=="/*":
                    flag=True
                    left+=1
                elif flag==False:
                    current+=line[left]
                left+=1
            if flag==False and current:      
                result.append(current)
        return result
                    
                    
                    
                    
                
                
        