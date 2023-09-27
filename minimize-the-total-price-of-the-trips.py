class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
      graph=defaultdict(list)
      for src,dist in edges:
        graph[src].append(dist)
        graph[dist].append(src)

      freq=[0]*n
      visited=set()

      def dfs(src,dist,path):
        path.add(src)
        visited.add(src)

        if src==dist:
          for node in path:
            freq[node]+=1
          return True
        
        for neigh in graph[src]:
          if neigh not in visited and dfs(neigh,dist,path):
            return True
        
        path.remove(src)
        return False
      
      for src,dist in trips:
        dfs(src,dist,set())
        visited.clear()
      
      memo={}

      def findTotalPrice(curr,parent,flag):
        if (curr,flag) in memo:
          return memo[(curr,flag)]
        
        result1= price[curr]*freq[curr]
        for neigh in graph[curr]:
          if neigh!=parent:
            result1+=findTotalPrice(neigh,curr,False)
        
        result2=inf
        if not flag:
          result2= (price[curr]//2)*freq[curr]
          for neigh in graph[curr]:
            if neigh != parent:
              result2+=findTotalPrice(neigh,curr,True)
        
        memo[(curr,flag)]= min(result1,result2)
        return memo[(curr,flag)]
      
      return findTotalPrice(0,-1,False)