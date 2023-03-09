# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result=0
        def count(root):
            nonlocal result
            if not root:
                return [0,0]

            left=count(root.left)
            right=count(root.right)
            size=left[1]+right[1]+1
            sums=left[0]+right[0]+root.val
            average=sums//size
            
            if average==root.val:
                result+=1
                
            return [sums,size]

        count(root)
        return result