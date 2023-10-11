# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(root,key):
            if not root:
                return False
            if root.val==key:
                return [root]
            left=findPath(root.left,key)
            right=findPath(root.right,key)
            
            if left==False and right==False:
                return False
            elif left==False:
                right.append(root)
                return right
            elif right==False:
                left.append(root)
                return left
        
        tree1=set(findPath(root,p.val))
        tree2=findPath(root,q.val)
        
        for i in tree2:
            if i in tree1:
                return i