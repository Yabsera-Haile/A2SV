class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent=[i for i in range(n)]

        def find(member):
            root=member
            
            while root!=parent[root]:
                root=parent[root]
            while member!=root:
                member,parent[member]=parent[member],root

            return root
        
        def union(member1,member2):
            root1=find(member1)
            root2=find(member2)
            if root1==root2 or root2!=member2:
                return False

            parent[root2]=root1
            return True
        
        for i in range(n):
            if leftChild[i]!=-1:
                if not union(i,leftChild[i]):
                    return False
            if rightChild[i]!=-1:
                if not union(i,rightChild[i]):
                    return False
        count=0
        for i,par in enumerate(parent):
            if par==i:
                count+=1
        
        return True if count==1 else False