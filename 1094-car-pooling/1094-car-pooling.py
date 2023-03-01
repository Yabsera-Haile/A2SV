class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        nums=[0]*1000

        for trip in trips:
            nums[trip[1]]+=trip[0]
            if trip[2]!=1000:
                nums[trip[2]]-=trip[0]
        
        result=0
        print(nums[:10])
        for num in nums:
            result+=num
            if result>capacity:
                return False
        return True



        