class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king=kingName
        self.graph=defaultdict(list)
        self.dead=set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)     

    def getInheritanceOrder(self) -> List[str]:
        # print(self.graph)
        throne = []
        def dfs(successor):
            if successor not in self.dead:
                throne.append(successor)

            if successor in self.graph:
                for child in self.graph[successor]:
                    dfs(child)
        dfs(self.king)
        return throne

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()