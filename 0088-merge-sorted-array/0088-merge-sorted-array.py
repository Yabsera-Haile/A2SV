class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #set initial values of the pointers
        pointer1=m-1
        pointer2=n-1
        pointer3=m+n-1
        
        #pointer3 iterates the whole nums1 while inserting the larger number among pointer1 and         pointer2
        while pointer3>=0:
            #If either of the pointers is negat
            if pointer2<0:
                break
            elif pointer1<0:
                nums1[pointer3]=nums2[pointer2]
                pointer3-=1  
                pointer2-=1
            #Check wheather pointer1 or pointer2 is pointing to the larger value
            elif nums1[pointer1]>=nums2[pointer2]:
                nums1[pointer3]=nums1[pointer1]
                pointer1-=1
                pointer3-=1
            else:
                nums1[pointer3]=nums2[pointer2]
                pointer2-=1
                pointer3-=1                


        