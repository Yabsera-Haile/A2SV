class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def mah(heights: List[int]) -> int:
            st=[]
            maxArea=0
            for bar in heights+[-1]:
                step=0
                while st and st[-1][1]>=bar:
                    w,h=st.pop()
                    step+=w
                    maxArea=max(maxArea,step*h)
                st.append((step+1,bar))
            return maxArea
        n,m=len(matrix),len(matrix[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    matrix[i][j]=1
                else:
                    matrix[i][j]=0 
                if i>0 and matrix[i][j]!=0:
                    matrix[i][j]=matrix[i-1][j]+matrix[i][j]
            ans=max(ans,mah(matrix[i]))
        return ans