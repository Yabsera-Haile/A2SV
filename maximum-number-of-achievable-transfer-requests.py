class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        result =  0   
        buildings = [0] * n

        def backtrack(start, curr):
            nonlocal result
            if start < len(requests):
                for index in range(start, len(requests)):
                    curr.append(requests[index])
                    prev, new = requests[index]
                    buildings[prev] -= 1
                    buildings[new] += 1
                    
                    if all(employees == 0 for employees in buildings):
                        result = max(result, len(curr))
                    
                    backtrack(index + 1, curr)
                    request = curr.pop()
                    prev, new = request
                    buildings[prev] += 1
                    buildings[new] -= 1
            
            return
        
        backtrack(0, [])
        
        return result