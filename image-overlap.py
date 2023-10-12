class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:  
        n=len(img1)
        ones1=[]
        ones2=[]
        result=defaultdict(int)

        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    ones1.append((i,j))
                if img2[i][j]:
                    ones2.append((i,j))
        if not ones1 or not ones2:
            return 0
        for row,col in ones1:
            for i,j in ones2:
                result[(i-row,j-col)]+=1
        
        return max(result.values())