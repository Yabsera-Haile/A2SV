# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helperFunc(root):
            result=[]
            if root:
                result.extend(helperFunc(root.left))
                result.append(root.val)
                result.extend(helperFunc(root.right))
            
            return result
        
        return helperFunc(root)








        # result=[]
        # if root and root.left:
        #     curr=self.inorderTraversal(root.left)
        #     result.extend(curr)
        # if root:
        #     result.append(root.val)
        # if root and root.right:
        #     curr=self.inorderTraversal(root.right)
        #     result.extend(curr)
        
        
        # return result