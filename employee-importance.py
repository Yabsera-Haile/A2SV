"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        subs=defaultdict(list)
        importance={}
        for employee in employees:
            importance[employee.id]=employee.importance
            subs[employee.id].extend(employee.subordinates)
                
        def dfs(employee):
            if not subs[employee]:
                return importance[employee]
            curr=0
            for sub in subs[employee]:
                curr+=dfs(sub)
            
            return curr+importance[employee]
            
        return dfs(id)