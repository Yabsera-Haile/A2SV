class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph={i:i for i in range(len(source))}

        def rep(x):
            if x==graph[x]:
                return x
            curr=rep(graph[x])
            graph[x]=curr
            return curr
        
        for a,b in allowedSwaps:
            parentA=rep(a)
            parentB=rep(b)
            if parentA!=parentB:
                graph[parentB]=parentA
        
        index = defaultdict(list)
        for i in range(len(source)):
            parent=rep(i)
            index[parent].append(i)
        
        result=0
        for key,value in index.items():
            source_nums=[source[i] for i in value]
            target_nums=[target[i] for i in value]
            source_count=Counter(source_nums)
            target_count=Counter(target_nums)

            for num,count in source_count.items():
                temp=target_count[num]
                if count>temp:
                    result+=count-temp
        
        return result