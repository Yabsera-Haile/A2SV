class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent=[i for i in range(n)]
        parent[firstPerson]=0
        meetings.sort(key=lambda x:x[2])

        def find(person):
            root=person
            while root!=parent[root]:
                root=parent[root]
            
            while person!=root:
                temp=parent[person]
                parent[person]=root
                person=temp
            return root
        
        def union(person1,person2):
            parent1=find(person1)
            parent2=find(person2)

            if parent1!=parent2:
                if parent1<parent2:
                    parent[parent2]=parent1
                else:
                    parent[parent1]=parent2

        result=set([0,firstPerson])
        prev_time=meetings[0][2]
        meeting_group=[]
        prev_meet=[[meetings[0][0],meetings[0][1]]]

        for x,y,time in meetings[1:]:
            if time==prev_time:
                prev_meet.append([x,y])
            else:
                meeting_group.append(prev_meet)
                prev_meet=[[x,y]]
                prev_time=time
        meeting_group.append(prev_meet)

        for meeting in meeting_group:
            for x,y in meeting:
                union(x,y)
                
            for x,y in meeting:
                parentX=find(x)
                parentY=find(y)
                if parentX!=0:
                    parent[x]=x
                    parent[y]=y
                else:
                    result.add(x)
                    result.add(y)

        return list(result)