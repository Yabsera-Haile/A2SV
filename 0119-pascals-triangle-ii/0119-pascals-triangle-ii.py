class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def helperFunc(index,row):
            if index==rowIndex:
                return row
            else:
                curr=[1]
                for i in range(1,len(row)):
                    curr.append(row[i-1]+row[i])
                curr.append(1)
                
                return helperFunc(index+1,curr)
            
        return helperFunc(0,[1])
            
            
        
        