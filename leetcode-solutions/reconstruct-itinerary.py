class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        tickets.sort(reverse=True)

        for src,dist in tickets:
            graph[src].append(dist)

        result=[]

        def findItinerary(loc):
            while graph[loc]:
                findItinerary(graph[loc].pop())

            result.append(loc)
        
        findItinerary("JFK")

        return reversed(result)
            



        