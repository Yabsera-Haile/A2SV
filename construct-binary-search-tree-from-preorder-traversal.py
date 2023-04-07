# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        head=TreeNode(preorder[0])

        for i in range(1,len(preorder)):
            curr=head
            while curr.left or curr.right:
                if curr.left and curr.val>preorder[i]:
                    curr=curr.left
                elif curr.right and curr.val<preorder[i]:
                    curr=curr.right
                else:
                    break
            if curr.val>preorder[i]:
                curr.left=TreeNode(preorder[i])
            if curr.val<preorder[i]:
                curr.right=TreeNode(preorder[i])     
        
        return head