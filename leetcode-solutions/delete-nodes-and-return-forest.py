# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)

        def findRoots(root):
            if not root:
                return root
                
            root.left = findRoots(root.left)
            root.right = findRoots(root.right)

            if root.val in to_delete:
                if not root.left and not root.right:
                    return None
                else:
                    if root.left:
                        result.append(root.left)
                    if root.right:
                        result.append(root.right)
                    return None
            
            return root
        
        last = findRoots(root)
        if last:
            result.append(last)

        return result
        