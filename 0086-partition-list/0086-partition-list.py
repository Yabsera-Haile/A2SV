# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:       
        head_large=large=ListNode()
        head_small=small=ListNode()
        
        while head:
            if head.val<x:
                small.next=head
                small=head
                head=head.next
            else:
                large.next=head
                large=head
                head=head.next
        large.next=None
        small.next = head_large.next
        
        return head_small.next
    
















