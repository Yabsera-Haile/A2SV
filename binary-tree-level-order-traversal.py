# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=defaultdict(list)

        def helperFunc(root,depth):
            if root:
                curr=[]
                if root.left:
                    curr.append(helperFunc(root.left,depth+1))
                if root.right:
                    curr.append(helperFunc(root.right,depth+1))
                if len(curr)>0:
                    result[depth+1].extend(curr)
                
                return root.val
        
        first=helperFunc(root,0)
        result[0].append(first)
        myKeys = list(result.keys())
        myKeys.sort()
        sorted_dict = {i: result[i] for i in myKeys}

        return sorted_dict.values() if root else []