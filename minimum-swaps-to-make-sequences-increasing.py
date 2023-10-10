class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)

        @cache
        def findSwaps(index,swapped):
            if index==n:
                return 0
            
            if nums1[index]>nums1[index-1] and nums2[index]>nums2[index-1]:
                result1= findSwaps(index+1,False)
                result2=inf
                if nums1[index]>nums2[index-1] and nums2[index]>nums1[index-1]:
                    nums1[index],nums2[index]=nums2[index],nums1[index]
                    result2=findSwaps(index+1,True)+1
                    nums1[index],nums2[index]=nums2[index],nums1[index]
                return min(result1,result2)

            nums1[index],nums2[index]=nums2[index],nums1[index]
            result= findSwaps(index+1,True)+1
            nums1[index],nums2[index]=nums2[index],nums1[index]
            
            return result

        result1=findSwaps(1,False)
        nums1[0],nums2[0]=nums2[0],nums1[0]
        result2=findSwaps(1,True)+1

        return min(result1,result2)