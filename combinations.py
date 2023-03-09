class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]

        def backtrack(canidate,k,first):
            if k==0:
                result.append(canidate)
            else:
                for i in range(first,n+1):
                    canidate.append(i)
                    backtrack(canidate[::],k-1,i+1)
                    canidate.pop()
        backtrack([],k,1)
        return result