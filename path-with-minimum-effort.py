class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        n=len(heights)
        m=len(heights[0])

        def checkInbound(row,col):
            return (0<= row < n) and (0<= col<m)
        
        dict={}

        for i in range(n):
            for j in range(m):
                dict[(i,j)]=float("inf")
        dict[(0,0)]=0

        visited=set()
        queue=[(0,(0,0))]

        while queue:
            curr_dist,node =heappop(queue)
            row,col=node
            if node in visited:
                continue
            visited.add(node)

            for change_x,change_y in directions:
                new_row=row+change_x
                new_col=col+change_y

                if checkInbound(new_row,new_col):
                    distance=max(curr_dist,abs(heights[row][col]-heights[new_row][new_col]))
                    
                    if distance < dict[(new_row,new_col)]:
                        dict[(new_row,new_col)]=distance
                        heappush(queue,(distance,(new_row,new_col)))

        return dict[(n-1,m-1)]