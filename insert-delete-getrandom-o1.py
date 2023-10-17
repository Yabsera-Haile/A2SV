class RandomizedSet:

    def __init__(self):
        self.pos={}
        self.nums=[]

    def insert(self, val: int) -> bool:
        if val not in self.pos or self.pos[val]==-1:
            self.pos[val]=len(self.nums)
            self.nums.append(val)
            return True
       
        return False     

    def remove(self, val: int) -> bool:
        if val not in self.pos or self.pos[val]==-1:
            return False
        curr=self.pos[val]
        self.pos[self.nums[-1]]=curr
        self.nums[curr],self.nums[-1]=self.nums[-1],self.nums[curr]
        self.pos[val]=-1
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()