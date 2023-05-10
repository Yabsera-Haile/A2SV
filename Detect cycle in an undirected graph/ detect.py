from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		color=[0]*V
		def dfs(vertex,prev):
		    if color[vertex]==2:
		        return True
		    if color[vertex]==1:
		        return False
		        
		    color[vertex]=1
		    
		    for neigh in adj[vertex]:
		        if neigh != prev:
		            curr=dfs(neigh,vertex)
    		        if not curr:
    		            return curr
    		            
		    color[vertex]=2
		    return True
	    
	    for i in range(V):
	        if color[i]==0:
	            curr=dfs(i,-1)
	            if not curr:
	                return 1
	    return 0


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends