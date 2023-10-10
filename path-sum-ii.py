# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result=[]

        def helperFunc(root,nodes,_sum):
            if not root:
                return
            _sum += root.val
            nodes.append(root.val)

            if (not root.right) and (not root.left):
                if _sum==targetSum and nodes:
                    result.append(nodes)
                    return

            helperFunc(root.left,nodes[::],_sum)
            helperFunc(root.right,nodes[::],_sum)


        helperFunc(root,[],0)
        return result