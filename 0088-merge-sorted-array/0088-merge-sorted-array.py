class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #set initial values of the pointers
        pointer1=m-1
        pointer2=n-1
        current=m+n-1
        
        #iterate nums1 and insert the larger value between pointer1 and pointer2 in current
        while current>=0:
            #If pointer2 is negative then nums1 is sorted
            if pointer2<0:
                break
            #If pointer1 is negative then copy values of pointer2 to the remainging portion
            elif pointer1<0:
                nums1[current]=nums2[pointer2]
                current-=1  
                pointer2-=1
            #Check wheather pointer1 or pointer2 is pointing to the larger value
            elif nums1[pointer1]>=nums2[pointer2]:
                nums1[current]=nums1[pointer1]
                pointer1-=1
                current-=1
            else:
                nums1[current]=nums2[pointer2]
                pointer2-=1
                current-=1                


        