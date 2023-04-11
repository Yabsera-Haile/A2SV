"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        result=0

        def dfs(root,depth):
            nonlocal result
            if not root.children:
                result=max(result,depth)
            
            for child in root.children:
                dfs(child,depth+1)

        if root:
            dfs(root,1)

        return result