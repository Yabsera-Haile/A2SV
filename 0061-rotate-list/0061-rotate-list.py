# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        counter=head
        end=start=None
        if head:
            while counter:
                count+=1
                end=counter
                counter=counter.next
            k=k%count
            if count==1 or k==0:
                start=head
            else:
                counter=head
                i=0
                while counter:
                    if i==count-k-1:
                        start=counter.next
                        counter.next=None
                        break
                    counter=counter.next 
                    i+=1
                end.next=head
        return start
        
        