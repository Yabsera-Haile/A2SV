class Solution:   
    def minOperations(self, boxes: str) -> List[int]:       
        result = [0]*len(boxes)
        
        left=right=0
        leftResult=rightResult =0
        n=len(boxes)
        
        for i in range(1, n):
            if boxes[i-1] == '1': left += 1
            leftResult += left 
            result[i] = leftResult
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1': right += 1
            rightResult += right
            result[i] += rightResult
            
        return result
            
                
            
        