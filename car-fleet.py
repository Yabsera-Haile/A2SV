class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars={}
        for i in range(len(position)):
            cars[position[i]]=speed[i]
        
        stack=[]
        for pos,speed in sorted(cars.items(),reverse=True):
            time=(target-pos)/speed
            stack.append(time)

            if len(stack)>1 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)