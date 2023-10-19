# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=num2=0
        while l1!=None:
            num1=(num1*10)+l1.val
            l1=l1.next

        while l2!=None:
            num2=(num2*10)+l2.val
            l2=l2.next

        head=dummy=ListNode(0)

        result=str(num1+num2)
        for num in result:
            dummy.next=ListNode(num)
            dummy=dummy.next

        return head.next