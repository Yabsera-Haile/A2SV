class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph={}
        for account in accounts:
            name=account[0]
            for j in range(1,len(account)):
                graph[(name,account[j])]=(name,account[j])
        
        def rep(x):
            if x == graph[x]:
                return x
            curr=rep(graph[x])
            graph[x]=curr
            return curr
        
        for account in accounts:
            name=account[0]
            for j in range(2,len(account)):
                parentA=rep((name,account[j-1]))
                parentB=rep((name,account[j]))
                if parentA!=parentB:
                    graph[parentB]=parentA
        
        pos=defaultdict(list)
        names={}
        for key,value in graph.items():
            value=rep(value)
            pos[value[1]].append(key[1])
            names[value[1]]=value[0]

        result=[]
        for key,value in pos.items():
            curr=[]
            curr.append(names[key])
            curr.extend(sorted(value))
            result.append(curr)
            
        return result