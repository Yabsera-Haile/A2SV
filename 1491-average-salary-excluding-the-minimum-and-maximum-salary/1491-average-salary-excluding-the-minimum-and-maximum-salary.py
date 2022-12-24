class Solution:
    def average(self, salary: List[int]) -> float:
        #sort salart
        salary.sort() 
        #cast the int values to float
        salary=[float(sal) for sal in salary]
        length=len(salary)-2
        result= sum(salary[1:-1])
        return result/length
        
        