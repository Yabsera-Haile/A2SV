# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        elif p and q:
            answer=False
            if p.val==q.val:
                answer=True
            answer=answer and self.isSameTree(p.left,q.left)
            answer=answer and self.isSameTree(p.right,q.right)

            return answer
        else:
            return False