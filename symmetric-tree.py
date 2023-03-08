# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helperFunc(root1,root2):
            if not root1 and not root2:
                return True
            elif root1 and root2:
                result=root1.val==root2.val
                result = result and helperFunc(root1.left,root2.right)
                result = result and helperFunc(root1.right,root2.left)
                return result
            else:
                return False
        
        return helperFunc(root.left,root.right)