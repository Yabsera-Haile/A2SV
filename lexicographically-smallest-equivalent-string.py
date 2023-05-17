class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph={chr(97+i):chr(97+i) for i in range(26)}

        def rep(x):
            if x==graph[x]:
                return x
            curr=rep(graph[x])
            graph[x]=curr
            return curr
        
        for i in range(len(s1)):
            parent1=rep(s1[i])
            parent2=rep(s2[i])
            if parent1<parent2:
                graph[parent2]=parent1
            elif parent2<parent1:
                graph[parent1]=parent2
        
        result=[]
        for letter in baseStr:
            result.append(rep(letter))
        
        return "".join(result)