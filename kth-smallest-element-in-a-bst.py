# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root):
            result=[]
            if root:
                result.extend(inOrder(root.left))
                result.append(root.val)
                result.extend(inOrder(root.right))
            return result
        
        result=inOrder(root)
        return result[k-1]