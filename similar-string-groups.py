class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs)
        parent=[i for i in range(n)]
        rank=[0]*n

        def checkAnagram(word1,word2):
            count=0
            index=-1
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    if count==0:
                        count+=1
                        index=i
                    elif count==1 and word1[i]==word2[index] and word2[i]==word1[index]:
                        count+=1
                    else:
                        return False
            return True
        
        def find(word):
            root=word
            while root!=parent[root]:
                root=parent[root]
            
            while word!=root:
                temp=parent[word]
                parent[word]=root
                word=root
            return root
        
        def union(word1,word2):
            parent1=find(word1)
            parent2=find(word2)
            if parent1!=parent2:
                if rank[parent1]>rank[parent2]:
                    parent[parent2]=parent1
                elif rank[parent1]<rank[parent2]:
                    parent[parent1]=parent2
                else:
                    parent[parent2]=parent1
                    rank[parent1]+=1

        for i in range(n):
            for j in range(i+1,n):
                if checkAnagram(strs[i],strs[j]):
                    union(i,j)

        for i in range(n):
            find(i)

        result=set(parent)
        return len(result)