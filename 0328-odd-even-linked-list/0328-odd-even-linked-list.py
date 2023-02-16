# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead=odd=ListNode()
        evenHead=even=ListNode()
        count=0
        while head:
            count+=1
            if count % 2 == 1:
                odd.next=head
                odd=head
            else:
                even.next=head
                even=head
            head=head.next
        even.next=None
        odd.next=evenHead.next
        
        return oddHead.next
        