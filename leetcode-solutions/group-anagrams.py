class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)

        for s in strs:
            temp=str(sorted(s))
            result[temp].append(s)
        
        return result.values()
        