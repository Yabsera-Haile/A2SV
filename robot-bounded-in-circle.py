class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #0:North, 1:East, 2:South, 3:West
        position=[0]*4
        direction=0

        for inst in instructions*4:
            if inst=="G":
                position[direction]+=1
            elif inst=="L":
                if direction==0:
                    direction=3
                else:
                    direction-=1
            else:
                if direction==3:
                    direction=0
                else:
                    direction +=1

        vertical=position[0]-position[2]
        horizontal=position[1]-position[3]
        if vertical==0 and horizontal==0:
            return True
        else:
            return False