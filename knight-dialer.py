class Solution:
    def knightDialer(self, n: int) -> int:
        position={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),0:(3,1)}
        directions=[(2,-1),(2,1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        memo={}

        def checkInbound(row,col):
            return ((0<=row<3) and (0<=col<3)) or (row==3 and col==1)
        
        @cache
        def findNums(n,pos):
            if n==0:
                return 1

            result=0
            for change_x,change_y in directions:
                new_row=pos[0]+change_y
                new_col=pos[1]+change_x

                if checkInbound(new_row,new_col):
                    result+=(findNums(n-1,(new_row,new_col))% (10**9+7))
            
            return result
        
        result=0

        for i in range(10):
            result+=findNums(n-1,position[i])

        
        return result % (10**9+7)