# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def helperFunc(root,par,g_par):
            if not root:
                return 0
            result=0
            if g_par % 2==0:
                result=root.val
            result+=helperFunc(root.left,root.val,par)
            result+=helperFunc(root.right,root.val,par)

            return result
        return helperFunc(root,1,1)