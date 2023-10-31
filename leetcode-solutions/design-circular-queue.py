class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[]
        self.max=k
        self.tail=0
        self.head=0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            self.head+=1
            return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.tail+=1
            return True

        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head-1]

    def isEmpty(self) -> bool:
        if self.head-self.tail==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.head-self.tail==self.max:
            return True
        else:
            return False

        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()