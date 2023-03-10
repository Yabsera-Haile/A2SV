# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        count=defaultdict(list)
        result=0
        def helperFunc(root,depth,val):
            if root:
                count[depth].append(val)

                helperFunc(root.left,depth+1,2*val)
                helperFunc(root.right,depth+1,2*val+1)
        
        helperFunc(root,0,1)
        for key,value in count.items():
            curr=value[-1]-value[0]+1
            result=max(result,curr)
        
        return result