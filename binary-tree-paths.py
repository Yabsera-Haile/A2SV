# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        def helperFunc(root,curr):
            if root:
                curr.append(str(root.val))
                if not root.right and not root.left:
                    result.append(curr)
                else:
                    helperFunc(root.left,curr.copy())
                    helperFunc(root.right,curr.copy())
        helperFunc(root,[])

        for i,path in enumerate(result):
            result[i]="->".join(path)
        return result