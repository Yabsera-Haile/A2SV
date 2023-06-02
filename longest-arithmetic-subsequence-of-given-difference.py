class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        result=[]
        hashmap=defaultdict(int)

        for i in range(len(arr)):
            result.append(hashmap[arr[i]-difference]+1)
            hashmap[arr[i]]=result[-1]
        
        return max(result)