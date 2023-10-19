class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)

        @cache
        def findDistance(index1,index2,mode):
            if index1>n-1:
                return m-index2
            if index2>m-1:
                return n-index1
            if word1[index1]==word2[index2]:
                return findDistance(index1+1,index2+1,0)
            else:
                insert=findDistance(index1,index2+1,1)+1
                delete=findDistance(index1+1,index2,2)+1
                replace=findDistance(index1+1,index2+1,3)+1
    
                return min(insert,delete,replace)
        
        return findDistance(0,0,0)