class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        direction=[1,-1,10,-10,100,-100,1000,-1000]
        result=0
        queue=deque()
        if "0000" not in deadends:
            queue.append("0000")

        while queue:
            l=len(queue)

            for _ in range(l):
                curr=queue.popleft()
                if curr==target:
                    return result

                for change in direction:
                    temp=int(curr)
                    if change<0 and (temp//abs(change)%10) == 0:
                        temp-=(9*change)
                    elif change>0 and (temp//abs(change)%10) == 9:
                        temp-=(9*change)
                    else:
                        temp+=change
                    temp=str(temp)
                    temp="0"*(4-len(temp))+temp
                    if temp not in deadends:
                        queue.append(temp)
                        deadends.add(temp)

            result+=1
        
        return -1