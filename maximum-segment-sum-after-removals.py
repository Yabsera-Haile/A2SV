class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        parent = [i for i in range(n)]
        rank = [0] * n
        sums = [0] * n
        
        def union(i, j):
            i, j = find(i), find(j)
            if rank[i] < rank[j]:
                i, j = j, i       
            parent[j] = i
            rank[i] += rank[j]
            sums[i] += sums[j]
        
        def find(i):
            while i != parent[i]:
                parent[i] = i = parent[parent[i]]
            return i
        
        for i in range(n - 1, 0, -1):
            j = removeQueries[i]
            sums[j] = nums[j]
            if j and sums[j - 1]:
                union(j, j - 1)
            if j != n - 1 and sums[j + 1]:
                union(j, j + 1)
            result[i - 1] = max(result[i], sums[find(j)])
        
        return result