# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current=prev=head
        i=1
    
        while i < left:
            prev , current = current , current.next
            i +=1
            
        start = None
        end = current
        
        while i >= left and i <= right:
            temp = current.next
            current.next = start
            start = current
            current = temp
            i +=1
            
        prev.next = start
        end.next =current
        
        if left >1:
            return head
        else:
            return start
        