# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count=defaultdict(int)

        def counter(root):
            if root:
                count[root.val]+=1
                counter(root.left)
                counter(root.right)
        counter(root)
        count=dict(sorted(list(count.items()),key=lambda x:x[1],reverse=True))
        
        result=[]
        for key,value in count.items():
            if not result:
                result.append(key)
            elif value==count[result[-1]]:
                result.append(key)

        return result