class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        parent=[i for i in range(n*n)]
        size=[1 for i in range(n*n)]

        def check(row,col):
            return 0<=row<n and 0<=col<n

        def find(node):
            if node==parent[node]:
                return node
            else:
                parent[node]=find(parent[node])
                return parent[node]

        def union(node1,node2):
            parent1=find(node1)
            parent2=find(node2)
            
            if parent1!=parent2:
                if size[parent1]>size[parent2]:
                    parent[parent2]=parent1
                    size[parent1]+=size[parent2]
                else:
                    parent[parent1]=parent2
                    size[parent2]+=size[parent1]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    node1 = (i*n)+j
                    for row,col in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if check(row,col) and grid[row][col]:
                            node2=(row*n)+col
                            union(node1,node2)

        result=0 
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    neigh=set()
                    for row,col in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if check(row,col) and grid[row][col]:
                            node=(row*n)+col
                            neigh.add(find(node))
                    curr=1
                    for node in neigh:
                        curr+=size[node]
                    result=max(result,curr)

        for i in range(n*n):
            result=max(result,size[find(i)])

        return result