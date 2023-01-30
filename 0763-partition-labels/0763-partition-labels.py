class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l= len(s)
        last = {s[i]: i for i in range(l)} 
        i=0
        result=[]
        while i<l:
            j=i+1
            end=last[s[i]]
            while j<end:
                end=max(last[s[j]],end)
                j+=1
            result.append(end-i+1)
            i=end+1
        return result
