# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        def checkValue(root):
            if not root:
                return 0
            return root.val
        
        return checkValue(root) == checkValue(root.left) + checkValue(root.right)
        
        