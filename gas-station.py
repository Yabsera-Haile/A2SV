class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        diffs=[gas[i]-cost[i] for i in range(n)]

        if sum(diffs)<0:
            return -1
        
        prefix=0
        result=-1
        for i in range(n):
            if prefix+diffs[i]<0:
                result=-1
                prefix=0
                continue
            elif result==-1:
                result=i
            prefix+=diffs[i]
        
        return result