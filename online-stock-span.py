class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.stock=[]
        self.ref=defaultdict(int)
        self.count=0

    def next(self, price: int) -> int:
        result=0

        while self.stack and self.stock[-1]<=price:
            result+=self.ref[self.stack.pop()]
            self.stock.pop()

        self.ref[self.count]+=result+1
        self.stack.append(self.count)
        self.stock.append(price)
        self.count+=1
        # print(self.ref,self.stock,self.stack)
        return result+1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)