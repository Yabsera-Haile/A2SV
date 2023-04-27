# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue=deque([root])
        result=[]

        while queue:
            l=len(queue)
            curr=0

            for _ in range(l):
                temp=queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                curr+=temp.val
            result.append(curr/l)
        
        return result