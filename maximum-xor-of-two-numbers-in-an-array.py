class Solution:
    def insert(self, num):
        curr = self.root 
        for shift in range(self.n, -1, -1):           
            val = 1 if num & (1 << shift) else 0     
            if val not in curr:
                curr[val] = {}
            curr = curr[val]   

    def findMaximumXOR(self, nums: List[int]) -> int:
        self.n = len(bin(max(nums))) - 2             
        self.root = {}
        for num in nums: 
            self.insert(num)           
            
        result = 0
        for num in nums:     
            curr=""                       
            node = self.root 
            
            for shift in range(self.n, -1, -1):
                val = 1 if num & (1 << shift) else 0  
                if 1-val in node:
                    node=node[1-val]
                    curr+=str(1-val)
                else:
                    node=node[val]
                    curr+=str(val)

            result = max(result, int(curr,2)^num)     

        return result