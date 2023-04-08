# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:     
        result=0
        prefix=defaultdict(int)
        prefix[0]=1

        def helperFunc(root,_sum):
            nonlocal result
            if not root:
                return 
            _sum += root.val
            result += prefix[_sum - targetSum]
            prefix[_sum]+=1
            
            helperFunc(root.left,_sum)
            helperFunc(root.right,_sum)
            
            prefix[_sum] -= 1
                 

        helperFunc(root,0)
        return result