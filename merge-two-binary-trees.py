# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        temp=None
        if root1 and root2:
            temp=TreeNode()
            temp.val=root1.val+root2.val
            temp.left=self.mergeTrees(root1.left,root2.left)
            temp.right=self.mergeTrees(root1.right,root2.right)
        elif root1:
            temp=TreeNode(root1.val,root1.left,root1.right)
        elif root2:
            temp=TreeNode(root2.val,root2.left,root2.right)

        return temp