# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result=float("-inf")
        def dfs(root):
            nonlocal result
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            curr=max(root.val+left,root.val+right,root.val)
            result=max(result,curr,root.val+left+right)
            return curr
        dfs(root)
        return result