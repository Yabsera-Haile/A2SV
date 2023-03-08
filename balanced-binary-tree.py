# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helperFunc(root):
            result=0
            if root:
                result+=1
                left=helperFunc(root.left)
                right=helperFunc(root.right)

                if left==-1 or right==-1 or abs(left-right)>1:
                    return -1
                else:
                    result+=max(left,right)

            return result
        
        if helperFunc(root)==-1:
            return False
        else:
            return True