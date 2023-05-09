class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index,task in enumerate(tasks):
            task.append(index)
        
        tasks.sort()
        heap=[]
        index=0
        time=tasks[index][0]
        result=[]
        while index<len(tasks) or heap:
            if not heap and time<tasks[index][0]:
                time=tasks[index][0]

            while index<len(tasks) and tasks[index][0]<=time:
                undone=tasks[index]
                heappush(heap,(undone[1],undone[2]))
                index+=1

            dur,task=heappop(heap)
            time+=dur
            result.append(task)
        
        return result