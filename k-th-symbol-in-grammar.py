class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helperFunc(n,k,p):
            if n==1:
                return 0 if p==1 else 1
            else:
                tempK=math.ceil(k/2)
                tempP=2 if tempK==k//2 else 1
                curr=helperFunc(n-1,tempK,tempP)
                if curr==0:
                    if p==1:
                        return 0
                    else:
                        return 1
                elif curr==1:
                    if p==1:
                        return 1
                    else:
                        return 0

        return helperFunc(n,k,1)