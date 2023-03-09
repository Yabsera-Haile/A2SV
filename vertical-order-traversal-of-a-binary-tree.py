# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes=[]

        def helperFunc(root,row,col):
            if root:
                helperFunc(root.left,row+1,col-1)
                helperFunc(root.right,row+1,col+1)
                nodes.append([root.val,row,col])
        helperFunc(root,0,0)
        sorted_nodes=sorted(nodes,key=lambda x:[x[2],x[1],x[0]])
        result=defaultdict(list)
        
        for node in sorted_nodes:
            result[node[2]].append(node[0])
        return result.values()








        # helperFunc(root,0)
        # myKeys = list(nodes.keys())
        # myKeys.sort()
        # result = {i: nodes[i] for i in myKeys}
        # for key,value in result.items():
        #     value.sort()

        # return result.values() if root else []