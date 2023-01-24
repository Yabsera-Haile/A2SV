class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonals={}
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                current=diagonals.get(row-col,-1)
                if current == -1:
                    diagonals[row-col] = matrix[row][col]
                elif current != matrix[row][col]:
                    return False
        return True
                    
        