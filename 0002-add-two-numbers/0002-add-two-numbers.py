# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=digit=ListNode(0)
        rem=0
        while l1 or l2 or rem:
            num1=l1.val if l1 else 0
            num2=l2.val if l2 else 0
            curr=num1+num2+rem
            digit.next=ListNode(curr%10)
            rem=curr//10
            l1=l1.next if l1 else l1
            l2=l2.next if l2 else l2
            digit=digit.next
            
        return result.next
            
            
            
            
        