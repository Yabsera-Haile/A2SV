class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.prefix[i][j]=self.prefix[i-1][j]+self.prefix[i][j-1] - self.prefix[i-1][j-1]+matrix[i-1][j-1]
                


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        result=self.prefix[row2+1][col2+1]-self.prefix[row2+1][col1]-self.prefix[row1][col2+1]+self.prefix[row1][col1]

        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in range(len(matrix)):
        #     for j in range(1, len(matrix[i])):
        #         matrix[i][j] += matrix[i][j - 1]
        # for i in range(len(matrix[0])):
        #     for j in range(1, len(matrix)):
        #         matrix[j][i] += matrix[j - 1][i]
        # self.matrix = matrix 
        
                # answer = self.matrix[row2][col2]
        # if col1 > 0:
        #     answer -= self.matrix[row2][col1 - 1]
        # if row1 > 0:
        #     answer -= self.matrix[row1 - 1][col2]
        # if row1 > 0 and col1 > 0:
        #     answer += self.matrix[row1 - 1][col1 - 1]
        # return answer