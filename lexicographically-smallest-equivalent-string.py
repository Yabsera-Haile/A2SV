class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Union Find
        n=len(s1)
        parent=[i for i in range(26)]

        def find(letter):
            root=letter
            while root!=parent[root]:
                root=parent[root]
            while letter!=root:
                temp=parent[letter]
                parent[letter]=root
                letter=temp
            return root
        
        def union(letter1,letter2):
            parent1=find(letter1)
            parent2=find(letter2)

            if parent1!=parent2:
                if parent1<parent2:
                    parent[parent2]=parent1
                else:
                    parent[parent1]=parent2
        
        for i in range(n):
            letter1=ord(s1[i])-ord('a')
            letter2=ord(s2[i])-ord('a')
            union(letter1,letter2)
        
        result=[]
        for letter in baseStr:
            curr=ord(letter)-ord('a')
            result.append(chr(find(curr)+ord('a')))
        
        return "".join(result)




        # DFS
        # graph={chr(97+i):chr(97+i) for i in range(26)}

        # def rep(x):
        #     if x==graph[x]:
        #         return x
        #     curr=rep(graph[x])
        #     graph[x]=curr
        #     return curr
        
        # for i in range(len(s1)):
        #     parent1=rep(s1[i])
        #     parent2=rep(s2[i])
        #     if parent1<parent2:
        #         graph[parent2]=parent1
        #     elif parent2<parent1:
        #         graph[parent1]=parent2
        
        # result=[]
        # for letter in baseStr:
        #     result.append(rep(letter))
        
        # return "".join(result)