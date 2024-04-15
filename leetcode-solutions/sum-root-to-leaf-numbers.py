# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result=[]
        def dfs(root,path):
            if not root.left and not root.right:
                result.append(int("".join(path)))
            if root.left:
                path.append(str(root.left.val))
                dfs(root.left,path)
                path.pop()
            if root.right:
                path.append(str(root.right.val))
                dfs(root.right,path)
                path.pop()
        
        dfs(root,[str(root.val)])
        print(result)
        return sum(result)