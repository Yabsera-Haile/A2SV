class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
    
        
        for n in range(len(matrix)):
            row=n-1
            col=n-1
            
            while row>=0:
                matrix[row][n],matrix[n][col]=matrix[n][col],matrix[row][n]
                row-=1
                col-=1                
                
            
            
        