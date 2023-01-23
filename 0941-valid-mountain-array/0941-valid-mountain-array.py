class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) >=3 :  
            
            maxi = arr.index(max(arr))
            if maxi!=0 and maxi!=len(arr)-1:
                left = arr[:maxi]
                right = arr[maxi:]
                left_arr = sorted(left)
                right_arr = sorted(right,reverse=True)
                
                size_right_set = len(set(right))
                size_left_set = len(set(left))
                size_left_arr = len(left_arr)
                size_right_arr = len(right_arr)
                
                if left_arr == left and size_left_set == size_left_arr and right == right_arr                   and size_right_set == size_right_arr:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
