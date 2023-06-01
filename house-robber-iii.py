# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo={}
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        if root not in self.memo:
            child=0
            gr_child=0
            if root.left:
                child+=self.rob(root.left)
                gr_child+=self.rob(root.left.right)+self.rob(root.left.left)
            if root.right:
                child+=self.rob(root.right)
                gr_child+=self.rob(root.right.right)+self.rob(root.right.left)    

            self.memo[root]=max(child,gr_child+root.val)   

        return self.memo[root]