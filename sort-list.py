# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findMid(head):
            slow=fast=head
            prev=None
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
            prev.next=None
            return [head,slow]
        
        def sorter(head):
            if not head or not head.next:
                return head
            mid=findMid(head)
            left=sorter(mid[0])
            right=sorter(mid[1])

            result=dummy=ListNode()

            while left and right:
                if left.val<right.val:
                    dummy.next=left
                    left,dummy=left.next,dummy.next
                else:
                    dummy.next=right
                    right,dummy=right.next,dummy.next
            dummy.next=left or right

            return result.next
        
        return sorter(head)