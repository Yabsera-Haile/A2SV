class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.num = 0
        self.ones = 0

    def fix(self, idx: int) -> None:
        num = self.num | (1 << (self.size-idx-1))
        if num != self.num:
            self.ones += 1
        self.num = num

    def unfix(self, idx: int) -> None:
        num = self.num & ((1 << (self.size-idx-1))^((1 << self.size) - 1))
        if num != self.num:
            self.ones -= 1
        self.num = num
        
    def flip(self) -> None:
        self.num ^= ((1 << self.size) - 1)
        self.ones = self.size-self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        bit=bin(self.num)[2:]
        bit=(("0"*(self.size-len(bit)))+bit)
        return bit
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()