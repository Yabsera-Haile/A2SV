# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result=[]
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if not node:
                result.append("#")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(result)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data=="#":
            return None
        tree=data.split(",")
        root=TreeNode(tree[0])
        queue=deque([root])
        i=0

        while queue:
            node=queue.popleft()
            i+=1
            if tree[i]=="#":
                node.left=None
            else:
                node.left=TreeNode(int(tree[i]))
                queue.append(node.left)
            i+=1
            if tree[i]=="#":
                node.right=None
            else:
                node.right=TreeNode(int(tree[i]))
                queue.append(node.right)
        
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))