class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap={}
        for path in paths:
            info=path.split(" ")
            current=[]
            for i in range(1,len(info)):
                content=info[i].split("(")
                file=hashmap.get(content[1],-1)
                if file == -1:
                    file=[]
                    file.append(info[0]+"/"+content[0])
                    hashmap[content[1]]=file
                else:
                    file.append(info[0]+"/"+content[0])
                    hashmap[content[1]]=file
        result=[value for value in hashmap.values() if len(value)>1] 
        return result
                    
        
                
        
        
        