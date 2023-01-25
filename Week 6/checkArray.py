class Solution:
    def arraySortedOrNot(self, arr, n):
        for index in range(n-1):
            if arr[index] > arr[index+1]:
                return 0
        return 1
