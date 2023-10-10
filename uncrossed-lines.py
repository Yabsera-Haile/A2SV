class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)

        @cache
        def findLines(index1,index2):
            if index1>=n or index2>=m:
                return 0
            
            result=0
            for i in range(index1,n):
                for j in range(index2,m):
                    if nums1[i]==nums2[j]:
                        result=max(result,findLines(i+1,j+1)+1)
           
            return result
        
        return findLines(0,0)