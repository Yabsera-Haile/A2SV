# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        visited=set()
        result={}
        def findDuplicates(root):
            if not root:
                return ["#"]
            value=[str(root.val)]
            value.extend(findDuplicates(root.left))
            value.extend(findDuplicates(root.right))
            key=",".join(value)
            if key in visited:
                result[key]=root
            else:
                visited.add(key)

            return value

        findDuplicates(root)

        return result.values()