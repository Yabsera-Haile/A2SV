class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows=[]
        zero_cols=[]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.append(row)
                    zero_cols.append(col)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zero_rows:
                    matrix[row][col]=0
                elif col in zero_cols:
                    matrix[row][col]=0
        