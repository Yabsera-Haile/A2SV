# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helperFunc(left,right):
            if right==left:
                return TreeNode(nums[left])

            mid=math.ceil((right+left)/2)
            root=TreeNode(nums[mid])
            if right==mid:
                root.left=helperFunc(left,mid-1)
            else:
                root.left=helperFunc(left,mid-1)
                root.right=helperFunc(mid+1,right)

            return root
        
        return helperFunc(0,len(nums)-1)