# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n=mountain_arr.length()
        def findIndex(left,right):
            while left<=right:
                mid=(left+right)//2
                index=mountain_arr.get(mid)
                if mid==0 or mid==n-1:
                    return mid
                pre=mountain_arr.get(mid-1)
                post=mountain_arr.get(mid+1)
                if pre<index>post:
                    return mid
                elif pre<index<post:
                    left=mid
                elif pre>index>post:
                    right=mid
            return -1
        def findTargetIncreasing(left,right):
            while left<=right:
                mid=(left+right)//2
                index=mountain_arr.get(mid)
                if index==target:
                    return mid
                if index>target:
                    right=mid-1
                elif index<target:
                    left=mid+1
            return -1
        def findTargetDecreasing(left,right):
            while left<=right:
                mid=(left+right)//2
                index=mountain_arr.get(mid)
                if index==target:
                    return mid
                if index>target:
                    left=mid+1
                elif index<target:
                    right=mid-1
            return -1
        
        top= findIndex(0,n-1)
        
        result = findTargetIncreasing(0,top)
        if result!=-1:
            return result
        return findTargetDecreasing(top,n-1)