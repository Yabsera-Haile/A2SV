class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction=[(0,-1),(0,1),(1,0),(-1,0)]

        def check(row,col):
            return (0<=row<len(image)) and (0<=col<len(image[0]))
        
        def dfs(row,col,prev):
            image[row][col]=color

            for vert,horx in direction:
                new_col=col+horx
                new_row=row+vert
                if check(new_row,new_col) and image[new_row][new_col]==prev:
                    dfs(new_row,new_col,prev)
        
        if image[sr][sc]!=color:
            dfs(sr,sc,image[sr][sc])
        
        return image