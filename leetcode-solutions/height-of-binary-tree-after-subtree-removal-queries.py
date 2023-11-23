# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        @cache
        def findHeight(root):
            if not root:
                return -1

            return 1 + max(findHeight(root.left),findHeight(root.right))

        subtree = defaultdict(int)

        def dfs(root,depth,max_height):
            if not root: 
                return 

            subtree[root.val] = max_height

            dfs(root.left,depth+1,max(max_height,depth+1+findHeight(root.right)))
            dfs(root.right,depth+1,max(max_height,depth+1+findHeight(root.left)))

        dfs(root,0,0)

        return [subtree[i] for i in queries]


