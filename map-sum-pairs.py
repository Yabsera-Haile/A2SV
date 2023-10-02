class TrieNode:
    def __init__(self):
        self.children={}
        self.val=0

class MapSum:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr=self.root
        for letter in key:
            if letter not in curr.children:
                curr.children[letter]=TrieNode()

            curr=curr.children[letter]        
        curr.val=val

    def sum(self, prefix: str) -> int:
        curr=self.root
        for letter in prefix:
            if letter not in curr.children:
                return 0
            curr=curr.children[letter]
        
        return self.findSum(curr)
    
    def findSum(self,node):
        result=node.val
        for child in node.children.values():
            print(child)
            result+=self.findSum(child)  
        return result

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)