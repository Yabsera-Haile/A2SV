class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                current=diagonals.get(i+j,-1)
                if current==-1:
                    diagonals[i+j]=[mat[i][j]]
                else:
                    current.append(mat[i][j])
                    diagonals[i+j]=current
                    
        result=[]
        for key,value in diagonals.items():
            if key%2!=0:
                for val in value:
                    result.append(val)
            else:
                for val in value[::-1]:
                    result.append(val)
        return result
                    
                
            
        