class DetectSquares:

    def __init__(self):
        self.points=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        
    def count(self, point: List[int]) -> int:
        result=0
        x0,y0=point

        for (x,y),count in self.points.items():
            distX=abs(x-x0)
            distY=abs(y-y0)
            if distX==distY and distY!=0 and (x,y0) in self.points and (x0,y) in self.points:
                result+= (count * self.points[(x,y0)] * self.points[x0,y])
        
        return result

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)