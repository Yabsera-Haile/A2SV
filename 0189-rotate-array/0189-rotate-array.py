class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(0,k):
            temp=nums.pop(-1)
            nums.insert(0,temp)
        