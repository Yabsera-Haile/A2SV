# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents={}
        def dfs(parent,child):
            parents[child]=parent
            if child==target:
                return child
            if child.left:
                curr= dfs(child,child.left)
                if curr:
                    return curr
            if child.right:
                curr= dfs(child,child.right)
                if curr:
                    return curr
            return None
        seen=set()
        def bfs(root,level):
            seen.add(root)
            queue=deque([root])
            depth=0
            while queue:
                if depth==level:
                    return [curr.val for curr in queue]
                l=len(queue)
                for _ in range(l):
                    curr=queue.popleft()
                    if curr.left and curr.left not in seen:
                        queue.append(curr.left)
                    if curr.right and curr.right not in seen:
                        queue.append(curr.right)
                depth+=1
            return []
        
       
        result=[]
        
        curr=dfs(-1,root)
        depth=k
        while curr!=-1 and depth>=0:
            result.extend(bfs(curr,depth))
            curr=parents[curr]
            depth-=1
        return result