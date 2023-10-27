class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        unused_rooms = list(range(n))
        heapify(unused_rooms)
        used_rooms = []
        count = defaultdict(int)

        for start, end in meetings:
            while len(used_rooms) > 0 and used_rooms[0][0] <= start:
                heappush(unused_rooms, heappop(used_rooms)[1])
                
            if len(unused_rooms) == 0:
                time, room = heappop(used_rooms)
                count[room]+=1
                heappush(used_rooms,(max(start,time)+(end-start),room))
            else:
                room = heappop(unused_rooms)
                count[room]+=1
                heappush(used_rooms,(start+(end-start),room))
                
        _max = max(count.values())
        result=filter(lambda room: count[room]==_max,range(n))
        return min(result)   