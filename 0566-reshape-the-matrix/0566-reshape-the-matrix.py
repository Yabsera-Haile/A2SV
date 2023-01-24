class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        col_len=len(mat[0])
        n_elements=len(mat)*len(mat[0])
        if n_elements != r*c:
            return mat
        
        result=[[0]*c for _ in range(r)]
        
        for row in range(r):
            for col in range(c):
                unique = (row * c) + col
                i= unique // col_len
                j= unique % col_len
                result[row][col] = mat [i][j]
        return result
                    
        