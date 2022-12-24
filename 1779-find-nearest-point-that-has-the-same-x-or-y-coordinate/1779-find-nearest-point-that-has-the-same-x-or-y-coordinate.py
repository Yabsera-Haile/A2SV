class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        #build hashmap to keep track of original index
        hashmap={index:point for index,point in enumerate(points)}
        
        #filter only valid points
        points=[point for point in points if point[0]==x or point[1]==y]
        print(points)
        
        # calculate the manhattan distance dictionary
        distance={}
        for point in points:
            keys = list(hashmap.keys())
            vals = list(hashmap.values())
            distance[keys[vals.index(point)]]=abs(point[0]-x)+abs(point[1]-y)
        print(distance)
        #Find the smallest Manhatan distace
        result=0
        minimum=10**4
        for key,value in distance.items():
            if value == minimum:
                result=min(result,key)
            elif value < minimum:
                minimum=value
                result=key
        if len(points)==0:
            result=-1
        return result