class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        graph={(i,j):(i,j) for i in range(m) for j in range(n)}
        
        direction={1:(0,-1,0,1),2:(-1,0,1,0),3:(0,-1,1,0), 4:(0,1,1,0), 5:(0,-1,-1,0), 6:(0,1,-1,0)}
        def check(cell,neigh):
            if not ((0<=neigh[0]<m) and (0<=neigh[1]<n)):
                return False
            a,b,c,d = direction[grid[neigh[0]][neigh[1]]]
            i,j=neigh
            cell1=(i+a,j+b)
            cell2=(i+c,j+d)
            if cell==cell1 or cell==cell2:
                return True
            return False
        
        def rep(x):
            if x==graph[x]:
                return x
            curr=rep(graph[x])
            graph[x]=curr
            return curr
        
        for i in range(m):
            for j in range(n):
                a,b,c,d = direction[grid[i][j]]
                cell0=(i,j)
                cell1=(i+a,j+b)
                cell2=(i+c,j+d)
                # print(cell1,cell2)
                if check((i,j),cell1) and check((i,j),cell2):
                    parent0=rep(cell0)
                    parent1=rep(cell1)
                    parent2=rep(cell2)
                    if parent1!=parent2 or parent1!=parent0:
                        graph[parent2]=parent1
                        graph[parent0]=parent1
                    # print(i,j,graph)
        return rep((0,0))==rep((m-1,n-1))