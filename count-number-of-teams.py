class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        @cache
        def findTeams(index,last, count,flag):
            if count==3:
                
                return 1
            
            result=0
            for i in range(index,n):
                if flag:
                    if last==-1 or rating[i]>rating[last]:
                        result+=findTeams(i+1,i,count+1,flag)
                else:
                    if last == -1 or rating[i]<rating[last]:
                        result+=findTeams(i+1,i,count+1,flag)

            return result
        
        return findTeams(0,-1,0,False) + findTeams(0,-1,0,True)