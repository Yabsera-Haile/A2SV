# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # BFS
        result=1
        queue=deque([(root,0)])

        while queue:
            l=len(queue)
            result=max(result,queue[-1][1]-queue[0][1]+1)

            for _ in range(l):
                node,level = queue.popleft()
                if node.left:
                    queue.append((node.left,level*2+1))
                if node.right:
                    queue.append((node.right,level*2+2))
        
        return result


        # DFS
        # count=defaultdict(list)
        # result=0
        # def helperFunc(root,depth,val):
        #     if root:
        #         count[depth].append(val)

        #         helperFunc(root.left,depth+1,2*val)
        #         helperFunc(root.right,depth+1,2*val+1)
        
        # helperFunc(root,0,1)
        # for key,value in count.items():
        #     curr=value[-1]-value[0]+1
        #     result=max(result,curr)
        
        # return result