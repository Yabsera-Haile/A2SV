class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #O(n)
        count=Counter(s1)
        n=len(s1)
        found=0

        for i in range(len(s2)):
            if s2[i] in count:
                count[s2[i]]-=1
                if count[s2[i]]==0:
                    found+=1
            if i>=n and s2[i-n] in count:
                if count[s2[i-n]]==0:
                    found-=1
                count[s2[i-n]]+=1
            if found == len(count):
                return True
        
        return False

        # O(n**2)
        # s1=list(s1)
        # s1.sort()
        # left=0
        # right=len(s1)-1
        
        # while right<len(s2):
        #     current=list(s2[left:right+1])
        #     current.sort()
        #     if current == s1:
        #         return True
        #     left+=1
        #     right+=1
        # return False