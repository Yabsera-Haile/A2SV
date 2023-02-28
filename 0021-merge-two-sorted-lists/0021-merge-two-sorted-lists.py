# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result=temp=ListNode()
        
        def helperFunc(list1,list2,result):
            if list1 and list2:
                if list1.val<list2.val:
                    result.next=list1
                    helperFunc(list1.next,list2,result.next)
                else:
                    result.next=list2
                    helperFunc(list1,list2.next,result.next)
            elif list1:
                result.next=list1
                helperFunc(list1.next,list2,result.next)
            elif list2:
                result.next=list2
                helperFunc(list1,list2.next,result.next)
            else:
                return result
        
        result=helperFunc(list1,list2,result)
        return temp.next        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # result=temp=ListNode()
        # while list1 and list2:
        #     if list1.val<list2.val:
        #         result.next=list1
        #         list1,result=list1.next,result.next
        #     else:
        #         result.next=list2
        #         list2,result=list2.next,result.next
        # if list1 or list2:
        #     result.next=list1 if list1 else list2
        # return temp.next