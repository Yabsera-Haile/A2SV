# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        result=0

        def findMoves(root):
            nonlocal result
            if not root:
                return 0

            left=findMoves(root.left)
            right=findMoves(root.right)
            
            result+=abs(left)
            result+=abs(right)
            root.val+=(left+right)

            return root.val-1
        
        findMoves(root)
        return result


