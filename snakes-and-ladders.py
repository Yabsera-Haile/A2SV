class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)

        ref = {}
        num=1
        cols=list(range(0,n))
        for row in range(n - 1, -1, -1):
            for col in cols:
                ref[num] = (row, col)
                num += 1
            cols.reverse()

        queue=deque([1])
        seen=set([1])
        result=0
        while queue:
            l=len(queue)
            for _ in range(l):
                
                curr=queue.popleft()
                if curr==n**2:
                    return result

                for num in range(curr+1,min(curr+6,n**2)+1):
                    row,col=ref[num]
                    if num not in seen and board[row][col]==-1:
                        seen.add(num)
                        queue.append(num)
                    elif num not in seen and board[row][col] not in seen:
                        seen.add(num)
                        queue.append(board[row][col])

            result+=1

        return -1