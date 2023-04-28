class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue=deque([0])
        seen=set()

        while queue:
            curr=queue.popleft()
            seen.add(curr)

            for key in rooms[curr]:
                if key not in seen:
                    queue.append(key)
        
        if len(seen)==len(rooms):
            return True
        else:
            return False