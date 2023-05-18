class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph={i:i for i in range(len(s))}

        def rep(x):
            if x == graph[x]:
                return x
            curr=rep(graph[x])
            graph[x]=curr
            return curr
 
        for pair in pairs:
            parentA=rep(pair[0])
            parentB=rep(pair[1])
            if parentA!=parentB:
                graph[parentB]=parentA

        index=defaultdict(list)
        letter=defaultdict(list)
        for key,value in graph.items():
            index[rep(value)].append(key)
            letter[rep(value)].append(s[key])
        
        for key in index.keys():
            index[key].sort()
            letter[key].sort()

        result=list(s)
        for key in index.keys():
            for i in range(len(index[key])):
                result[index[key][i]]=letter[key][i]
                
        # print(index,letter)  
        return "".join(result)