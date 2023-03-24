def solution():
    t=int(input())

    for _ in range(t):
        result=0
        def mergeSort(left, right, arr):
            nonlocal result
            if left==right:
                return arr
            if left == right-1:
                if arr[right]<arr[left]:
                    result+=1
                    return [arr[right],arr[left]]
                else:
                    return [arr[left],arr[right]]
                        
            mid = (left + right) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)


        def merge(left_arr, right_arr):
            nonlocal result
            temp = []
            if left_arr[0]>=right_arr[-1]:
                result+=1
                temp.extend(right_arr)
                temp.extend(left_arr)
            else:
                temp.extend(left_arr)
                temp.extend(right_arr)
            return temp
        
        m=int(input())
        nums=list(map(int,input().split()))
        
        if sorted(nums) == mergeSort(0,len(nums)-1,nums):
            print(result)
        else:
            print(-1)

solution()