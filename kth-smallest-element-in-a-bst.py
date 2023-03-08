# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helperFunc(root):
            result=[]
            if root:
                result.extend(helperFunc(root.left))
                result.append(root.val)
                result.extend(helperFunc(root.right))
            return result
        
        answer=helperFunc(root)
        return answer[k-1]