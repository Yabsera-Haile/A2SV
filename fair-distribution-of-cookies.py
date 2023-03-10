class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        result=float("inf")

        def distribute(curr,index):
            nonlocal result
            if index==len(cookies):
                temp=max(curr)
                result=min(result,temp)
            elif index<len(cookies):
                for i in range(k):
                    curr[i]+=cookies[index]
                    if curr[i]<result:
                        distribute(curr,index+1)
                    curr[i]-=cookies[index]
        curr=[0]*k
        distribute(curr,0)
        return result