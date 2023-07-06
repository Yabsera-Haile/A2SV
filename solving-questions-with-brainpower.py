class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = [0] * len(questions)
        memo[-1] = questions[-1][0]
        
        for i in range(len(questions) - 2, -1, -1):
            memo[i],skiped = questions[i]
            if i + skiped + 1 < len(questions):
                memo[i] += memo[i + skiped + 1]

            memo[i] = max(memo[i], memo[i + 1])
        
        return memo[0]