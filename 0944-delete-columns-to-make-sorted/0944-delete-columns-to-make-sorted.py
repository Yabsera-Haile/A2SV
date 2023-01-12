class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result=0
        for i in range(len(strs[0])):
            mini=0
            for s in strs:
                current=ord(s[i])
                if current>=mini:
                    mini=current
                else:
                    result+=1
                    break
        return result
            
        